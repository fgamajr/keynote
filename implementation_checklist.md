# implementation_checklist.md

---

## Phase 1: Foundation Setup

### Project Structure
- [ ] Create repository with standard web project layout
- [ ] Set up build tool (Vite, Webpack, or Rollup)
- [ ] Configure TypeScript (strict mode)
- [ ] Set up linting (ESLint) and formatting (Prettier)
- [ ] Create folder structure:
  ```
  /src
    /scenes        (19 scene components)
    /components    (reusable UI elements)
    /hooks         (scroll detection, animation)
    /utils         (interpolation, state calc)
    /assets        (images, fonts)
  /public          (static assets)
  ```

### Core Dependencies
- [ ] Install GSAP (with ScrollTrigger plugin)
- [ ] Install React or Vue (if using framework)
- [ ] Install intersection-observer polyfill
- [ ] Install testing libraries (Jest, Testing Library)

### Global Styles
- [ ] Set up CSS reset (Normalize.css or similar)
- [ ] Define CSS custom properties:
  - Colors: TCU blue (#0C326F), Gold (#D4AF37), etc.
  - Typography scale
  - Spacing scale
  - Z-index layers
- [ ] Set up media queries for responsive breakpoints

---

## Phase 2: Scroll System Architecture

### Scroll Container
- [ ] Implement native scroll container (overflow-y: auto)
- [ ] Calculate total scroll height: 1900vh + 100vh buffer
- [ ] Set up scroll snap points at scene boundaries
- [ ] Implement passive scroll listeners

### State Management
- [ ] Create scroll position tracking hook
- [ ] Implement scene detection logic
- [ ] Create interpolation utilities:
  - Linear interpolation
  - Ease-in/out functions
  - Clamp functions
- [ ] Set up performance monitoring (FPS counter in dev)

### Scene Router
- [ ] Create scene registry (19 scenes mapped to scroll ranges)
- [ ] Implement active scene detection
- [ ] Set up scene transition handling
- [ ] Create fallback for no-JS (static content order)

---

## Phase 3: Scene Implementation (Per Scene)

### Scene 0: Abertura
- [ ] Implement globe component (Three.js or SVG)
- [ ] Create zoom animation to South America
- [ ] Add Cuiabá marker with pulsing glow
- [ ] Text reveal: "Fernando Gama", "Cuiabá, MT"
- [ ] Transition to white background at end

### Scene 1: Dois Pontos
- [ ] Create two dots at 25% and 75% horizontal
- [ ] Implement line draw animation (SVG stroke-dashoffset)
- [ ] Text: "O caminho mais curto entre dois pontos"
- [ ] **CRITICAL**: Dot positions must match Scene 2 exactly

### Scene 2: A Estrada
- [ ] Implement Magic Move/Morph from Scene 1
- [ ] Add terrain topography (SVG paths)
- [ ] Add winding road (SVG path with stroke-dash animation)
- [ ] Fade straight line to 40% opacity, dashed
- [ ] Text: "Exceto no mundo real"

### Scene 3: O Planeta
- [ ] Create dark slate background
- [ ] Implement wireframe globe (3D or SVG)
- [ ] Add Brazil and Amsterdam markers
- [ ] Draw red dashed line through center
- [ ] Draw blue arc around surface
- [ ] Text: "Restrições tornam soluções possíveis"

### Scene 4: O Problema
- [ ] Create glassmorphism cards (CSS backdrop-filter)
- [ ] Implement number count-up animation
- [ ] Cards: R$ 51B, 3.5M famílias, 10.7M documentos
- [ ] Rodapé: "63.588 registros na amostra"

### Scene 5: A Solução
- [ ] Split screen: Negações (✗) vs Afirmações (✓)
- [ ] Staggered reveal of list items
- [ ] Main title: "Auditoria como Código"
- [ ] Comparison table: NÃO É / É
- [ ] Final text: "A IA interpreta. O Código audita."

### Scene 6: Arquitetura
- [ ] Three horizontal layers (cards)
- [ ] Layer 1: Cyan (#4FC3F7) - IA
- [ ] Layer 2: Blue (#0C326F) - Validação
- [ ] Layer 3: Gold (#D4AF37) - Decisão
- [ ] SVG arrows connecting layers
- [ ] Text: "A IA sugere. O Protocolo decide."

### Scene 7: Demonstração
- [ ] Isometric layout (left to right flow)
- [ ] Left: Chaotic document icons (red)
- [ ] Center: Processing box with cyan glow
- [ ] Right: Organized folders (green, checkmarked)
- [ ] Time display: "3.2 segundos"

### Scene 8: Conclusão (Intermediária)
- [ ] Ghost images from previous scenes (20-40% opacity)
- [ ] Text: "A IA sugere. O Protocolo decide."
- [ ] Prepare for technical section transition

### Scene 9: MCP
- [ ] Database cylinder (PostgreSQL icon)
- [ ] AI inside database (not outside)
- [ ] Comparison: old model (data out) vs new model (AI in)
- [ ] Lock icons indicating Read-Only
- [ ] Text: "Read-Only. Sem exceções."

### Scene 10: 6 Abordagens
- [ ] Grid 3x2 of glassmorphism cards
- [ ] Icons for each capability:
  1. Visão Computacional (camera)
  2. SQL via Prompt (code)
  3. Análise Estatística (graph)
  4. Engenharia Reversa DDL (database)
  5. Geração de Relatórios (documents)
  6. Validação Multi-camadas (shield)

### Scene 11: Zero Kelvin
- [ ] Icy/crystal visual theme
- [ ] Three cards with identical number: "3,175,345"
- [ ] Lock icons on each card
- [ ] Thermometer graphic at "absolute zero"
- [ ] Text: "Os números não derretem"

### Scene 12: Idempotência
- [ ] Terminal window (dark mode, monospace font)
- [ ] Output: "Result: Idempotent. 16,501 Records"
- [ ] Stack of 5 anti-hallucination layers
- [ ] Equation: "Same Seed + Same Population = Same Records"

### Scene 13: Demo ao Vivo
- [ ] Isometric pipeline visualization
- [ ] Documents flowing left → center → right
- [ ] Machine glow pulse animation
- [ ] Output accumulation animation
- [ ] Optional: Video frame in corner

### Scene 14: Papéis de Trabalho
- [ ] Flow diagram: YAML → Tree → LaTeX
- [ ] Tree with 12 branches (Papéis de Trabalho)
- [ ] LaTeX document icon at end
- [ ] Text: "Audit as Code"

### Scene 15: Os 4 Achados
- [ ] Grid 2x2 of impact cards
- [ ] Numbers count up:
  - 27.1% Inadequado
  - 45.92% Erro Geoespacial
  - 90.62% Inválido (FALECIDOS)
  - 94.1% Falha Absoluta
- [ ] Red/orange critical color scheme

### Scene 16: Novo Auditor
- [ ] Left: New roles list (YAML Coder, Intérprete, Orquestrador, Engenheiro)
- [ ] Right: Bar chart comparing 10 months vs 2 months
- [ ] Tooltip: "Reinvested in Analytical Depth"
- [ ] Text: "De escritor para orquestrador"

### Scene 17: O Legado
- [ ] Dashboard 3 columns:
  - Left: Quantitativos (R$ 51B, 210+ memos, 9.7/10)
  - Center: Feats (3.7M records, 12.8M CPFs, etc.)
  - Right: Roadmap (YAML Template, RTCU publication)

### Scene 18: Mic Drop
- [ ] Minimal background (white or dark space)
- [ ] Single text: "A IA decide o que faz sentido. A nossa engenharia decide o que é permitido."
- [ ] First line: Blue (#0C326F)
- [ ] Second line: Gold (#D4AF37)
- [ ] **CRITICAL**: No animation in this scene. Static only.

---

## Phase 4: Animation System

### Interpolation Engine
- [ ] Implement linear interpolation utility
- [ ] Implement easing functions:
  - easeOutQuad
  - easeInOutCubic
  - easeOutElastic (for number pop)
- [ ] Create scroll-to-progress mapper
- [ ] Implement phase detection (entrance/settled/exit)

### Performance Optimization
- [ ] Add `will-change: transform` before animations
- [ ] Remove `will-change` after animations complete
- [ ] Implement requestAnimationFrame loop
- [ ] Add frame rate monitoring

### Reduced Motion Support
- [ ] Implement `prefers-reduced-motion` media query
- [ ] Create static fallbacks for all animations
- [ ] Disable parallax effects when reduced motion preferred
- [ ] Show final values immediately (no count-up)

---

## Phase 5: Asset Integration

### Image Handling
- [ ] Set up lazy loading with prefetch for next 2 scenes
- [ ] Implement blur-up placeholder technique
- [ ] Add error handling with fallback colors
- [ ] Optimize all images (WebP with PNG fallback)

### Font Loading
- [ ] Preload critical fonts (SF Pro or Inter)
- [ ] Implement font-display: swap
- [ ] Set up monospace font for terminal scenes

### SVG Optimization
- [ ] Run all SVGs through optimizer
- [ ] Ensure viewBox attributes set
- [ ] Test stroke-dasharray animations

---

## Phase 6: Testing & Quality

### Functional Testing
- [ ] Test scroll behavior at each scene boundary
- [ ] Verify all 19 scenes are reachable
- [ ] Test scene transitions (no glitches)
- [ ] Verify number animations work correctly

### Performance Testing
- [ ] Test on low-end laptop (target: 30fps minimum)
- [ ] Test on mobile devices
- [ ] Verify memory usage stays under 100MB
- [ ] Check for layout thrashing

### Accessibility Testing
- [ ] Keyboard navigation works (arrow keys)
- [ ] Screen reader announces scene changes
- [ ] Color contrast meets WCAG AA
- [ ] Reduced motion mode works

### Cross-Browser Testing
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

---

## Phase 7: Deployment Preparation

### Build Configuration
- [ ] Set up production build
- [ ] Enable minification
- [ ] Configure asset hashing
- [ ] Set up error tracking (Sentry optional)

### Hosting Setup
- [ ] Configure static hosting
- [ ] Set up CDN (if needed)
- [ ] Enable gzip/brotli compression
- [ ] Configure caching headers

### Documentation
- [ ] Write README with setup instructions
- [ ] Document scene modification process
- [ ] Create troubleshooting guide
- [ ] Archive source files

---

## Phase 8: Final Verification

### Pre-Launch Checklist
- [ ] All 19 scenes implemented and tested
- [ ] All animations smooth (30fps+ on target hardware)
- [ ] Accessibility audit passed
- [ ] Cross-browser testing completed
- [ ] No console errors
- [ ] Build successful and deployed
- [ ] Backup created

### Sign-Off
- [ ] Technical lead approval
- [ ] Design lead approval
- [ ] Accessibility review passed
- [ ] Performance budget met

---

## Critical Path (Minimum Viable)

If time-constrained, prioritize in this order:

1. **Scenes 0-8** (Core narrative: 0.5 days)
2. **Scroll system** (Foundation: 1 day)
3. **Scenes 15, 16, 18** (Impact, evolution, conclusion: 0.5 days)
4. **Scenes 9-14** (Technical depth: 1 day)
5. **Scenes 17** (Legacy: 0.25 days)
6. **Polish and testing** (1 day)

**Total minimum: 4 days for experienced team**

---
