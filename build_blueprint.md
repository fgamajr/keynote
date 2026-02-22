# build_blueprint.md

---

# Project Mental Model

## Core Concept
This is a **scroll-driven cinematic narrative** where scroll position acts as a timeline. There are no "slides"—only 19 sequential scenes that occupy defined scroll segments. The viewport is a fixed camera; elements enter, settle, and exit based on scroll progress.

## Architectural Principles
1. **Scroll is time**: No animation durations in milliseconds. All motion computed from scroll position.
2. **Deterministic rendering**: Same scroll position = identical visual state across browsers/devices.
3. **Progressive disclosure**: Information reveals in layers controlled by user scroll speed.
4. **Self-contained scenes**: No shared elements between scenes. Prevents state corruption during rapid scroll.
5. **GPU-only animations**: Only `transform` and `opacity` animate. No layout properties.

## Scene Type Taxonomy
- **Type A (Metaphorical)**: Scenes 0-3. Visual abstraction, camera movement, minimal text.
- **Type B (Evidential)**: Scenes 4-8, 13-15. Data visualization, number animations, proof.
- **Type C (Technical)**: Scenes 9-12, 16-17. Architecture diagrams, static structure revealed through scroll.
- **Type D (Cinematic)**: Scene 18. No scroll-linked animation. Static terminus.

## Narrative Arc
Scene 0 (Personal anchor) → Scenes 1-3 (Metaphor: line/road/planet) → Scenes 4-8 (Problem/Solution narrative) → Scenes 9-12 (Technical safeguards: MCP/Zero Kelvin/Idempotence) → Scenes 13-17 (Results/Demo/Legacy) → Scene 18 (Philosophical conclusion)

---

# System Build Order

## Phase 1: Foundation (Day 1)
```
1.1 Create project structure
    ├── src/
    │   ├── scenes/          (Scene0.tsx through Scene18.tsx)
    │   ├── components/      (Dot, Line, Card, Terminal, etc.)
    │   ├── hooks/           (useScrollProgress, useSceneState)
    │   ├── utils/           (interpolation, clamp, lerp)
    │   └── styles/          (global.css, variables.css)
    ├── public/
    │   └── assets/          (SVGs, optimized images)
    └── index.html

1.2 Install dependencies
    - gsap (with ScrollTrigger)
    - @gsap/react (useGSAP hook)
    - react / react-dom
    - TypeScript
    - Vite (build tool)

1.3 Set up global styles
    - CSS custom properties (colors, typography, spacing)
    - CSS reset (Normalize.css)
    - Dark/light background transition system
```

## Phase 2: Scroll Infrastructure (Day 1-2)
```
2.1 Implement scroll container
    - Native overflow-y: scroll
    - Total height: 2000vh (1900vh content + 100vh buffer)
    - Passive scroll listeners only

2.2 Build scene registry
    - Map scroll ranges to scene indices
    - Compute: sceneIndex = floor(scrollY / 100vh)
    - Track: sceneProgress = (scrollY % 100vh) / 100vh

2.3 Create interpolation utilities
    - lerp(start, end, progress)
    - clamp(value, min, max)
    - easeOutQuad, easeInOutCubic (pre-calculated curves)

2.4 Build Scene wrapper component
    - Receives: sceneIndex, isActive, progress
    - Handles: mount/unmount based on proximity
    - Implements: reduced motion fallback
```

## Phase 3: Scene Implementation (Days 2-4)
```
Implementation order (highest risk first):
1. Scene 1 (Two Dots) - Validates coordinate system
2. Scene 3 (Planet) - Tests 3D/globe performance
3. Scene 2 (Road) - Tests morph transition
4. Scene 0 (Opening) - Polish intro
5. Scene 4 (Problem) - Tests number animations
6. Scene 6 (Architecture) - Tests layer stacking
7. Scene 15 (4 Findings) - Tests grid/count-up
8. Scene 18 (Mic Drop) - Static, tests typography
9. Remaining scenes (5, 7-14, 16-17) - Content population
```

