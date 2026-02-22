# assets_inventory.md

---

## Summary

**Total Assets:** 47 image files + 4 font families + 3 icon sets  
**Total Estimated Size:** ~15-20 MB  
**Format Priority:** SVG → WebP → PNG

---

## Scene 0: Abertura Pessoal

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 0-1 | Globo Terrestre | 3D/Illustration | SVG/PNG | 200KB | Earth from space, South America visible |
| 0-2 | Zoom América do Sul | Map | SVG | 50KB | Highlighted Brazil, Cuiabá marked |
| 0-3 | Transição Escuro | Gradient | CSS | - | Fade to dark background |

### Color Palette
- **Space Background:** #1A1A2E → #0D0D1A (gradient)
- **Earth:** #0C326F (TCU Blue) at 60% opacity
- **Cuiabá Marker:** #D4AF37 (Gold) with glow
- **Text:** #FFFFFF (White)

### Notes
- Globe can be CSS-only (radial gradients) or Three.js for rotation
- Cuiabá position: 15.6010° S, 56.0974° W

---

## Scene 1: Dois Pontos

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 1-1 | Dois Pontos + Linha | Graphic | SVG | 5KB | Two dots connected by straight line |
| 1-2 | Apenas Dois Pontos | Graphic | SVG | 3KB | Dots only (for animation) |
| 1-3 | Apenas Linha | Graphic | SVG | 2KB | Line only (for draw animation) |

### Specifications
- **Dot 1 Position:** X: 25%, Y: 50%
- **Dot 2 Position:** X: 75%, Y: 50%
- **Dot Size:** 24px diameter
- **Line Stroke:** 3px, gradient #0C326F → #D4AF37
- **Background:** #FFFFFF (Pure white)

### Animation Requirements
- Stroke-dasharray animation for line drawing
- No external assets needed

---

## Scene 2: A Estrada

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 2-1 | Estrada Topo | Illustration | SVG | 30KB | Winding road from above |
| 2-2 | Apenas Estrada | Path | SVG | 15KB | Road path for animation |
| 2-3 | Terreno Paisagem | Background | SVG/PNG | 100KB | Mountains, hills, vegetation |

### Specifications
- **Road Color:** #8B7355 (earth tone)
- **Straight Line:** Dashed, 40% opacity, #BDBDBD
- **Terrain:** #9CAF88 (sage), #BCAAA4 (taupe), #B0BEC5 (mountains)
- **Background:** Gradient #E8F4F8 → #F5F1E8

### Critical Note
- Dots must be in EXACT same position as Scene 1 for Morph transition

---

## Scene 3: O Planeta

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 3-1 | Globo Wireframe | 3D | SVG/WebP | 150KB | Wireframe Earth, dark background |
| 3-2 | Globo Elemento | Component | SVG | 80KB | Globe for layering |
| 3-3 | Linha Vermelha | Path | SVG | 5KB | Dashed line through center |
| 3-4 | Arco Azul | Path | SVG | 5KB | Curved line around surface |

### Specifications
- **Background:** #1A1A2E (Dark slate)
- **Globe Grid:** #0C326F at 30% opacity
- **Red Line:** #E57373, dashed, through center
- **Blue Arc:** #4FC3F7, glowing, around surface
- **Markers:** #4FC3F7 with pulse glow

### Positions
- **Brazil (Cuiabá):** 35% X, 65% Y
- **Amsterdam:** 65% X, 35% Y

---

## Scene 4: O Problema

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 4-1 | Visualização Escala | Abstract | SVG | 50KB | Document flow visualization |
| 4-2 | Ícones Documentos | Icon Set | SVG | 20KB | ID cards, titles, forms |
| 4-3 | Dois Auditores | Silhouette | SVG | 10KB | Two professional figures |

