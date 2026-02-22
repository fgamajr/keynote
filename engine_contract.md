# engine_contract.md

## 1. Scene Lifecycle

```
                    ┌─────────────────┐
                    │    UNMOUNTED    │
                    └────────┬────────┘
                             │ Engine.mount(scene)
                             ▼
                    ┌─────────────────┐
                    │   INITIALIZED   │
                    │  (DOM created)  │
                    └────────┬────────┘
                             │ Engine.enter(scene)
                             ▼
                    ┌─────────────────┐
                    │     ENTER       │
                    │  (animate in)   │
                    └────────┬────────┘
                             │ enter() completes
                             ▼
                    ┌─────────────────┐
                    │    ACTIVE       │◄──────┐
                    │ (scroll-driven) │       │
                    └────────┬────────┘       │
                             │ update()       │
                             ▼                │
                    ┌─────────────────┐       │
                    │    UPDATE       │───────┘
                    │ (progress 0→1)  │
                    └────────┬────────┘
                             │ Engine.exit(scene)
                             ▼
                    ┌─────────────────┐
                    │     EXIT        │
                    │  (animate out)  │
                    └────────┬────────┘
                             │ exit() completes
                             ▼
                    ┌─────────────────┐
                    │    UNMOUNTED    │
                    │  (DOM removed)  │
                    └─────────────────┘
```

### Lifecycle Hooks

| Hook | Called By | Timing | Return |
|------|-----------|--------|--------|
| `enter()` | Engine | Scene becomes visible | Promise<void> |
| `update(progress)` | Engine | Every scroll frame | void |
| `exit()` | Engine | Scene leaving viewport | Promise<void> |
| `getHeight()` | Engine | Mount time | number (vh) |
| `getAccessibilityContent()` | Engine | Fallback mode | string (HTML) |

### Mounting Rules

1. **Eager Mount**: Scene mounted when scroll within 200vh of start
2. **Lazy Unmount**: Scene unmounted when scroll >200vh past end
3. **Max Concurrent**: 5 scenes mounted simultaneously
4. **DOM Isolation**: Each scene renders to isolated container

---

## 2. Scene State Model

### Scene State Shape

```typescript
interface SceneState {
  // Immutable config (set once at mount)
  readonly id: string;
  readonly startScroll: number;    // vh position
  readonly endScroll: number;      // vh position
  readonly height: number;         // vh units
  
  // Mutable internal state (private to scene)
  phase: 'enter' | 'settled' | 'exit' | 'inactive';
  progress: number;                // 0.0 → 1.0
  localProgress: number;           // Phase-relative 0.0 → 1.0
  
  // Derived (computed by engine, read-only by scene)
  isActive: boolean;
  distanceFromViewport: number;    // vh units
}
```

### Phase Boundaries

| Phase | Progress Range | LocalProgress | Purpose |
|-------|----------------|---------------|---------|
| `enter` | 0.00 - 0.33 | (progress - 0) / 0.33 | Elements appear |
| `settled` | 0.33 - 0.66 | (progress - 0.33) / 0.33 | Full visibility |
| `exit` | 0.66 - 1.00 | (progress - 0.66) / 0.33 | Elements depart |

### State Invariants

1. **Progress Monotonic**: Never decreases during active phase
2. **Phase Deterministic**: Same progress → same phase, always
3. **No Shared State**: Scenes cannot access other scene states
4. **Immutable Config**: startScroll, endScroll fixed after mount

---

## 3. Scroll Progress Mapping

### Global Scroll Space

```
Total Document Height: 2000vh (configurable)
Scene Height: 100vh per scene (configurable via getHeight())
Transition Overlap: 50vh between scenes

Scene 0:   0vh   → 100vh
Scene 1:  100vh  → 200vh
Scene 2:  200vh  → 300vh
...
Scene 18: 1800vh → 1900vh
Buffer:   1900vh → 2000vh (no scene)
```

### Progress Calculation

```typescript
function calculateProgress(
  scrollY: number,      // Current scroll position (px)
  sceneStart: number,   // Scene start (vh)
  sceneEnd: number      // Scene end (vh)
): number {
  const vh = window.innerHeight / 100;
  const startPx = sceneStart * vh;
  const endPx = sceneEnd * vh;
  const sceneHeight = endPx - startPx;
  
  const rawProgress = (scrollY - startPx) / sceneHeight;
  return clamp(rawProgress, 0.0, 1.0);
}
```

