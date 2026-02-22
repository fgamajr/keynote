 # Experience Model

  ## Narrative Progression

  The experience consists of 19 scenes (mapped from slides 0-18). Each scene occupies a defined scroll distance of 100vh. The total scrol
  l track length is 1900vh plus 100vh buffer for entry/exit.

  Scene transitions occur at scroll position thresholds: 0, 100vh, 200vh, ... 1800vh. Each threshold triggers a macro-transition where th
  e previous scene commits to its final state and the next scene begins from a defined initial state.

  ## Scroll-as-Timeline Mechanics

  Scroll position is the single source of truth. No animation durations exist in absolute time. All motion is computed as a function of s
  croll position within scene boundaries.

  The scroll container is pinned during scene transitions to ensure completion of state changes before releasing to next scene. Pin durat
  ion: 50vh per transition, creating 50vh "transition corridors" between 100vh "scene plates".

  ## Scene Types

  Three architectural scene types exist:

  **Type A: Metaphorical (Scenes 0-3)**
  - Visual abstraction dominates
  - Text minimal, declarative
  - Camera movement (zoom, pan) tied to scroll

  **Type B: Evidential (Scenes 4-8, 13-15)**
  - Data visualization and proof
  - Number animations scroll-driven
  - Layout shifts expose information progressively

  **Type C: Technical (Scenes 9-12, 16-17)**
  - Architecture diagrams and process flows
  - Static structure revealed through scroll
  - No arbitrary motion, only disclosure

  **Type D: Cinematic (Scene 18)**
  - Minimal content, maximum negative space
  - No scroll-linked animation
  - Static terminus state

  ## Cognitive Load Distribution

  Metaphor density decreases linearly through the experience:
  - Scenes 0-3: High abstraction (globe, paths, physics)
  - Scenes 4-8: Concrete problem/solution
  - Scenes 9-17: Technical validation
  - Scene 18: Philosophical conclusion

  No scene contains more than one primary insight. Secondary insights are visually subordinate (opacity < 0.6).

  ---

  # Rendering Architecture

  ## Coordinate System

  All positioning uses viewport-relative units (vh, vw) with percentage fallbacks. No pixel values for layout. Pixel values permitted onl
  y for:
  - Border widths (1px, 2px)
  - Text sizes (rem units with px fallback)
  - SVG stroke widths

  Z-index layering:
  - Layer 0: Background elements (z-index: 0)
  - Layer 1: Scene content (z-index: 10)
  - Layer 2: Foreground/transition overlays (z-index: 20)
  - Layer 3: Accessibility skip links (z-index: 100)

  ## State Management

  Each scene maintains three scroll-defined states:
  - `entrance`: scroll 0% to 33% of scene
  - `settled`: scroll 33% to 66% of scene
  - `exit`: scroll 66% to 100% of scene

  State transitions are computed via interpolation functions defined per property. No discrete state changes at boundaries—continuous int
  erpolation only.

  State calculation formula:

  progress = (currentScroll - sceneStart) / sceneHeight phase = floor(progress * 3) / 3  // Creates 0, 0.33, 0.66 segments localProgress
  = (progress - phase) / 0.33  // 0-1 within segment


  ## Asset Loading Strategy

  Assets load in three tiers:
  - **Critical**: Scene 0 assets load immediately (blocking)
  - **Next**: Scenes 1-5 assets load after Scene 0 settles
  - **Deferred**: Scenes 6-18 assets load when Scene 4 becomes active

  No lazy loading during scroll. All assets for active and next two scenes must be resident in memory before scroll reaches them.

  ## Transition Architecture

  Scene transitions use opacity cross-fade combined with transform handoff. Duration: 50vh scroll distance (approximately 500ms at normal
  scroll speed).

  Handoff rules:
  - Outgoing scene opacity: 1 → 0.3 (linear, 0-50% of transition)
  - Outgoing scene transforms: continue to completion state
  - Incoming scene opacity: 0 → 1 (ease-in, 20-100% of transition)
  - Incoming scene start state: defined, not computed

  No shared elements between scenes. Each scene is self-contained to prevent state corruption during rapid scroll.

  ---

  # Scene Specifications

  ## Scene 0: Abertura (0-100vh)

  **Initial State (0vh):**
  - Background: Deep space gradient (#1A1A2E)
  - Globe: Centered, 30% viewport size, 0% rotation
  - Cuiabá marker: Hidden (opacity 0, scale 0)

  **Settled State (33-66vh):**
  - Globe: 50% viewport size, rotated to show South America
  - Cuiabá marker: Visible (opacity 1, scale 1), pulsing glow
  - Text: "Fernando Gama" opacity 1, y-position 60vh

  **Exit State (100vh):**
  - Globe: Fading to 20% opacity
  - Marker: Scale 2x, fading
  - Background: Transitioning to white

  **Scroll-Driven Properties:**
  - Globe rotation: 0° to 45° (linear with scroll 0-50%)
  - Globe scale: 0.3 to 0.5 (ease-out, 0-66%)
  - Marker appearance: scroll 40-60%, opacity 0→1, scale 0→1
  - Background color: scroll 80-100%, blend from dark to white

  **Assets:**
  - 1: Globo terrestre wireframe (SVG)
  - 2: Marcador de Cuiabá (SVG com glow)
  - 3: Gradient background (CSS)

  ---

  ## Scene 1: Dois Pontos (100-200vh)

  **Initial State (100vh):**
  - Background: White (#FFFFFF)
  - Two dots: Hidden (opacity 0)
  - Line: Hidden (stroke-dashoffset: 100%)

  **Settled State (133-166vh):**
  - Two dots: Visible, positioned 25% and 75% horizontally, centered vertically
  - Line: Fully drawn connecting dots
  - Text: "O caminho mais curto entre dois pontos" visible

  **Exit State (200vh):**
  - All elements: Holding position for transition to Scene 2

  **Scroll-Driven Properties:**
  - Dot 1: scroll 100-110%, opacity 0→1
  - Dot 2: scroll 110-120%, opacity 0→1
  - Line draw: scroll 120-140%, stroke-dashoffset 100%→0%
  - Text: scroll 140-150%, opacity 0→1, y-offset 20px→0

  **Assets:**
  - 1: Two dot elements (CSS/SVG)
  - 2: Line element (SVG with dash animation capability)

  **Critical Constraint:** Dot positions must exactly match Scene 2 dot positions for morph transition.

  ---

  ## Scene 2: A Estrada (200-300vh)

  **Initial State (200vh):**
  - Dots: Same position as Scene 1 exit
  - Line: Same as Scene 1
  - Terrain: Hidden below viewport (y: 100%)
  - Winding road: Hidden

  **Settled State (233-266vh):**
  - Terrain: Visible, filling lower 60% of viewport
  - Winding road: Fully visible, highlighted
  - Straight line: Faded to 40% opacity, dashed style
  - Text: Changed to "Exceto no mundo real"

  **Exit State (300vh):**
  - Road: Fully established as primary path
  - Text holding for next transition

  **Scroll-Driven Properties:**
  - Terrain rise: scroll 200-230%, y: 100%→0%
  - Road reveal: scroll 220-260%, opacity 0→1, stroke-dashoffset animation
  - Line transition: scroll 230-250%, opacity 1→0.4, style solid→dashed
  - Text crossfade: scroll 200-210%, opacity swap

  **Assets:**
  - 1: Terrain topography (SVG or image)
  - 2: Winding road path (SVG)
  - 3: Modified straight line (same element, style change)

  ---

  ## Scene 3: O Planeta (300-400vh)

  **Initial State (300vh):**
  - Background: Dark slate (#1A1A2E)
  - Globe wireframe: Centered, small
  - Brazil/Amsterdam markers: Hidden

  **Settled State (333-366vh):**
  - Globe: Rotated, markers visible
  - Red line: Dashed, through center
  - Blue arc: Curved around surface
  - Text: "Restrições tornam soluções possíveis"

  **Exit State (400vh):**
  - Red line: Faded (30% opacity)
  - Blue arc: Highlighted (100% opacity)
  - Globe: Stable for next transition

  **Scroll-Driven Properties:**
  - Globe fade-in: scroll 300-320%, opacity 0→1
  - Markers: scroll 320-340%, opacity 0→1
  - Red line draw: scroll 340-360%, stroke-dash animation
  - Blue arc draw: scroll 360-380%, stroke-dash animation
  - Line emphasis swap: scroll 380-400%, red fade, blue highlight

  **Assets:**
  - 1: Wireframe globe (3D rendered or SVG)
  - 2: Red dashed line (SVG)
  - 3: Blue glowing arc (SVG)

  ---

  ## Scene 4: O Problema (400-500vh)

  **Initial State (400vh):**
  - Background: White
  - Cards: Hidden, positioned off-screen
  - Numbers: 0 displayed

  **Settled State (433-466vh):**
  - Card 1: "R$ 51 Bilhões" visible, scaled to 100%
  - Card 2: "3.5 Milhões" visible
  - Card 3: "10.7 Milhões" visible
  - Rodapé: "63.588 registros na amostra" visible

  **Exit State (500vh):**
  - All cards stable
  - Transition to text-based scene preparing

  **Scroll-Driven Properties:**
  - Card 1: scroll 400-420%, opacity 0→1, scale 0.8→1, y: 50px→0
  - Card 2: scroll 415-435%, opacity 0→1, scale 0.8→1, y: 50px→0
  - Card 3: scroll 430-450%, opacity 0→1, scale 0.8→1, y: 50px→0
  - Number count-up: scroll 410-440%, animated number increment (JS-driven from scroll position)
  - Rodapé: scroll 460-480%, opacity 0→1

  **Assets:**
  - 1-3: Glassmorphism cards (CSS)
  - Icons: Money, family, documents (SVG)

  ---

  ## Scene 5: A Solução (500-600vh)

  **Initial State (500vh):**
  - Text "NÃO": Small, positioned left
  - Checkmarks: Hidden
  - Comparison layout: Not visible

  **Settled State (533-566vh):**
  - Negations (✗): Listed and struck through
  - Affirmations (✓): Listed prominently
  - "Auditoria como Código": Large, centered
  - NÃO É / É comparison: Both columns visible

  **Exit State (600vh):**
  - Final text: "A IA interpreta. O Código audita."
  - All previous elements faded

  **Scroll-Driven Properties:**
  - Negations: scroll 500-530%, staggered reveal with ✗ marks
  - Affirmations: scroll 530-560%, staggered reveal with ✓ marks
  - Main title: scroll 560-580%, scale up, center
  - Comparison table: scroll 540-570%, slide in from sides
  - Final text: scroll 580-600%, opacity 0→1

  ---

  ## Scene 6: Arquitetura (600-700vh)

  **Initial State (600vh):**
  - Three layers: Collapsed, hidden
  - Arrows: Not drawn

  **Settled State (633-666vh):**
  - Layer 1 (IA): Expanded, cyan glow
  - Layer 2 (Validação): Expanded, blue
  - Layer 3 (Decisão): Expanded, gold
  - Arrows: Fully drawn connecting layers
  - Labels: All visible

  **Exit State (700vh):**
  - Layers stable
  - Final text: "A IA sugere. O Protocolo decide."

  **Scroll-Driven Properties:**
  - Layer 1: scroll 600-620%, height 0→auto, opacity 0→1
  - Arrow 1: scroll 620-630%, stroke-dash draw
  - Layer 2: scroll 630-650%, height 0→auto, opacity 0→1
  - Arrow 2: scroll 650-660%, stroke-dash draw
  - Layer 3: scroll 660-680%, height 0→auto, opacity 0→1
  - Final text: scroll 680-700%, opacity 0→1

  **Assets:**
  - Layer cards: CSS with border colors (cyan, blue, gold)
  - Arrows: SVG with dash animation

  ---

  ## Scene 7: Demonstração (700-800vh)

  **Initial State (700vh):**
  - Document input: Left, chaotic appearance
  - Processing box: Center, minimal
  - Output: Right, hidden

  **Settled State (733-766vh):**
  - Document: Flowing into processor
  - Processing box: Active (glow pulse)
  - Output: Organized documents visible
  - Time indicator: "3.2 segundos" displayed

  **Exit State (800vh):**
  - Complete flow demonstrated
  - All elements stable

  **Scroll-Driven Properties:**
  - Document flow: scroll 700-750%, x-position left→center, opacity 1→0.3 (entering machine)
  - Processor activation: scroll 720-780%, glow intensity pulse
  - Output reveal: scroll 760-800%, opacity 0→1, x-position center→right
  - Time display: scroll 780-800%, opacity 0→1, scale 0.9→1

  ---

  ## Scene 8: Conclusão (800-900vh)

  **Initial State (800vh):**
  - Ghosts of previous scenes: Faint (20% opacity)
  - Text: Hidden

  **Settled State (833-866vh):**
  - Ghost images: Layered (Slide 1, 2, 3, 6)
  - Main text: "A IA sugere. O Protocolo decide."
  - Subtext: Visible

  **Exit State (900vh):**
  - Final text prominent
  - Ready for technical section

  **Scroll-Driven Properties:**
  - Ghost reveals: scroll 800-840%, staggered opacity 0→0.3
  - Main text: scroll 840-870%, opacity 0→1, y-offset 30px→0
  - Color emphasis: scroll 860-900%, first line blue, second line gold

  ---

  ## Scene 9: MCP (900-1000vh)

  **Initial State (900vh):**
  - Database: Bottom center
  - AI: Outside, above
  - Insecure model: Not shown

  **Settled State (933-966vh):**
  - Comparison: Old model (data out) vs new model (AI in)
  - AI: Inside database perimeter
  - Lock icons: Visible
  - Read-only indicators: Visible

  **Exit State (1000vh):**
  - Secure architecture established

  **Scroll-Driven Properties:**
  - Old model (fade): scroll 900-920%, opacity 1→0.3 (ghosted)
  - New model: scroll 920-960%, AI descends into database position
  - Lock reveal: scroll 940-980%, staggered opacity 0→1
  - Connection lines: scroll 950-990%, draw animation

  ---

  ## Scene 10: 6 Abordagens (1000-1100vh)

  **Initial State (1000vh):**
  - Grid: Hidden
  - Cards: Collapsed

  **Settled State (1033-1066vh):**
  - 6 cards: Full grid visible (3x2)
  - Icons: All displayed
  - Text: All labels visible

  **Exit State (1100vh):**
  - Cards stable
  - Ready for next technical scene

  **Scroll-Driven Properties:**
  - Grid container: scroll 1000-1020%, opacity 0→1
  - Card 1: scroll 1020-1030%, scale 0.8→1, opacity 0→1
  - Card 2: scroll 1025-1035%, scale 0.8→1, opacity 0→1
  - (Continue staggered pattern for cards 3-6)
  - Highlight on mention: Each card glows briefly when narrator mentions it

  ---

  ## Scene 11: Zero Kelvin (1100-1200vh)

  **Initial State (1100vh):**
  - Number: Single instance
  - Crystal/ice effect: Not applied
  - Flowchart: Hidden

  **Settled State (1133-1166vh):**
  - Three cards: All showing "3,175,345"
  - Ice/crystal effect: Applied to numbers
  - Lock icons: On each card
  - Thermometer: Optional visual

  **Exit State (1200vh):**
  - Invariance demonstrated

  **Scroll-Driven Properties:**
  - Card 1: scroll 1100-1120%, opacity 0→1
  - Card 2: scroll 1110-1130%, opacity 0→1 (number identical)
  - Card 3: scroll 1120-1140%, opacity 0→1 (number identical)
  - Ice effect: scroll 1140-1180%, filter: blur→sharp, glow effect
  - Lock reveals: scroll 1160-1200%, staggered

  ---

  ## Scene 12: Idempotência (1200-1300vh)

  **Initial State (1200vh):**
  - Terminal: Dark, empty
  - Layers: Not stacked

  **Settled State (1233-1266vh):**
  - Terminal: Showing "Result: Idempotent. 16,501 Records"
  - 5 layers: Stacked on right
  - Equation: "Same Seed + Same Population = Same Records"

  **Exit State (1300vh):**
  - Determinism proven visually

  **Scroll-Driven Properties:**
  - Terminal type: scroll 1200-1240%, text appears character-by-character (scroll-driven)
  - Glow: scroll 1240-1280%, terminal glows with success
  - Layers stack: scroll 1220-1280%, cards slide in and stack
  - Equation: scroll 1260-1300%, opacity 0→1

  ---

  ## Scene 13: Demo ao Vivo (1300-1400vh)

  **Initial State (1300vh):**
  - Left: Chaotic folders (red)
  - Center: Machine (gray, inactive)
  - Right: Empty

  **Settled State (1333-1366vh):**
  - Left: Documents flowing toward center
  - Center: Machine active (cyan glow)
  - Right: Organized folders (green, checked)
  - Video frame: Optional corner display

  **Exit State (1400vh):**
  - Complete pipeline demonstrated

  **Scroll-Driven Properties:**
  - Document flow: scroll 1300-1350%, continuous flow animation tied to scroll
  - Machine pulse: scroll 1320-1380%, glow intensity cycles with scroll
  - Output accumulation: scroll 1360-1400%, folders appear progressively

  ---

  ## Scene 14: Papéis de Trabalho (1400-1500vh)

  **Initial State (1400vh):**
  - YAML: Left, isolated
  - Process tree: Not grown
  - LaTeX: Right, empty

  **Settled State (1433-1466vh):**
  - YAML: Connected to tree
  - Process tree: Fully grown with 12 branches
  - LaTeX: Receiving inputs
  - Flow arrows: All drawn

  **Exit State (1500vh):**
  - Complete workflow mapped

  **Scroll-Driven Properties:**
  - YAML reveal: scroll 1400-1420%, opacity 0→1
  - Tree growth: scroll 1420-1480%, branches extend progressively
  - LaTeX reveal: scroll 1460-1500%, opacity 0→1
  - Arrow draws: scroll 1440-1490%, stroke-dash animations

  ---

  ## Scene 15: Os 4 Achados (1500-1600vh)

  **Initial State (1500vh):**
  - Grid: Empty
  - Numbers: 0%

  **Settled State (1533-1566vh):**
  - 4 cards: 27.1%, 45.92%, 90.62%, 94.1%
  - Impact text: All visible
  - Colors: Red/orange for critical

  **Exit State (1600vh):**
  - Impact established

  **Scroll-Driven Properties:**
  - Card 1: scroll 1500-1525%, number counts 0→27.1%
  - Card 2: scroll 1515-1540%, number counts 0→45.92%
  - Card 3: scroll 1530-1555%, number counts 0→90.62% (emphasis: this is shocking)
  - Card 4: scroll 1545-1600%, number counts 0→94.1%

  **Critical:** Number count-up must be scroll-driven, not time-based.

  ---

  ## Scene 16: Novo Auditor (1600-1700vh)

  **Initial State (1600vh):**
  - Left: New roles list, hidden
  - Right: Chart not drawn
  - 10 months bar: Not visible

  **Settled State (1633-1666vh):**
  - Left: YAML Coder, Intérprete, Orquestrador, Engenheiro visible
  - Right: Bar chart comparing 10 months vs 2 months
  - Tooltip: "Reinvested in Analytical Depth" visible

  **Exit State (1700vh):**
  - Career evolution demonstrated

  **Scroll-Driven Properties:**
  - Role reveals: scroll 1600-1640%, staggered list items
  - Chart bars: scroll 1620-1680%, height animation 0→full
  - Comparison emphasis: scroll 1660-1700%, 2-month bar highlights
  - Tooltip: scroll 1680-1700%, opacity 0→1

  ---

  ## Scene 17: O Legado (1700-1800vh)

  **Initial State (1700vh):**
  - Three columns: Empty
  - Numbers: Not displayed

  **Settled State (1733-1766vh):**
  - Left: R$ 51B, 210+ memos, 9.7/10
  - Center: MCP, 33 skills, 2 agents, 3.7M records, 12.8M CPFs
  - Right: Roadmap items visible

  **Exit State (1800vh):**
  - Legacy established

  **Scroll-Driven Properties:**
  - Left column: scroll 1700-1740%, staggered card reveals
  - Center column: scroll 1720-1760%, staggered reveals
  - Right column: scroll 1740-1800%, roadmap items appear
  - Pulse on key numbers: R$ 51B and 9.7/10 get brief glow at 1760vh

  ---

  ## Scene 18: Mic Drop (1800-1900vh)

  **Initial State (1800vh):**
  - Background: Transitioning (dark or light)
  - Text: Hidden

  **Settled State (1833-1866vh):**
  - Background: Solid (dark space or white—consistent choice)
  - Main text: "A IA decide o que faz sentido. A nossa engenharia decide o que é permitido."
  - Full opacity, large scale

  **Exit State (1900vh):**
  - Text remains
  - Experience complete

  **Scroll-Driven Properties:**
  - Background transition: scroll 1800-1830%, gradient shift
  - First line: scroll 1830-1860%, opacity 0→1, y-offset 50px→0, color blue
  - Second line: scroll 1850-1880%, opacity 0→1, y-offset 50px→0, color gold
  - Final hold: scroll 1880-1900%, no change, static for reading

  **Critical Constraint:** No animation in final 100vh. Text must be completely static.

  ---

  # Failure Modes & Safeguards

  ## Scroll Hijacking Failure

  **Failure Mode:** User cannot scroll naturally, experience feels broken.

  **Safeguard:**
  - Scroll container is native browser scroll
  - No `preventDefault()` on scroll events
  - Pinning achieved via `position: sticky` with scroll-snap, not scroll blocking
  - If JS fails, content remains accessible as long vertical page

  ## Animation Jank

  **Failure Mode:** Frame rate drops below 30fps during transitions.

  **Safeguards:**
  - All animations use `transform` and `opacity` only (GPU accelerated)
  - No `filter: blur()` animations during scroll
  - No `width`/`height` animations—use `scale` instead
  - `will-change: transform` applied to animated elements 500ms before animation

  **Detection:** PerformanceObserver monitoring frame rate. If < 30fps for > 3s, disable non-critical animations via CSS class injection.

  ## Rapid Scroll Skipping

  **Failure Mode:** User scrolls quickly, misses critical content.

  **Safeguards:**
  - Scroll-snap points at scene boundaries (not during scenes)
  - Snap behavior: `scroll-snap-type: y proximity` (not mandatory)
  - Scene transitions pinned to ensure visibility even with rapid scroll
  - No essential information in first or last 10% of scene (buffer zones)

  ## Reduced Motion Preference

  **Failure Mode:** Motion-sensitive users cannot tolerate animation.

  **Safeguard:**
  - Media query `@media (prefers-reduced-motion: reduce)` disables:
    - All transform animations (use opacity only)
    - Parallax effects
    - Number count-up animations (show final values immediately)
    - Glow/pulse effects
  - Scene transitions become simple opacity fades
  - Content remains fully accessible

  ## Mobile Viewport

  **Failure Mode:** Layout breaks on narrow screens.

  **Safeguards:**
  - Minimum supported width: 320px
  - Layout transforms to single column below 768px
  - Font sizes: min 16px (no zoom issues)
  - Touch scroll: Native, no custom touch handlers
  - Scene 3 (globe) simplifies to 2D projection on mobile

  ## Asset Loading Failure

  **Failure Mode:** Images fail to load, layout breaks.

  **Safeguards:**
  - All critical visuals have CSS gradient fallbacks
  - Text content never depends on image visibility
  - `onerror` handlers replace failed images with colored placeholders
  - Loading state: Skeleton screens match final layout dimensions

  ## JavaScript Failure

  **Failure Mode:** JS fails to load or execute.

  **Safeguard:**
  - Core content is semantic HTML (progressive enhancement)
  - Without JS: Page is long scrollable document with all scenes visible
  - No blank screens without JS
  - CSS-only scroll indicators (`position: sticky` section headers)

  ---

  # Performance Model

  ## Render Budget

  **Target Devices:** Low-end laptops (Intel i3, integrated graphics, 4GB RAM)

  **Budget Allocation per Frame:**
  - Style calculations: < 5ms
  - Layout: < 10ms (avoid layout thrashing)
  - Paint: < 8ms
  - Composite: < 5ms
  - Total: < 16ms (60fps) under normal conditions
  - Degraded target: < 33ms (30fps) acceptable during transitions

  ## Memory Budget

  **Total JS Heap:** < 100MB
  **Image Memory:** < 50MB resident
  **DOM Nodes:** < 5000

  **Optimization:**
  - Scene elements removed from DOM when > 2 scenes away
  - Images lazy-loaded but prefetched for next 2 scenes
  - No canvas elements (SVG preferred for crispness and memory)

  ## Scroll Performance

  **Scroll Listener:** Passive only (`{ passive: true }`)
  **Throttling:** No throttling on RAF, but state calculation debounced to RAF
  **Interpolation:** Pre-calculate interpolation curves at initialization, not per frame

  ## Battery Consideration

  **Detection:** If `navigator.getBattery()` reports < 20%, disable:
  - Glow effects
  - Particle animations (if any)
  - Background gradients (use solid colors)

  ---

  # Accessibility Model

  ## Screen Reader Experience

  **Structure:**
  - Each scene is a `<section>` with `aria-labelledby` pointing to scene title
  - Scene titles are `<h2>` (hierarchy: h1 for presentation title, h2 for scenes)
  - Decorative visuals (globe, roads) have `aria-hidden="true"`
  - Data values announced with `aria-live="polite"` during number reveals

  **Navigation:**
  - Skip link: "Skip to scene X" dropdown at top
  - Keyboard navigation: Arrow keys advance to next/prev scene snap point
  - Focus management: Focus moves to scene title when scene becomes active

  ## Color Independence

  **Requirement:** All information conveyed by color must also be conveyed by:
  - Text labels
  - Iconography
  - Position/ordering

  **Specifics:**
  - Scene 15 (4 Achados): Red/orange cards also have warning icons
  - Scene 6 (3 layers): Colors (cyan/blue/gold) also have labels and positions (top/middle/bottom)
  - Scene 3 (lines): Red vs blue lines also differ in style (dashed vs solid)

  ## Motion Sensitivity

  See "Reduced Motion Preference" in Failure Modes.

  ## Cognitive Accessibility

  **Reading Level:** Target 8th grade (ensures broad comprehension)
  **Sentence Length:** Max 20 words per sentence in text displays
  **Abbreviations:** All expanded on first use (YAML → "YAML, a readable data format")
  **Focus Indicators:** Visible 3px outline on all interactive elements

  ## Low Vision

  **Text Scaling:** Supports up to 200% zoom without horizontal scroll
  **Contrast:** All text meets WCAG AA (4.5:1), large text meets AAA (7:1)
  - Scene 18 text: Minimum 48px at 100% zoom, 24px at 200% zoom

  ---

  # Implementation Guarantees

  ## Deterministic Behavior

  **Guarantee:** Given the same scroll position, the visual state is identical across:
  - Browsers (Chrome, Firefox, Safari, Edge)
  - Operating systems
  - Screen resolutions
  - Time of day

  **Mechanism:**
  - No random values in animations
  - No time-based calculations (all scroll-based)
  - No device-specific branching beyond feature detection
  - Interpolation curves defined as mathematical functions, not approximations

  ## Debuggability

  **Requirement:** A developer can understand the state at any scroll position without running the code.

  **Mechanism:**
  - Each scene exports its state calculation function for unit testing
  - Scroll position → state mapping is logged in debug mode (console.table)
  - Visual debugging overlay: Shows current scene, phase, and localProgress when `?debug=true` in URL

  ## Graceful Degradation

  **Levels:**
  1. **Full Experience:** Modern browser, JS enabled, good GPU
  2. **Static Experience:** Modern browser, JS disabled—long scrollable document
  3. **Reduced Motion:** Respects `prefers-reduced-motion`
  4. **Minimal:** Very old browser—single column text-only version (semantic HTML still valid)

  ## No Developer Intuition Required

  **All decisions are documented:**
  - No "use your judgment" statements
  - All pixel values specified or calculated from base units
  - All timing functions explicitly defined
  - All asset formats specified
  - All fallback behaviors explicitly described

  ## Testability

  **Each scene can be tested in isolation:**
  - Scene 5 works without Scene 4 being present
  - State calculations are pure functions (input: scroll position, output: visual state)
  - Unit tests can verify: at scroll 550vh, Scene 5 property X equals value Y

  ---

  # Asset Specification

  ## Image Formats

  **Preferred:** SVG (scalable, small file size, crisp)
  **Fallback:** WebP with PNG fallback
  **No:** JPEG (no transparency support needed, but lossy artifacts unacceptable for UI elements)

  ## Resolution Requirements

  **SVG:** ViewBox defined, no raster elements
  **Raster:** 2x display size for retina (e.g., if displayed at 500px, source is 1000px)
  **Maximum file size:** 100KB per image (except Scene 3 globe which may be 200KB)

  ## Color Profiles

  **All assets:** sRGB
  **No CMYK** (web conversion issues)

  ---

  # Final Notes for Implementation Team

  1. Use this document as the single source of truth. Any ambiguity should be resolved by referring to the Scene Specifications section.

  2. Build Scene 1 first. If Scene 1 works (dots appear, line draws, text fades), the architecture is sound.

  3. Scene 3 (globe) is the highest risk for performance. Test on actual low-end hardware, not just browser DevTools throttling.

  4. Scene 18 has no animation—ensure this is implemented as static. A "final polish" animation here would violate the specification.

  5. The Skeptic Reviewer role exists because these safeguards were explicitly challenged. Do not remove safeguards without equivalent re
  placement.

  6. This specification prioritizes stability over visual flourish. If a visual effect cannot be implemented within the Performance Model
  , it must be cut, not approximated.