## Phase 4: Integration & Polish (Day 5)
```
4.1 Transition system
    - Cross-fade between scenes (50vh transition corridors)
    - Outgoing: opacity 1→0.3 (first 50% of transition)
    - Incoming: opacity 0→1 (20-100% of transition)

4.2 Reduced motion implementation
    - @media (prefers-reduced-motion: reduce)
    - Disable all transforms, use opacity-only fades
    - Show final values immediately (no count-up)

4.3 Performance optimization
    - will-change: transform on animated elements
    - Remove will-change after animation complete
    - Scene DOM nodes unmount when >2 scenes away

4.4 No-JS fallback
    - All content in semantic HTML order
    - CSS-only layout (no absolute positioning required)
    - Scenes stack vertically as normal document flow
```

## Phase 5: Testing & Deployment (Day 6)
```
5.1 Functional testing
    - All 19 scenes reachable
    - Scroll position → state mapping verified
    - No console errors

5.2 Performance testing
    - Target: 60fps on mid-range laptop
    - Minimum: 30fps on low-end hardware
    - Memory: <100MB heap usage

5.3 Accessibility audit
    - Keyboard navigation (arrow keys)
    - Screen reader announcements
    - WCAG AA color contrast

5.4 Deployment
    - Static file hosting
    - Gzip/brotli compression
    - Cache headers for assets
```

---

# Scene Construction Manual

## SCENE 0: Abertura Pessoal (0-100vh)

**Purpose**: Establish human connection and geographic anchor before abstract concepts.

**Trigger**: scrollY >= 0 && scrollY < 100vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| globe | SVG | assets/scene0/globe.svg | 50KB |
| marker | SVG | assets/scene0/marker-cuiaba.svg | 5KB |

**Required Components**:
- Globe (SVG or CSS radial gradients)
- Pulsing marker (CSS animation)
- Text elements (name, title, location)

**State Transitions**:
```
entrance (0-33%):
  - Globe: opacity 0→1, scale 0.3→0.5, rotation 0°→45°
  - Marker: hidden
  - Text: hidden

settled (33-66%):
  - Globe: stable, rotation continues to 45°
  - Marker: opacity 0→1, scale 0→1, pulse glow active
  - Text: opacity 0→1, staggered reveal

exit (66-100%):
  - Globe: opacity 1→0.2
  - Marker: scale 1→2, opacity 1→0
  - Background: #1A1A2E → #FFFFFF
```

**Done Criteria**:
- [ ] Globe visible and rotating
- [ ] Marker pulses at Cuiabá position
- [ ] Text readable against dark background
- [ ] Background transitions to white at 100vh

---

## SCENE 1: Dois Pontos (100-200vh)

**Purpose**: Establish geometric metaphor—shortest path between two points.

**Trigger**: scrollY >= 100vh && scrollY < 200vh

**Required Assets**: None (CSS/SVG only)

**Required Components**:
- Dot 1 (left): X: 25vw, Y: 50vh, 24px, #0C326F
- Dot 2 (right): X: 75vw, Y: 50vh, 24px, #D4AF37
- Connecting line: gradient #0C326F → #D4AF37, 3px stroke

**State Transitions**:
```
entrance (100-133vh):
  - Dot 1: scroll 100-110vh, opacity 0→1
  - Dot 2: scroll 110-120vh, opacity 0→1
  - Line: scroll 120-133vh, stroke-dashoffset 100%→0%

settled (133-166vh):
  - All elements: stable, fully visible
  - Text: "O caminho mais curto entre dois pontos é uma linha reta"

exit (166-200vh):
  - All elements: hold position for Scene 2 morph
```

**Critical Constraint**: Dot positions must exactly match Scene 2 dot positions (X: 25vw/75vw, Y: 50vh).

**Done Criteria**:
- [ ] Dots appear at exact positions
- [ ] Line draws with scroll
- [ ] Positions match Scene 2 for seamless transition

---

## SCENE 2: A Estrada (200-300vh)

**Purpose**: Break expectation—real world requires curved paths.

**Trigger**: scrollY >= 200vh && scrollY < 300vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| terrain | SVG | assets/scene2/terrain.svg | 30KB |
| road | SVG | assets/scene2/road.svg | 15KB |

**Required Components**:
- Terrain topography (SVG paths)
- Winding road (SVG with stroke-dash animation)
- Straight line (faded to 40%, dashed style)