### Phase Calculation

```typescript
function calculatePhase(progress: number): Phase {
  if (progress < 0.33) return 'enter';
  if (progress < 0.66) return 'settled';
  return 'exit';
}

function calculateLocalProgress(progress: number, phase: Phase): number {
  switch (phase) {
    case 'enter': return progress / 0.33;
    case 'settled': return (progress - 0.33) / 0.33;
    case 'exit': return (progress - 0.66) / 0.33;
  }
}
```

### Scroll Event Handling

```typescript
// Engine-side (single listener)
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  
  mountedScenes.forEach(scene => {
    const progress = calculateProgress(scrollY, scene.start, scene.end);
    scene.update(progress);
  });
}, { passive: true });
```

---

## 4. Animation Triggering Rules

### What Triggers Animation

| Trigger | Source | Allowed Actions |
|---------|--------|-----------------|
| `enter()` call | Engine on mount | CSS transitions, Web Animations API, GSAP |
| `update(progress)` | Scroll position | `transform`, `opacity` updates only |
| `exit()` call | Engine on unmount | CSS transitions, Web Animations API, GSAP |

### Animation Constraints

1. **Scroll-Driven Only**: `update()` must not use time-based animations
2. **GPU Properties Only**: Only `transform` and `opacity` in `update()`
3. **No Layout Thrashing**: No reads of layout properties in `update()`
4. **Deterministic**: Same progress → same visual state, always

### Interpolation Utilities (Provided by Engine)

```typescript
// Available in scene context
lerp(start: number, end: number, progress: number): number
easeOutQuad(t: number): number
easeInOutCubic(t: number): number
clamp(value: number, min: number, max: number): number
```

### Animation Anti-Patterns (Forbidden)

```typescript
// ❌ NEVER DO THIS
update(progress) {
  setTimeout(() => { this.animate(); }, 100);  // Time-based
  requestAnimationFrame(() => { this.move(); }); // Uncontrolled loop
  this.element.style.width = '100px';  // Layout property
  this.x += 1;  // State mutation without scroll input
}

// ✅ CORRECT
update(progress) {
  const x = lerp(0, 100, easeOutQuad(progress));
  this.element.style.transform = `translateX(${x}vw)`;
}
```

---

## 5. Allowed Side Effects

### Permitted Side Effects

| Effect | Context | Constraints |
|--------|---------|-------------|
| DOM mutations | enter(), exit() | Must complete before Promise resolves |
| Style mutations | update() | GPU properties only |
| Image loading | enter() | Must be cached before update() calls |
| Event listeners | mount() | Must remove on unmount() |
| Console logging | Any | Debug builds only |

### Forbidden Side Effects

| Effect | Reason |
|--------|--------|
| Network requests | Non-deterministic timing |
| localStorage writes | Side effects unpredictable |
| URL mutations | Breaks scroll position |
| Global state writes | Violates isolation |
| setTimeout/setInterval | Time-based, not scroll-based |
| alert/confirm/prompt | Blocks thread |

### Scene API Surface

```typescript
// Scene receives from Engine
interface SceneContext {
  readonly container: HTMLElement;     // Scene root element
  readonly id: string;                  // Scene identifier
  
  // Utilities
  lerp(start: number, end: number, t: number): number;
  easeOutQuad(t: number): number;
  easeInOutCubic(t: number): number;
  clamp(value: number, min: number, max: number): number;
}

// Scene exports to Engine
interface Scene {
  enter(): Promise<void>;
  update(progress: number): void;
  exit(): Promise<void>;
  getHeight(): number;  // returns vh units
  getAccessibilityContent(): string;  // returns HTML string
}
```

---

## 6. Performance Constraints

### Frame Budget

| Operation | Budget | Measurement |
|-----------|--------|-------------|
| `update()` execution | < 2ms | per scene |
| Total frame time | < 16ms | all scenes |
| Style calculations | < 5ms | per frame |
| Layout | Avoid | never trigger |
| Paint | < 8ms | per frame |

### Memory Budget

| Resource | Limit | Enforcement |
|----------|-------|-------------|
| DOM nodes per scene | < 200 | Static analysis |
| Images per scene | < 10 | Code review |
| Event listeners | Clean up | Lint rule |
| Closure retention | None after exit | Profiling |

### Optimization Requirements