### UI Components
- **Cards:** Glassmorphism (backdrop-filter: blur)
- **Number Font:** SF Pro Display Heavy, 120px
- **Card 1:** R$ 51 Bilhões (Gold #D4AF37)
- **Card 2:** 3.5 Milhões (Blue #0C326F)
- **Card 3:** 10.7 Milhões (Blue #0C326F)

### Icons Needed
- Money/stack icon
- Family/group icon
- Documents/pages icon

---

## Scene 5: A Solução

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 5-1 | Conceito Protocolo | Abstract | SVG | 40KB | Protocol vs programming |
| 5-2 | Protocolo vs Programação | Icon Set | SVG | 15KB | Comparison icons |

### UI Components
- **Negations:** ✗ marks in #C53030 (Red)
- **Affirmations:** ✓ marks in #0C326F (Blue)
- **Cards:** Split layout, glassmorphism

### Icons Needed
- Code brackets (</>)
- Document/checkmark
- Scales of justice
- Clipboard/seal

---

## Scene 6: Arquitetura

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 6-1 | Três Camadas | Diagram | SVG | 30KB | Three-layer architecture |
| 6-2 | Fluxo Dados | Icon Set | SVG | 15KB | Data flow icons |
| 6-3 | Guardrails | Illustration | SVG | 25KB | AI contained by framework |

### Layer Specifications
- **Layer 1 (IA):** Cyan #4FC3F7, cloud shape, fluid
- **Layer 2 (Validação):** Blue #0C326F, geometric, structured
- **Layer 3 (Decisão):** Gold #D4AF37, solid, authoritative
- **Arrows:** SVG paths with stroke-dash animation

### Icons Needed
- Document (input)
- Gears/processing
- Checkmark/seal (output)

---

## Scene 7: Demonstração

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 7-1 | Interface Sistema | Mockup | SVG/PNG | 100KB | Dashboard UI mockup |
| 7-2 | Documento Processando | Illustration | SVG | 30KB | Document → processing flow |
| 7-3 | Status Icons | Icon Set | SVG | 10KB | Processing states |

### Layout
- **Left:** Chaotic documents (red/orange)
- **Center:** Processing machine (gray + cyan glow)
- **Right:** Organized output (green + checkmarks)

### Icons Needed
- Chaotic folder (red)
- Processing box with glow
- Organized folder (green)
- Checkmark badge

---

## Scene 8: Conclusão (Intermediária)

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 8-1 | Jornada Completa | Composite | SVG | 50KB | Ghost images from previous |
| 8-2 | Guardrails Final | Illustration | SVG | 30KB | Final guardrails metaphor |

### Ghost Images
- Scene 1: 20% opacity
- Scene 2: 40% opacity
- Scene 3: Dark globe
- Scene 6: Three layers

---

## Scene 9: MCP

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 9-1 | Arquitetura MCP | Diagram | SVG | 40KB | AI inside database |
| 9-2 | Inversão Fluxo | Arrows | SVG | 10KB | Flow direction arrows |
| 9-3 | Cadeado Read-Only | Icon | SVG | 5KB | Security lock |

### Components
- **Database:** Cylinder, graphite #4A5568
- **AI:** Cyan glow #4FC3F7, inside perimeter
- **Locks:** Shield icons, red #C53030
- **Connection:** Glowing lock mechanism

---

## Scene 10: 6 Abordagens

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 10-1 | Grid Seis Abordagens | Grid | SVG | 60KB | 3x2 card grid |
| 10-2 | Ícones Seis | Icon Set | SVG | 30KB | Six capability icons |

### Card Icons (6 total)
1. Camera/eye (Computer Vision)
2. Code brackets (SQL)
3. Bell curve (Statistics)
4. Database schema (Reverse Engineering)
5. Documents (Report Generation)
6. Shield/check (Validation)

### Card Style
- Glassmorphism
- Slate gray + warm tones
- Apple Keynote aesthetic

---

## Scene 11: Zero Kelvin

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 11-1 | Diagrama Invariantes | Flowchart | SVG | 35KB | Number preservation flow |
| 11-2 | Cristal Congelamento | Illustration | SVG | 40KB | Ice crystal aesthetic |
| 11-3 | Termômetro Zero | Graphic | SVG | 15KB | Absolute zero gauge |

### Specifications
- **Numbers:** 3,175,345 (monospace, identical)
- **Ice Effect:** #4FC3F7, #0C326F (cold blues)
- **Crystal Texture:** Subtle, glistening
- **Locks:** On each number card

---

## Scene 12: Idempotência

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 12-1 | Terminal Camadas | Composite | SVG | 50KB | Terminal + 5 layers |
| 12-2 | Ícone Semente | Icon | SVG | 5KB | Seed/DNA symbol |

### Components
- **Terminal:** Dark mode, #1A1A2E, cyan text
- **Output:** "Result: Idempotent. 16,501 Records"
- **Layers:** 5 stacked rectangles (sand, slate, pale green)
- **Equation:** Icons + text

---

## Scene 13: Demo ao Vivo

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 13-1 | Fluxo Isométrico | Illustration | SVG | 50KB | Pipeline 3D view |
| 13-2 | Ícones Estado | Icon Set | SVG | 20KB | Processing states |
| 13-3 | Terminal Snapshot | Screenshot | PNG | 200KB | Optional video frame |

### Pipeline States
1. Input: Chaotic (red)
2. Processing: Machine (gray + cyan)
3. Output: Organized (green)

---

## Scene 14: Papéis de Trabalho

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 14-1 | Fluxo YAML LaTeX | Diagram | SVG | 45KB | YAML → Tree → LaTeX |
| 14-2 | Ícone LaTeX | Icon | SVG | 10KB | Academic document |

### Flow Components
- **YAML:** Code icon, green
- **Tree:** 12 branches
- **LaTeX:** Document with formulas, gold

---

## Scene 15: Os 4 Achados

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 15-1 | Grid Impacto | Grid | SVG | 60KB | 2x2 impact cards |
| 15-2 | Ícones Alerta | Icon Set | SVG | 20KB | Warning icons |

### Numbers (Animated)
- **27.1%** - Inadequado (Orange #ED8936)
- **45.92%** - Erro Geoespacial (Orange #ED8936)
- **90.62%** - Inválido (Red #C53030)
- **94.1%** - Falha Absoluta (Red #C53030)

### Icons
- Document with warning
- Map pin with error
- Email with skull (falecidos)
- Broken code brackets

---

## Scene 16: Novo Auditor

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 16-1 | Novo Perfil | Composite | SVG | 50KB | Roles + bar chart |
| 16-2 | Ícones Evolução | Icon Set | SVG | 20KB | Career evolution icons |

### Components
- **Roles:** 4 items with icons (left)
- **Chart:** 10 months vs 2 months (right)
- **Tooltip:** "Reinvested in Analytical Depth"

### Role Icons
- Terminal (YAML Coder)
- Brain (Interpreter)
- Conductor/orbit (Orchestrator)
- Gear (Engineer)

---

## Scene 17: O Legado

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 17-1 | Dashboard Três Colunas | Dashboard | SVG | 80KB | Executive summary |

### Columns
- **Left:** Quantitativos (R$ 51B, 210+ memos, 9.7/10)
- **Center:** Feats (3.7M records, 12.8M CPFs, etc.)
- **Right:** Roadmap (YAML Template, RTCU, Orchestrator)

---

## Scene 18: Mic Drop

### Visual Assets

| ID | Name | Type | Format | Size | Description |
|----|------|------|--------|------|-------------|
| 18-1 | Background Tipografia | Solid | CSS | - | Minimal background |

### Specifications
- **Background:** #FFFFFF (White) OR #0D0D1A (Dark Space)
- **Text 1:** "A IA decide o que faz sentido." - Blue #0C326F
- **Text 2:** "A nossa engenharia decide o que é permitido." - Gold #D4AF37
- **Font Size:** 48px minimum
- **Style:** Heavy/Bold, tracking +0.05em

### Critical Note
- NO IMAGES
- NO ANIMATION
- Typography only

---

## Font Requirements

### Primary Font: SF Pro (San Francisco)
- **Weights:** Light, Regular, Medium, Bold, Heavy
- **Usage:** All UI text, headings, body
- **Fallback:** Inter, Helvetica Neue, Arial

### Monospace Font: SF Mono / JetBrains Mono
- **Usage:** Terminal scenes, code, numbers
- **Fallback:** Consolas, Monaco, Courier

### License
- SF Pro: Apple license (free for web use)
- Inter: Open Source (Google Fonts)
- JetBrains Mono: Open Source

---

## Icon Sets

### Set 1: Hero Icons (Outline)
- **Usage:** General UI, navigation
- **License:** MIT (free)
- **Size:** 24px default

### Set 2: Phosphor Icons
- **Usage:** Specialized technical icons
- **License:** MIT (free)
- **Weight:** Light, Regular, Bold

### Set 3: Custom SVG
- **Usage:** Specific metaphors (globe, guardrails, etc.)
- **Source:** Generate via prompts or custom design

---

## Animation Assets

### Lottie (Optional)
- Complex animations (globe rotation, document flow)
- JSON format
- ~50-100KB per animation

### CSS Animations (Preferred)
- All simple transitions
- No external files
- Better performance

### GSAP
- ScrollTrigger plugin (required)
- Timeline animations
- License: Standard (free for this use)

---

## Generation Status

### Prompts Ready (in nanobanana/)
- [x] All 47 prompts generated
- [x] Organized by scene
- [x] Ready for Midjourney/DALL-E/Leonardo

### Next Steps
1. Run prompts through image generators
2. Optimize images (SVGO for SVGs, ImageOptim for PNGs)
3. Convert to WebP where appropriate
4. Test in browser
5. Adjust colors to match TCU palette

---

## Asset Pipeline

```
Generation (Midjourney/DALL-E)
    ↓
Optimization (SVGO/ImageOptim)
    ↓
Conversion (WebP fallback PNG)
    ↓
Integration (Import into codebase)
    ↓
Testing (Cross-browser, performance)
```

---