**State Transitions**:
```
entrance (200-233vh):
  - Dots: maintain position from Scene 1
  - Terrain: y 100%→0%, opacity 0→1
  - Straight line: style solid→dashed, opacity 1→0.4

settled (233-266vh):
  - Road: stroke-dash draw animation, opacity 0→1
  - Road highlighted, straight line subdued
  - Text: "Exceto no mundo real"

exit (266-300vh):
  - All elements stable for transition to Scene 3
```

**Done Criteria**:
- [ ] Terrain rises from below
-- [ ] Road reveals progressively with scroll
- [ ] Straight line fades to ghost state
- [ ] Dots never move position

---

## SCENE 3: O Planeta (300-400vh)

**Purpose**: Universalize metaphor—physics constraints enable orbit.

**Trigger**: scrollY >= 300vh && scrollY < 400vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| globe-wireframe | SVG | assets/scene3/globe.svg | 80KB |

**Required Components**:
- Wireframe globe (SVG or Three.js)
- Brazil marker (Cuiabá): 35% X, 65% Y
- Amsterdam marker: 65% X, 35% Y
- Red dashed line (through center)
- Blue glowing arc (around surface)

**State Transitions**:
```
entrance (300-333vh):
  - Background: #FFFFFF → #1A1A2E (dark slate)
  - Globe: opacity 0→1, scale 0.5→1

settled (333-366vh):
  - Markers: opacity 0→1
  - Red line: stroke-dash draw
  - Blue arc: stroke-dash draw
  - Text: "Restrições tornam soluções possíveis"

exit (366-400vh):
  - Red line: fade to 30%
  - Blue arc: highlight to 100%
```

**Done Criteria**:
- [ ] Background transitions to dark
- [ ] Globe rotates to show South America
- [ ] Lines draw with scroll progress
- [ ] Final state emphasizes blue arc (viable path)

---

## SCENE 4: O Problema (400-500vh)

**Purpose**: Crush viewer with scale—R$ 51B, 11M documents, 2 auditors.

**Trigger**: scrollY >= 400vh && scrollY < 500vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| icons | SVG Set | assets/scene4/icons.svg | 20KB |