```typescript
// Required pattern for animated elements
class Scene {
  private animatedElements: HTMLElement[] = [];
  
  enter() {
    // Set will-change before animation
    this.animatedElements.forEach(el => {
      el.style.willChange = 'transform, opacity';
    });
  }
  
  exit() {
    // Remove will-change after animation
    return new Promise(resolve => {
      // ... animation complete
      this.animatedElements.forEach(el => {
        el.style.willChange = 'auto';
      });
      resolve();
    });
  }
}
```

### Performance Killers (Auto-Rejected)

- `filter: blur()` in `update()`
- `box-shadow` animation in `update()`
- Layout property reads in `update()`
- Unthrottled scroll listeners
- Memory leaks in closures

---

## 7. Accessibility Fallback

### Fallback Modes

| Mode | Trigger | Behavior |
|------|---------|----------|
| **Full** | JS enabled, no pref | Scroll-driven animations |
| **Reduced Motion** | `prefers-reduced-motion: reduce` | Opacity fades only, no transforms |
| **No JS** | `<noscript>` or JS error | Static HTML from `getAccessibilityContent()` |

### getAccessibilityContent() Contract

```typescript
/**
 * Returns semantic HTML for fallback display.
 * Called by Engine when:
 * - JavaScript is disabled
 * - Scene fails to load
 * - Reduced motion strongly preferred
 * 
 * Must return complete, readable content.
 * No animations. No interactive elements.
 */
getAccessibilityContent(): string {
  return `
    <section aria-labelledby="scene-${this.id}-title">
      <h2 id="scene-${this.id}-title">Scene Title</h2>
      <p>Content description...</p>
      <dl>
        <dt>Key Metric</dt>
        <dd>27.1%</dd>
      </dl>
    </section>
  `;
}
```

### Reduced Motion Implementation

```typescript
update(progress: number) {
  const prefersReducedMotion = 
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  if (prefersReducedMotion) {
    // Opacity only, instant at threshold
    this.element.style.opacity = progress > 0.5 ? '1' : '0';
  } else {
    // Full animation
    const x = lerp(0, 100, easeOutQuad(progress));
    this.element.style.transform = `translateX(${x}vw)`;
    this.element.style.opacity = String(progress);
  }
}
```

### No-JS Fallback Structure

```html
<!-- Engine renders this when JS disabled -->
<div id="presentation-fallback">
  <section><!-- Scene 0 accessibility content --></section>
  <section><!-- Scene 1 accessibility content --></section>
  <!-- ... all scenes ... -->
</div>

<noscript>
  <style>
    #presentation-engine { display: none; }
    #presentation-fallback { display: block; }
  </style>
</noscript>
```

### Screen Reader Support

```typescript
// Scene must set ARIA attributes in enter()
enter() {
  this.container.setAttribute('role', 'region');
  this.container.setAttribute('aria-label', 'Scene Title');
  
  // Live regions for dynamic content
  this.metricsElement.setAttribute('aria-live', 'polite');
  this.metricsElement.setAttribute('aria-atomic', 'true');
}
```

---

## 8. Scene Implementation Template

```typescript
class ExampleScene implements Scene {
  private container: HTMLElement;
  private elements: Map<string, HTMLElement> = new Map();
  private context: SceneContext;
  
  constructor(context: SceneContext) {
    this.context = context;
    this.container = context.container;
    this.buildDOM();
  }
  
  // Required: Initial animation
  async enter(): Promise<void> {
    this.elements.forEach(el => {
      el.style.willChange = 'transform, opacity';
    });
    
    // Animate in
    await this.animateOpacity(0, 1, 300);
  }
  
  // Required: Scroll-driven update
  update(progress: number): void {
    // Calculate phase
    let localProgress: number;
    if (progress < 0.33) {
      localProgress = progress / 0.33;
      this.updateEnter(localProgress);
    } else if (progress < 0.66) {
      localProgress = (progress - 0.33) / 0.33;
      this.updateSettled(localProgress);
    } else {
      localProgress = (progress - 0.66) / 0.33;
      this.updateExit(localProgress);
    }
  }
  
  // Required: Cleanup animation
  async exit(): Promise<void> {
    await this.animateOpacity(1, 0, 300);
    
    this.elements.forEach(el => {
      el.style.willChange = 'auto';
    });
  }
  
  // Required: Height in vh
  getHeight(): number {
    return 100; // vh units
  }
  
  // Required: Static fallback
  getAccessibilityContent(): string {
    return `
      <section>
        <h2>Scene Title</h2>
        <p>Description for screen readers and no-JS fallback.</p>
      </section>
    `;
  }
  
  // Private: Build scene DOM
  private buildDOM(): void {
    this.container.innerHTML = `
      <div class="scene-content">
        <div class="element" data-key="main"></div>
      </div>
    `;
    
    this.elements.set('main', 
      this.container.querySelector('[data-key="main"]')
    );
  }
  
  // Private: Phase-specific updates
  private updateEnter(progress: number): void {
    const x = this.context.lerp(-100, 0, this.context.easeOutQuad(progress));
    this.elements.get('main').style.transform = `translateX(${x}vw)`;
  }
  
  private updateSettled(progress: number): void {
    // Hold position or subtle motion
  }
  
  private updateExit(progress: number): void {
    const x = this.context.lerp(0, 100, this.context.easeInOutCubic(progress));
    this.elements.get('main').style.transform = `translateX(${x}vw)`;
  }
  
  // Private: Utility (use Engine utilities instead in production)
  private animateOpacity(from: number, to: number, duration: number): Promise<void> {
    return new Promise(resolve => {
      const start = performance.now();
      const element = this.elements.get('main');
      
      const frame = (now: number) => {
        const elapsed = now - start;
        const progress = Math.min(elapsed / duration, 1);
        element.style.opacity = String(from + (to - from) * progress);
        
        if (progress < 1) {
          requestAnimationFrame(frame);
        } else {
          resolve();
        }
      };
      
      requestAnimationFrame(frame);
    });
  }
}

// Export factory function
export function createScene(context: SceneContext): Scene {
  return new ExampleScene(context);
}
```

---

## 9. Engine Integration Contract

### Engine Responsibilities

```typescript
interface Engine {
  // Scene management
  registerScene(id: string, factory: SceneFactory): void;
  mountScene(id: string): void;
  unmountScene(id: string): void;
  
  // Scroll handling
  getScrollPosition(): number;
  scrollToScene(id: string): void;
  
  // Utilities exposed to scenes
  lerp(start: number, end: number, t: number): number;
  easeOutQuad(t: number): number;
  easeInOutCubic(t: number): number;
  clamp(value: number, min: number, max: number): number;
}
```

### Registration

```typescript
// In scene file
import { createScene as createScene0 } from './scenes/Scene0';
import { createScene as createScene1 } from './scenes/Scene1';

// In engine
engine.registerScene('scene-0', createScene0);
engine.registerScene('scene-1', createScene1);
// ... etc
```

### Scroll Coordinate System

| Unit | Description | Conversion |
|------|-------------|------------|
| `vh` | Viewport height | 1vh = window.innerHeight / 100 |
| `vw` | Viewport width | 1vw = window.innerWidth / 100 |
| `px` | Pixels | Device-dependent |
| `progress` | Scene-relative | 0.0 = start, 1.0 = end |

All scene positioning uses `vh` units. Engine converts to pixels for DOM.

---

## 10. Validation Rules

### Static Analysis Checks

```yaml
rules:
  - name: no-settimeout-in-update
    pattern: "update.*setTimeout"
    severity: error
    message: "Time-based animations forbidden in update()"
    
  - name: no-layout-properties
    pattern: "style\.(width|height|top|left|margin|padding)"
    severity: error
    message: "Layout properties forbidden in update()"
    
  - name: will-change-required
    pattern: "enter\(\)[\s\S]*?{[\s\S]*?}"
    must_contain: "willChange"
    severity: warning
    message: "will-change should be set in enter()"
    
  - name: cleanup-required
    pattern: "exit\(\)[\s\S]*?{[\s\S]*?}"
    must_contain: "willChange.*auto"
    severity: warning
    message: "will-change should be removed in exit()"
```

### Runtime Assertions

```typescript
// Engine validates scene compliance
debugAssertSceneCompliance(scene: Scene) {
  // 1. getHeight returns positive number
  const height = scene.getHeight();
  console.assert(height > 0, 'getHeight() must return positive number');
  
  // 2. getAccessibilityContent returns non-empty string
  const a11y = scene.getAccessibilityContent();
  console.assert(a11y.length > 0, 'getAccessibilityContent() must return content');
  console.assert(a11y.includes('<'), 'getAccessibilityContent() must return HTML');
  
  // 3. update is synchronous
  const start = performance.now();
  scene.update(0.5);
  const duration = performance.now() - start;
  console.assert(duration < 2, 'update() must complete in <2ms');
}
```

---

END OF CONTRACT