**Required Components**:
- Glassmorphism cards (CSS backdrop-filter: blur)
- Number display with count-up animation
- Card 1: R$ 51 Bilhões (#D4AF37)
- Card 2: 3.5 Milhões famílias (#0C326F)
- Card 3: 10.7 Milhões documentos (#0C326F)
- Footer: "63.588 registros na amostra"

**State Transitions**:
```
entrance (400-433vh):
  - Card 1: scroll 400-420vh, opacity 0→1, scale 0.8→1, y 50px→0
  - Number: scroll 410-440vh, count 0→51,000,000,000

settled (433-466vh):
  - Card 2: scroll 415-435vh, reveal
  - Card 3: scroll 430-450vh, reveal
  - Numbers all visible

exit (466-500vh):
  - Cards stable
  - Prepare transition to Scene 5
```

**Done Criteria**:
- [ ] Numbers count up based on scroll (not time)
- [ ] Cards have glassmorphism effect
- [ ] Scale feels overwhelming

---

## SCENE 5: A Solução (500-600vh)

**Purpose**: Define "Auditoria como Código" by negation and affirmation.

**Trigger**: scrollY >= 500vh && scrollY < 600vh

**Required Assets**: None (CSS only)

**Required Components**:
- Split screen: Negações (left) vs Afirmações (right)
- ✗ marks in #C53030 (Red)
- ✓ marks in #0C326F (Blue)
- Main title: "Auditoria como Código"
- Final text: "A IA interpreta. O Código audita."

**State Transitions**:
```
entrance (500-533vh):
  - Negations: staggered reveal with ✗ marks

settled (533-566vh):
  - Affirmations: staggered reveal with ✓ marks
  - Comparison table slides in from sides

exit (566-600vh):
  - Main title scales up
  - Final text: "A IA interpreta. O Código audita."
```

**Done Criteria**:
- [ ] Split layout clear
- [ ] Staggered animation on scroll
- [ ] Final text prominent

---

## SCENE 6: Arquitetura (600-700vh)

**Purpose**: Show three-layer system—IA proposes, Protocol approves.

**Trigger**: scrollY >= 600vh && scrollY < 700vh

**Required Assets**: None (CSS/SVG only)

**Required Components**:
- Layer 1 (IA): Cyan #4FC3F7, cloud shape
- Layer 2 (Validação): Blue #0C326F, geometric
- Layer 3 (Decisão): Gold #D4AF37, solid
- SVG arrows connecting layers

**State Transitions**:
```
entrance (600-633vh):
  - Layer 1: height 0→auto, opacity 0→1
  - Arrow 1: stroke-dash draw

settled (633-666vh):
  - Layer 2: reveal
  - Arrow 2: stroke-dash draw
  - Layer 3: reveal

exit (666-700vh):
  - Final text: "A IA sugere. O Protocolo decide."
```

**Done Criteria**:
- [ ] Three layers clearly differentiated by color/shape
- [ ] Arrows animate between layers
- [ ] Hierarchy visually clear

---

## SCENE 7: Demonstração (700-800vh)

**Purpose**: Show system working—document → processing → output.

**Trigger**: scrollY >= 700vh && scrollY < 800vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| doc-icons | SVG Set | assets/scene7/icons.svg | 15KB |

**Required Components**:
- Left: Chaotic documents (red/orange)
- Center: Processing box with cyan glow pulse
- Right: Organized folders (green, checkmarks)
- Time display: "3.2 segundos"

**State Transitions**:
```
entrance (700-733vh):
  - Documents: chaotic, red
  - Processor: minimal

settled (733-766vh):
  - Documents flow toward processor (x-animation)
  - Processor: glow pulse active
  - Output: folders appear (green)

exit (766-800vh):
  - Time display appears
  - Complete flow demonstrated
```

**Done Criteria**:
- [ ] Flow direction left→center→right clear
- [ ] Processor has pulsing glow
- [ ] Output shows organization/validation

---

## SCENE 8: Conclusão Intermediária (800-900vh)

**Purpose**: Bridge from problem/solution to technical depth.

**Trigger**: scrollY >= 800vh && scrollY < 900vh

**Required Assets**: None (CSS opacity only)

**Required Components**:
- Ghost images from Scenes 1, 2, 3, 6 at 20-40% opacity
- Main text: "A IA sugere. O Protocolo decide."
- Prepare for Scene 9 transition

**State Transitions**:
```
entrance (800-833vh):
  - Ghosts: staggered opacity 0→0.3

settled (833-866vh):
  - Main text: opacity 0→1, y-offset 30px→0

exit (866-900vh):
  - Text color: line 1 blue, line 2 gold
```

**Done Criteria**:
- [ ] Ghost images create depth/memory
- [ ] Text synthesis clear
- [ ] Smooth transition to technical section

---

## SCENE 9: MCP (900-1000vh)

**Purpose**: Security architecture—AI inside database, Read-Only.

**Trigger**: scrollY >= 900vh && scrollY < 1000vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| database | SVG | assets/scene9/db.svg | 10KB |
| lock | SVG | assets/scene9/lock.svg | 5KB |

**Required Components**:
- Database cylinder (PostgreSQL style)
- AI element (cyan glow) descending into database
- Lock icons (shield, red #C53030)
- Comparison: old model (data out) vs new model (AI in)

**State Transitions**:
```
entrance (900-933vh):
  - Old model shown (ghosted at 30%)

settled (933-966vh):
  - AI descends into database position
  - Locks: staggered opacity 0→1

exit (966-1000vh):
  - Connection lines draw
  - Text: "Read-Only. Sem exceções."
```

**Done Criteria**:
- [ ] AI position clearly inside (not outside) database
- [ ] Lock icons prominent
- [ ] Read-only message clear

---

## SCENE 10: 6 Abordagens (1000-1100vh)

**Purpose**: Show breadth—AI not just for text generation.

**Trigger**: scrollY >= 1000vh && scrollY < 1100vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| icons | SVG Set | assets/scene10/icons.svg | 30KB |

**Required Components**:
- 3x2 grid of glassmorphism cards
- Icons: Camera (Vision), Code (SQL), Graph (Stats), DB (DDL), Docs (Reports), Shield (Validation)

**State Transitions**:
```
entrance (1000-1033vh):
  - Grid container: opacity 0→1

settled (1033-1066vh):
  - Cards 1-6: staggered scale 0.8→1, opacity 0→1

exit (1066-1100vh):
  - All cards stable
```

**Done Criteria**:
- [ ] 6 cards in 3x2 grid
- [ ] Staggered reveal on scroll
- [ ] Each card has distinct icon

---

## SCENE 11: Zero Kelvin (1100-1200vh)

**Purpose**: Prove numbers cannot vary—mathematical certainty.

**Trigger**: scrollY >= 1100vh && scrollY < 1200vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| crystal | SVG | assets/scene11/crystal.svg | 40KB |

**Required Components**:
- Three cards all showing: "3,175,345" (monospace)
- Ice/crystal visual effect (#4FC3F7, #0C326F)
- Lock icons on each card
- Thermometer at "absolute zero"

**State Transitions**:
```
entrance (1100-1133vh):
  - Card 1: opacity 0→1
  - Card 2: opacity 0→1 (same number)
  - Card 3: opacity 0→1 (same number)

settled (1133-1166vh):
  - Ice effect: filter blur→sharp, glow
  - Locks: staggered reveal

exit (1166-1200vh):
  - Invariance demonstrated
```

**Done Criteria**:
- [ ] All three numbers identical
- [ ] Ice/crystal visual theme
- [ ] Locks on all cards

---

## SCENE 12: Idempotência (1200-1300vh)

**Purpose**: Prove determinism—same seed = same result.

**Trigger**: scrollY >= 1200vh && scrollY < 1300vh

**Required Assets**: None (CSS only)

**Required Components**:
- Terminal window: dark #1A1A2E, cyan text
- Output: "Result: Idempotent. 16,501 Records"
- 5 stacked rectangles (anti-hallucination layers)
- Equation: "Same Seed + Same Population = Same Records"

**State Transitions**:
```
entrance (1200-1233vh):
  - Terminal: empty, dark

settled (1233-1266vh):
  - Terminal text: type character-by-character (scroll-driven)
  - Layers: slide in and stack
  - Glow: terminal glows with success

exit (1266-1300vh):
  - Equation: opacity 0→1
```

**Done Criteria**:
- [ ] Terminal has authentic dark-mode aesthetic
- [ ] Text appears progressively with scroll
- [ ] 5 layers visually stacked

---

## SCENE 13: Demo ao Vivo (1300-1400vh)

**Purpose**: Show working system—real pipeline visualization.

**Trigger**: scrollY >= 1300vh && scrollY < 1400vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| pipeline | SVG | assets/scene13/pipeline.svg | 50KB |

**Required Components**:
- Isometric pipeline layout
- Left: Chaotic folders (red)
- Center: Machine with cyan glow pulse
- Right: Organized folders (green, checked)

**State Transitions**:
```
entrance (1300-1333vh):
  - Left: chaotic
  - Center: inactive
  - Right: empty

settled (1333-1366vh):
  - Documents flow toward center
  - Machine: active pulse
  - Output: organized folders appear

exit (1366-1400vh):
  - Complete flow demonstrated
```

**Done Criteria**:
- [ ] Pipeline flow direction clear
- [ ] Machine glow pulses
- [ ] Output shows validation

---

## SCENE 14: Papéis de Trabalho (1400-1500vh)

**Purpose**: Show tangible output—YAML → 12 workpapers → LaTeX.

**Trigger**: scrollY >= 1400vh && scrollY < 1500vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| tree | SVG | assets/scene14/tree.svg | 30KB |

**Required Components**:
- YAML icon (green, code)
- Process tree with 12 branches
- LaTeX document (gold, academic)
- Flow arrows

**State Transitions**:
```
entrance (1400-1433vh):
  - YAML: isolated left

settled (1433-1466vh):
  - Tree: branches extend progressively
  - LaTeX: receives inputs

exit (1466-1500vh):
  - Arrows: stroke-dash draw
  - Text: "Audit as Code"
```

**Done Criteria**:
- [ ] Tree has 12 visible branches
- [ ] Flow YAML → Tree → LaTeX clear
- [ ] LaTeX document prominent

---

## SCENE 15: Os 4 Achados (1500-1600vh)

**Purpose**: Deliver impact—four shocking statistics.

**Trigger**: scrollY >= 1500vh && scrollY < 1600vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| warning-icons | SVG Set | assets/scene15/icons.svg | 20KB |

**Required Components**:
- 2x2 grid of impact cards
- Card 1: 27.1% Inadequado (Orange #ED8936)
- Card 2: 45.92% Erro Geoespacial (Orange #ED8936)
- Card 3: 90.62% Inválido (Red #C53030, FALECIDOS)
- Card 4: 94.1% Falha Absoluta (Red #C53030)

**State Transitions**:
```
entrance (1500-1533vh):
  - Card 1: number counts 0→27.1%
  - Card 2: number counts 0→45.92%

settled (1533-1566vh):
  - Card 3: number counts 0→90.62% (emphasis: shocking)
  - Card 4: number counts 0→94.1%

exit (1566-1600vh):
  - Impact established
```

**Critical**: Number count-up must be scroll-driven, not time-based.

**Done Criteria**:
- [ ] All four numbers count up with scroll
- [ ] 90.62% and 94.1% in red (critical)
- [ ] Grid layout stable

---

## SCENE 16: Novo Auditor (1600-1700vh)

**Purpose**: Human evolution—not replaced, but elevated.

**Trigger**: scrollY >= 1600vh && scrollY < 1700vh

**Required Assets**: None (CSS/SVG)

**Required Components**:
- Left: New roles list
  - YAML Coder
  - Intérprete
  - Orquestrador
  - Engenheiro
- Right: Bar chart (10 months vs 2 months)
- Tooltip: "Reinvested in Analytical Depth"

**State Transitions**:
```
entrance (1600-1633vh):
  - Roles: staggered list reveal

settled (1633-1666vh):
  - Chart bars: height animation 0→full
  - 2-month bar highlights

exit (1666-1700vh):
  - Tooltip: opacity 0→1
```

**Done Criteria**:
- [ ] Four roles clearly listed
- [ ] Bar chart shows dramatic reduction
- [ ] Tooltip visible

---

## SCENE 17: O Legado (1700-1800vh)

**Purpose**: Institutional impact—R$ 51B, 210+ memos, roadmap.

**Trigger**: scrollY >= 1700vh && scrollY < 1800vh

**Required Assets**:
| ID | Type | File | Size |
|----|------|------|------|
| dashboard | SVG | assets/scene17/dashboard.svg | 80KB |

**Required Components**:
- Three columns:
  - Left: Quantitativos (R$ 51B, 210+ memos, 9.7/10)
  - Center: Feats (MCP, 33 skills, 2 agents, 3.7M records, 12.8M CPFs)
  - Right: Roadmap (YAML Template, RTCU publication, Orchestrator)

**State Transitions**:
```
entrance (1700-1733vh):
  - Left column: staggered reveals

settled (1733-1766vh):
  - Center column: staggered reveals
  - Right column: roadmap items

exit (1766-1800vh):
  - R$ 51B and 9.7/10 pulse briefly
```

**Done Criteria**:
- [ ] Three columns balanced
- [ ] Key numbers prominent
- [ ] Roadmap items listed

---

## SCENE 18: Mic Drop (1800-1900vh)

**Purpose**: Eternal philosophical conclusion—no animation, maximum impact.

**Trigger**: scrollY >= 1800vh && scrollY < 1900vh

**Required Assets**: None (CSS only)

**Required Components**:
- Background: Solid #0D0D1A (dark space) OR #FFFFFF (white)
- Line 1: "A IA decide o que faz sentido." — #0C326F (Blue)
- Line 2: "A nossa engenharia decide o que é permitido." — #D4AF37 (Gold)
- Font: Minimum 48px, Heavy/Bold weight
- Subtitle (optional): "Audit-As-Code | TCU | 2026"

**State Transitions**:
```
entrance (1800-1830vh):
  - Background transition complete

settled (1830-1860vh):
  - Line 1: opacity 0→1, y-offset 50px→0
  - Line 2: opacity 0→1, y-offset 50px→0 (20vh delay)

exit (1860-1900vh):
  - NO ANIMATION. Static hold.
```

**Critical Constraint**: No animation in 1860-1900vh. Text must be completely static for reading.

**Done Criteria**:
- [ ] Background solid (no gradients)
- [ ] Both lines fully visible
- [ ] No animation in final 40vh
- [ ] Typography monumental

---

# Global Rules

## Coordinate System
- **Units**: vh/vw only for layout. No pixels for positioning.
- **Z-index layers**:
  - 0: Background
  - 10: Scene content
  - 20: Transition overlays
  - 100: Accessibility elements

## Color Palette (Immutable)
| Name | Hex | Usage |
|------|-----|-------|
| TCU Blue | #0C326F | Primary brand, Layer 2, Line 1 Scene 18 |
| TCU Gold | #D4AF37 | Emphasis, Layer 3, Line 2 Scene 18, Cuiabá marker |
| Cyan | #4FC3F7 | IA elements, glows, accents |
| Red Alert | #C53030 | Critical findings, locks, ✗ marks |
| Orange | #ED8936 | Warning findings |
| Dark Slate | #1A1A2E | Space backgrounds, terminals |
| White | #FFFFFF | Scene 1, 4, 5 backgrounds |
| Graphite | #0D0D1A | Scene 18 background option |

## Typography
| Element | Font | Size | Weight |
|---------|------|------|--------|
| Main titles | SF Pro Display | 48-64px | Bold/Heavy |
| Body text | SF Pro Text | 18-24px | Regular |
| Numbers | SF Pro Display | 120px | Heavy |
| Terminal | SF Mono / JetBrains Mono | 16px | Regular |
| Scene 18 | SF Pro Display | 48px+ | Heavy |

**Fallback chain**: SF Pro → Inter → Helvetica Neue → Arial

## Animation Constraints
1. **Only animate**: `transform`, `opacity`
2. **Never animate**: `width`, `height`, `top`, `left`, `margin`, `padding`
3. **will-change**: Apply 500ms before animation, remove after
4. **Reduced motion**: All transforms → instant opacity changes

## Scroll Behavior
- **Container**: Native browser scroll (no hijacking)
- **Listeners**: `{ passive: true }` only
- **Total height**: 2000vh (1900vh + 100vh buffer)
- **Scene height**: 100vh each
- **Transition**: 50vh cross-fade between scenes

## Performance Budget
| Metric | Target | Maximum |
|--------|--------|---------|
| Frame time | 16ms | 33ms |
| JS heap | 50MB | 100MB |
| DOM nodes | 3000 | 5000 |
| Image memory | 30MB | 50MB |

## Accessibility Requirements
- Keyboard: Arrow keys navigate between scenes
- Screen reader: Each scene is `<section aria-labelledby>`
- Contrast: WCAG AA minimum (4.5:1)
- Reduced motion: Respects `prefers-reduced-motion`
- No JS: Page works as long scrollable document

---

# Failure Prevention Guide

## 1. Layout Thrashing
**Symptom**: Frame rate drops during scroll.
**Prevention**:
- Read layout values (offsetHeight, etc.) once at initialization
- Write style changes in batches via CSS transforms
- Use `transform` instead of `top/left`

## 2. Rapid Scroll Skipping
**Symptom**: User scrolls fast, misses content.
**Prevention**:
- Scroll-snap at scene boundaries (not during scenes)
- Pin transitions for 50vh minimum
- Critical content never in first/last 10% of scene

## 3. Scene Element Bleed
**Symptom**: Elements from one scene visible in another.
**Prevention**:
- Unmount scene when >2 scenes away
- Opacity 0 on exit-complete (not display:none for transition)
- Z-index isolation per scene

## 4. Number Animation Jank
**Symptom**: Count-up animations stutter.
**Prevention**:
- Use `useRef` to update textContent directly
- No React state updates per frame
- Pre-calculate number string format

## 5. Reduced Motion Violation
**Symptom**: Motion-sensitive users experience discomfort.
**Prevention**:
- Media query check before any transform
- Fallback content ready (static versions)
- Test with macOS "Reduce motion" enabled

## 6. Mobile Viewport Collapse
**Symptom**: Layout breaks on narrow screens.
**Prevention**:
- Minimum width: 320px
- Single column layout below 768px
- Font sizes minimum 16px

## 7. Asset Loading Flash
**Symptom**: Images appear after scene visible.
**Prevention**:
- Load Scene 0 assets immediately (blocking)
- Prefetch Scenes 1-5 after Scene 0 settles
- Lazy load Scenes 6-18 when Scene 4 active
- Skeleton screens match final layout dimensions

## 8. Scene 18 Animation Creep
**Symptom**: Developer adds "polish" animation to final scene.
**Prevention**:
- Scene 18 specification: NO ANIMATION
- Code review check: any transform/opacity in 1860-1900vh is rejected
- Static final state is intentional design

---

# Definition of Done

## Functional Completion
- [ ] All 19 scenes implemented and reachable via scroll
- [ ] Scroll position → visual state mapping deterministic
- [ ] No console errors in production build
- [ ] No-JS fallback displays all content

## Performance Completion
- [ ] 60fps maintained during normal scroll
- [ ] 30fps minimum on low-end hardware
- [ ] Memory usage <100MB
- [ ] First contentful paint <2s

## Accessibility Completion
- [ ] Keyboard navigation works (arrow keys)
- [ ] Screen reader announces scene changes
- [ ] Color contrast meets WCAG AA everywhere
- [ ] Reduced motion mode tested and working

## Visual Completion
- [ ] All assets loaded and displaying correctly
- [ ] Colors match TCU palette exactly
- [ ] Typography hierarchy clear
- [ ] Scene transitions smooth (no glitches)

## Content Completion
- [ ] All text content matches speaker script
- [ ] Numbers animate correctly (scroll-driven)
- [ ] Scene 18 has no animation (static)
- [ ] Ghost images in Scene 8 at correct opacity

## Browser Completion
- [ ] Chrome (latest): Pass
- [ ] Firefox (latest): Pass
- [ ] Safari (latest): Pass
- [ ] Edge (latest): Pass

## Final Sign-Off
- [ ] Technical lead approval
- [ ] Design lead approval
- [ ] Accessibility review passed
- [ ] Performance budget met
- [ ] Deployed to production hosting

---

# Document Reconciliation Notes

## Resolved Conflicts

### Scene Numbering
- **Conflict**: `presentation_architecture.md` uses 9 scenes (0-8), `narrative.md` uses 19 scenes (0-18)
- **Resolution**: Use 19 scenes (0-18). `presentation_architecture.md` Acts map to scene ranges: Act 1 = Scenes 0-3, Act 2 = Scene 4, Act 3 = Scenes 5-9, Act 4 = Scenes 10-17, Act 5 = Scene 18.

### Scroll Height
- **Conflict**: Architecture doc says 1800vh, Narrative says 1900vh + 100vh buffer
- **Resolution**: 2000vh total (1900vh content + 100vh buffer). Scene 18 ends at 1900vh, final 100vh is exit buffer.

### Scene 8 Content
- **Conflict**: SLIDE_8_MASTER is "Conclusão Intermediária" with ghosts; Architecture Scene 8 is "Dashboard"
- **Resolution**: Scene 8 is "Conclusão Intermediária" (ghosts, bridge to technical). Scene 17 is "O Legado" (dashboard). This aligns with narrative flow.

### Scene 18 Content
- **Conflict**: SLIDE_18_MASTER has specific quote; Architecture Scene 9 (Mic Drop) has generic text
- **Resolution**: Scene 18 quote is authoritative from SLIDE_18_MASTER: "A IA decide o que faz sentido. A nossa engenharia decide o que é permitido."

### Key Phrase Placement
- **Conflict**: "Automação sem guardrails" appears in SLIDE_8 and as alternative in SLIDE_18
- **Resolution**: Primary phrase in Scene 18. Scene 8 uses bridge text "A IA sugere. O Protocolo decide."

## Implicit Assumptions Made Explicit

1. **Font availability**: SF Pro may require license check. Fallback chain (Inter → Helvetica Neue → Arial) guaranteed available.

2. **Globe implementation**: Scene 0 globe can be CSS-only (radial gradients) or Three.js. Blueprint specifies SVG for performance predictability.

3. **Terminal aesthetic**: Scene 12 terminal must look authentic. Use VS Code dark theme colors (#1A1A2E background, #4FC3F7 text).

4. **Ghost image opacity**: Scene 8 ghosts at 20-40% opacity. Exact values: Scene 1 ghost 20%, Scene 2 ghost 30%, Scene 3 ghost 40%, Scene 6 ghost 25%.

5. **Number format**: Brazilian Portuguese. "R$ 51 Bilhões" not "$51 Billion". Decimal comma: 27,1% not 27.1%.

---

END OF BUILD BLUEPRINT
