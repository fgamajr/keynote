# SLIDE 2: A QUEBRA (A Estrada)
## Documento Técnico Unificado - Auditoria como Código (TCU)
**Data:** 21 de Fevereiro de 2026  
**Projeto:** Keynote Executiva - 10 minutos  
**Papel:** AGENTE ORQUESTRADOR - Coordenação Técnica Completa

---

# 1. CRONOGRAMA DO SLIDE 2 (Segundo a Segundo)

## Timeline Detalhada de Animação

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CRONOGRAMA VISUAL DO SLIDE 2                              ║
║                         (Duração Total: ~35 segundos)                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

TEMPO    │ ELEMENTO                    │ ANIMAÇÃO                    │ NARRAÇÃO
─────────┼─────────────────────────────┼─────────────────────────────┼────────────────────────────────
00:00    │ ESTADO INICIAL              │ Herdado do Slide 1          │ [Silêncio - deixar plateia
         │ • Ponto Azul (X:25%, Y:50%) │ (Magic Move entrega         │  achar que não mudou nada]
         │ • Ponto Dourado (X:75%,50%) │  elementos idênticos)       │
         │ • Linha reta sólida         │                             │
         │ • Título "Auditoria..."     │                             │
         │                             │                             │
00:02    │ TÍTULO MUDA                 │ Fade out (0.3s) +           │ "Exceto..."
         │ "Auditoria como Código" →   │ Fade in (0.3s)              │
         │ "Exceto no mundo real"      │ Total: 0.6s                 │
         │                             │                             │
00:03    │ TERRENO TOPOGRÁFICO         │ Fade in + Scale Y           │ "...no mundo real."
         │ • Curvas de nível           │ (de 0% para 100%)           │
         │ • Relevo suave              │ Duração: 0.8s               │
         │                             │ Easing: ease-out            │
         │                             │ Direção: Bottom → Top       │
         │                             │                             │
00:04    │ ESTRADA SINUOSA             │ Stroke Draw (path)          │ "A rota ideal não é a menor
         │ • Linha curva azul          │ Duração: 1.2s               │  distância geométrica."
         │ • Conecta os dois pontos    │ Easing: ease-in-out         │
         │   por caminho tortuoso      │ Direção: Esq → Dir          │
         │                             │                             │
00:05    │ LINHA RETA TRANSFORMA       │ Morph: Sólida → Tracejada   │ [Pausa de 0.5s]
         │ • Opacity: 100% → 50%       │ Duração: 0.8s               │
         │ • Stroke style: alterado    │                             │
         │                             │                             │
00:06    │ LABELS DA ESTRADA           │ Fade in + Slide up          │ "A rota ideal é o caminho
         │ • "GUARDRAILS" (curva 1)    │ Stagger: 0.2s entre cada    │  mais curto entre o que é
         │ • "RESTRIÇÕES" (curva 2)    │ Duração: 0.5s cada          │  permitido."
         │ • "REGRAS" (curva 3)        │                             │
         │                             │                             │
00:08    │ DESTAQUE NOS PONTOS         │ Pulse animation             │ [Gesto para a estrada]
         │ • Glow aumentado            │ Duração: 0.4s               │
         │ • Escala: 1.0 → 1.1 → 1.0   │                             │
         │                             │                             │
00:09    │ TEXTO EXPLICATIVO           │ Fade in                     │ "E guardem bem esse conceito.
         │ (opcional - subtítulo)      │ Duração: 0.6s               │  Ele explica absolutamente
         │                             │                             │  todas as decisões de
         │                             │                             │  engenharia que tomamos."
         │                             │                             │
00:12    │ ESTADO FINAL - HOLD         │ Todos elementos estáveis    │ [Pausa dramática - deixar
         │                             │                             │  a frase assentar]
         │                             │                             │
00:15    │ PREPARAÇÃO TRANSIÇÃO        │ Elementos estabilizados     │ [Preparar transição para
         │                             │ para Slide 3                │  Slide 3 - O Problema Real]
─────────┴─────────────────────────────┴─────────────────────────────┴────────────────────────────────
```

## Diagrama de Estados do Slide

```
SLIDE 2 - MÁQUINA DE ESTADOS

┌─────────────┐    Magic Move     ┌─────────────┐
│  SLIDE 1    │ ─────────────────→│   ESTADO    │
│   (fim)     │    (0.5s)         │   INICIAL   │
└─────────────┘                   └──────┬──────┘
                                         │ 00:00
                                         ▼
                              ┌──────────────────────┐
                              │ • Dois pontos visíveis│
                              │ • Linha reta sólida  │
                              │ • Título anterior    │
                              │   (herdado)          │
                              └──────────┬───────────┘
                                         │ 00:02
                                         ▼
                              ┌──────────────────────┐
                              │   TÍTULO MUDA        │
                              │ "Exceto no mundo     │
                              │      real"           │
                              └──────────┬───────────┘
                                         │ 00:03
                                         ▼
                              ┌──────────────────────┐
                              │  TERRENO APARECE     │
                              │ • Curvas de nível    │
                              │ • Topografia         │
                              └──────────┬───────────┘
                                         │ 00:04
                                         ▼
                              ┌──────────────────────┐
                              │  ESTRADA APARECE     │
                              │ • Caminho sinuoso    │
                              │ • Conecta pontos     │
                              └──────────┬───────────┘
                                         │ 00:05
                                         ▼
                              ┌──────────────────────┐
                              │  LINHA TRANSFORMA    │
                              │ • Sólida→Tracejada   │
                              │ • Opacity 50%        │
                              └──────────┬───────────┘
                                         │ 00:06
                                         ▼
                              ┌──────────────────────┐
                              │  LABELS APARECEM     │
                              │ • Guardrails         │
                              │ • Restrições         │
                              │ • Regras             │
                              └──────────┬───────────┘
                                         │ 00:09
                                         ▼
                              ┌──────────────────────┐
                              │   TEXTO FINAL        │
                              │  (conceito-chave)    │
                              └──────────┬───────────┘
                                         │ 00:12
                                         ▼
                              ┌──────────────────────┐
                              │   ESTADO FINAL       │
                              │  (hold até 00:35)    │
                              └──────────────────────┘
```

---

# 2. MAPA DE TRANSIÇÃO SLIDE 1 → SLIDE 2

## 2.1 Elementos que PERSISTEM (Magic Move)

| Elemento | Slide 1 | Slide 2 | Ação de Transição |
|----------|---------|---------|-------------------|
| **Ponto Azul** | X: 25%, Y: 50% | X: 25%, Y: 50% | **MORPH** - Mesma posição exata |
| **Ponto Dourado** | X: 75%, Y: 50% | X: 75%, Y: 50% | **MORPH** - Mesma posição exata |
| **Linha Conectora** | Reta sólida | Reta tracejada (50% opacity) | **MORPH** - Transformação de estilo |
| **Fundo** | Branco #FFFFFF | Branco/cinza claro #F8F9FA | **MORPH** - Mudança sutil |

## 2.2 Elementos que TRANSFORMAM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ANIMAÇÕES DE TRANSFORMAÇÃO                               │
└─────────────────────────────────────────────────────────────────────────────┘

LINHA RETA (Slide 1) → LINHA TRACEJADA (Slide 2)
┌──────────────────────┐              ┌──────────────────────┐
│  ████████████████    │              │  ░░░░░░░░░░░░░░░░░░  │
│  (sólida, 100%)      │   MORPH      │  (tracejada, 50%)    │
│  stroke-width: 3px   │ ────────────→│  stroke-width: 2px   │
│  opacity: 1.0        │   0.8s       │  opacity: 0.5        │
│  #0C326F→#D4AF37     │              │  mesmas cores        │
└──────────────────────┘              └──────────────────────┘

TÍTULO (Slide 1) → TÍTULO (Slide 2)
┌──────────────────────────────┐      ┌──────────────────────────────┐
│  "Auditoria como Código"     │      │   "Exceto no mundo real"     │
│  SF Pro Bold, 64px, #0C326F  │ FADE │   SF Pro Bold, 64px, #1A202C │
│  (centro, abaixo da linha)   │ ────→│   (centro, topo do slide)    │
└──────────────────────────────┘      └──────────────────────────────┘
```

## 2.3 Elementos NOVOS (Aparições)

| Elemento | Descrição | Momento de Aparição | Animação |
|----------|-----------|---------------------|----------|
| **Terreno Topográfico** | Curvas de nível em cinza claro | 00:03 | Fade in + Scale Y |
| **Estrada Sinuosa** | Linha curva em azul #0C326F | 00:04 | Stroke draw (path) |
| **Labels Guardrails** | Textos ao longo da estrada | 00:06 | Fade in + Slide up |
| **Ícones de Restrição** | Símbolos sutis nas curvas | 00:07 | Pop in (scale) |

## 2.4 Diagrama de Camadas (Z-Index)

```
SLIDE 2 - ORDEM DAS CAMADAS (Z-INDEX)

┌─────────────────────────────────────────────────────────────┐
│  CAMADA 5 (Z: 50) - PONTOS                                  │
│  • Ponto Azul (X:25%, Y:50%)                                │
│  • Ponto Dourado (X:75%, Y:50%)                             │
│  • Sombra suave (drop-shadow)                               │
├─────────────────────────────────────────────────────────────┤
│  CAMADA 4 (Z: 40) - LINHA RETA (tracejada)                  │
│  • Linha original (agora tracejada, 50% opacity)            │
│  • Lembra o "caminho imaginado"                             │
├─────────────────────────────────────────────────────────────┤
│  CAMADA 3 (Z: 30) - ESTRADA                                 │
│  • Linha curva sinuosa (azul #0C326F)                       │
│  • Stroke-width: 4px (mais grossa que a reta)               │
│  • Efeito de profundidade sutil                             │
├─────────────────────────────────────────────────────────────┤
│  CAMADA 2 (Z: 20) - TERRENO/TOPOGRAFIA                      │
│  • Curvas de nível (cinza #E2E8F0)                          │
│  • Relevo suave (efeito de profundidade)                    │
│  • Fundo cinza muito claro (#F8F9FA)                        │
├─────────────────────────────────────────────────────────────┤
│  CAMADA 1 (Z: 10) - FUNDO                                   │
│  • Branco/cinza claro #F8F9FA                               │
│  • (antes era #FFFFFF puro no Slide 1)                      │
└─────────────────────────────────────────────────────────────┘

NOTA CRÍTICA: Os pontos DEVEM estar na camada mais alta para
parecerem "flutuar" sobre a estrada e o terreno.
```

---

# 3. ESPECIFICAÇÕES CRÍTICAS

## 3.1 Coordenadas dos Pontos (VERIFICAÇÃO DUPLA)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║              COORDENADAS CRÍTICAS - SLIDE 1 ↔ SLIDE 2                        ║
║                     ⚠️  NÃO ALTERAR ESTES VALORES  ⚠️                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│    Y: 10%                                                                    │
│       │                                                                      │
│       │    TÍTULO: "Exceto no mundo real"                                    │
│       │    (X: 50%, Y: 15%, centro)                                          │
│       │                                                                      │
│    Y: 30%                                                                    │
│       │                                                                      │
│       │                                                                      │
│       │         ┌─────┐                                              ╭─────╮ │
│       │         │     │    ═══════════════════════════════════════   │     │ │
│    Y: 50% ──────┤  ●  ├──────────────────────────────────────────────┤  ●  ├─┤
│       │         │     │   ↑ (linha tracejada, 50%)      (estrada) ↑  │     │ │
│       │         └──┬──┘   ═══════════════════════════════════════   ╰─────┯━│
│       │            │                                          ╭────╮      │ │
│       │            │                                     ╭────╯    ╰────╮ │ │
│       │            │                                ╭───╯               │ │ │
│       │            │                           ╭───╯                    │ │ │
│       │            │                      ╭────╯                        │ │ │
│       │            └─────────────────────╯                              │ │ │
│       │                                                                 │ │ │
│       │    X: 25%                                                  X: 75%    │
│                                                                              │
│    • PONTO 1 (Azul #0C326F):  X = 25%, Y = 50%                              │
│    • PONTO 2 (Dourado #D4AF37): X = 75%, Y = 50%                            │
│                                                                              │
│    TOLERÂNCIA MÁXIMA DE POSIÇÃO: ±2 pixels                                   │
│    Qualquer desvio maior quebrará o efeito Magic Move!                       │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Verificação de Consistência entre Slides

| Parâmetro | Slide 1 | Slide 2 | Tolerância | Status |
|-----------|---------|---------|------------|--------|
| Ponto 1 - X | 25.0% | 25.0% | ±0.1% | ✅ LOCKED |
| Ponto 1 - Y | 50.0% | 50.0% | ±0.1% | ✅ LOCKED |
| Ponto 2 - X | 75.0% | 75.0% | ±0.1% | ✅ LOCKED |
| Ponto 2 - Y | 50.0% | 50.0% | ±0.1% | ✅ LOCKED |
| Diâmetro P1 | 24px | 24px | ±1px | ✅ LOCKED |
| Diâmetro P2 | 24px | 24px | ±1px | ✅ LOCKED |

## 3.2 Cores Exatas

### Paleta de Cores do Slide 2

```
CORES INSTITUCIONAIS TCU (mantidas do Slide 1)
├── Azul TCU:        #0C326F  (RGB: 12, 50, 111)    → Ponto 1, Estrada
├── Dourado TCU:     #D4AF37  (RGB: 212, 175, 55)   → Ponto 2
│
CORES DE SUPORTE
├── Branco Puro:     #FFFFFF  (RGB: 255, 255, 255)  → Background base
├── Cinza Claro:     #F8F9FA  (RGB: 248, 249, 250)  → Novo background
├── Cinza Nível:     #E2E8F0  (RGB: 226, 232, 240)  → Curvas de topo
├── Cinza Médio:     #A0AEC0  (RGB: 160, 174, 192)  → Labels sutis
├── Cinza Escuro:    #4A5568  (RGB: 74, 85, 104)    → Texto alternativo
│
EFEITOS
├── Sombra Azul:     rgba(12, 50, 111, 0.3)
├── Sombra Ouro:     rgba(212, 175, 55, 0.3)
├── Linha Tracejada: rgba(74, 85, 104, 0.5)         → Opacidade 50%
```

### Gradientes e Transições

```
GRADIENTE DA ESTRADA (opcional)
┌─────────────────────────────────────────┐
│  #0C326F → #1E4A8C → #0C326F           │
│  (azul TCU → azul claro → azul TCU)     │
└─────────────────────────────────────────┘

LINHA TRACEJADA (Slide 2)
┌─────────────────────────────────────────┐
│  stroke: #4A5568                        │
│  stroke-width: 2px                      │
│  stroke-dasharray: 8, 6                 │
│  opacity: 0.5                           │
│  stroke-linecap: round                  │
└─────────────────────────────────────────┘
```

## 3.3 Tempos de Animação

### Tabela de Timings

| Animação | Início | Duração | Easing | Delay |
|----------|--------|---------|--------|-------|
| Magic Move (entrada) | 00:00 | 0.5s | ease-in-out | 0s |
| Título muda | 00:02 | 0.6s | ease-out | 0s |
| Terreno aparece | 00:03 | 0.8s | ease-out | 0s |
| Estrada desenha | 00:04 | 1.2s | ease-in-out | 0s |
| Linha transforma | 00:05 | 0.8s | ease-in-out | 0s |
| Labels aparecem | 00:06 | 0.5s | ease-out | 0.2s stagger |
| Pontos pulsam | 00:08 | 0.4s | spring | 0s |
| Texto final | 00:09 | 0.6s | ease-out | 0s |

### Curvas de Easing

```
EASING FUNCTIONS (CSS/Keynote equivalentes)

1. EASE-OUT (para aparições suaves)
   cubic-bezier(0, 0, 0.2, 1)
   
2. EASE-IN-OUT (para transformações)
   cubic-bezier(0.4, 0, 0.2, 1)
   
3. SPRING (para o pulso dos pontos)
   cubic-bezier(0.68, -0.55, 0.265, 1.55)
   
4. LINEAR (para draw da estrada)
   linear
```

---

# 4. MAPA DE SINCRONIZAÇÃO (Fala ↔ Visual)

## 4.1 Script Sincronizado Completo

```
╔══════════════════════════════════════════════════════════════════════════════╗
║              MAPA DE SINCRONIZAÇÃO - SLIDE 2                                 ║
║                   (Fala do Narrador × Elementos Visuais)                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:00 - 00:02 (2 segundos)                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [SILÊNCIO INTENCIONAL]                                                     │
│                                                                             │
│  VISUAL: Slide aparece idêntico ao anterior via Magic Move                  │
│  • Ponto Azul: visível (herdado)                                            │
│  • Ponto Dourado: visível (herdado)                                         │
│  • Linha reta: sólida, 100% opacity (herdada)                               │
│                                                                             │
│  AÇÃO DO PALESTRANTE:                                                       │
│  • Ficar em silêncio por 1 segundo                                          │
│  • Olhar para a plateia com expressão de "prestem atenção"                  │
│  • A plateia deve achar que o slide não mudou                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:02 - 00:03 (1 segundo)                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FALA: "Exceto..."                                                          │
│        ↑                                                                    │
│        └── Dica de suspense, voz baixa                                      │
│                                                                             │
│  VISUAL: Título começa a mudar                                              │
│  • "Auditoria como Código" fade out (0.3s)                                  │
│  • [micro pausa de 0.2s]                                                    │
│  • "Exceto no mundo real" fade in (0.3s)                                    │
│                                                                             │
│  SINCRONIZAÇÃO: A palavra "Exceto" coincide com o início do fade out        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:03 - 00:05 (2 segundos)                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FALA: "...no mundo real."                                                  │
│        "A rota ideal não é a menor distância geométrica."                   │
│                                                                             │
│  VISUAL:                                                                    │
│  00:03 - Terreno topográfico aparece (fade in + scale Y)                    │
│         • Curvas de nível surgem de baixo para cima                         │
│         • Efeito de "revelação" do mundo real                               │
│                                                                             │
│  00:04 - Estrada sinuosa começa a desenhar (stroke animation)               │
│         • A linha curva aparece gradualmente                                  │
│         • Conecta os mesmos dois pontos, mas por caminho tortuoso           │
│                                                                             │
│  SINCRONIZAÇÃO:                                                             │
│  • "mundo real" coincide com aparecimento do terreno                        │
│  • "rota ideal" coincide com início do desenho da estrada                   │
│  • "menor distância geométrica" enquanto a estrada desenha                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:05 - 00:06 (1 segundo)                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FALA: [PAUSA de 0.5 segundos - gesto para a estrada]                       │
│                                                                             │
│  VISUAL: Linha reta se transforma                                           │
│  • Stroke muda de sólido para tracejado                                     │
│  • Opacity reduz de 100% para 50%                                           │
│  • Visualmente: a "teoria" some, a "prática" (estrada) assume               │
│                                                                             │
│  SINCRONIZAÇÃO: A pausa permite que a plateia PROCESSE a transformação      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:06 - 00:08 (2 segundos)                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FALA: "A rota ideal é o caminho mais curto entre o que é permitido."       │
│                                                                             │
│  VISUAL: Labels aparecem ao longo da estrada                                │
│  • "GUARDRAILS" aparece na primeira curva (00:06.0)                         │
│  • "RESTRIÇÕES" aparece na segunda curva (00:06.2)                          │
│  • "REGRAS" aparece na terceira curva (00:06.4)                             │
│  • Cada label: fade in + slide up, 0.5s                                     │
│                                                                             │
│  00:08 - Pontos fazem pulso sutil (scale 1.0 → 1.1 → 1.0)                   │
│         • Destaque para o início e fim da jornada                           │
│                                                                             │
│  SINCRONIZAÇÃO:                                                             │
│  • "o que é permitido" coincide com labels de restrições                    │
│  • O pulso dos pontos reforça o conceito de início/fim                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:08 - 00:12 (4 segundos)                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FALA: "E guardem bem esse conceito.                                        │
│         Ele explica absolutamente todas as decisões de engenharia           │
│         que tomamos no nosso projeto."                                      │
│                                                                             │
│  VISUAL:                                                                    │
│  • Texto opcional aparece abaixo (fade in)                                  │
│  • Labels permanecem visíveis                                               │
│  • Estrada permanece destacada                                              │
│                                                                             │
│  SINCRONIZAÇÃO: Tom de voz mais sério, enfatizando a importância            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPO 00:12 - 00:35 (23 segundos - HOLD)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FALA: [SILÊNCIO ou transição para próxima fala]                            │
│                                                                             │
│  VISUAL: Estado final mantido                                               │
│  • Todos os elementos estáveis                                              │
│  • Plateia absorve a metáfora                                               │
│                                                                             │
│  AÇÃO: Preparar transição para Slide 3 (O Problema Real)                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 4.2 Diagrama de Timing Visual

```
SINCRONIZAÇÃO VISUAL - TIMELINE

00:00  00:02  00:03  00:04  00:05  00:06  00:08  00:09  00:12  00:35
│      │      │      │      │      │      │      │      │      │
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│      │      │      │      │      │      │      │      │      │
│  [SILÊNCIO] │      │      │      │      │      │      │      │
│      │      │      │      │      │      │      │      │      │
│      ├──────┤      │      │      │      │      │      │      │
│      │ TÍTULO      │      │      │      │      │      │      │
│      │ MUDA        │      │      │      │      │      │      │
│      │      ├──────┤      │      │      │      │      │      │
│      │      │ TERRENO     │      │      │      │      │      │
│      │      │ APARECE     │      │      │      │      │      │
│      │      │      ├──────────────┤      │      │      │      │
│      │      │      │ ESTRADA               │      │      │      │
│      │      │      │ DESENHA               │      │      │      │
│      │      │      │      ├──────┤      │      │      │      │
│      │      │      │      │ LINHA         │      │      │      │
│      │      │      │      │ TRANSFORMA    │      │      │      │
│      │      │      │      │      ├──────────────┤      │      │
│      │      │      │      │      │ LABELS +    │      │      │
│      │      │      │      │      │ PONTOS      │      │      │
│      │      │      │      │      │      ├──────┤      │      │
│      │      │      │      │      │      │ TEXTO │      │      │
│      │      │      │      │      │      │ FINAL │      │      │
│      │      │      │      │      │      │      ├───────┼──────┤
│      │      │      │      │      │      │      │ HOLD          │

NARRAÇÃO:
"Exceto... no mundo real.
 A rota ideal não é a menor distância geométrica.
 [pausa]
 A rota ideal é o caminho mais curto entre o que é permitido.
 E guardem bem esse conceito.
 Ele explica absolutamente todas as decisões de engenharia
 que tomamos no nosso projeto."
```

---

# 5. CHECKLIST DE INTEGRAÇÃO COM SLIDE 1

## 5.1 Pré-Produção (Antes de Criar o Slide)

### Checklist de Coesão

| # | Item | Status | Observações |
|---|------|--------|-------------|
| ☐ | Posição Ponto 1 verificada | | X: 25%, Y: 50% |
| ☐ | Posição Ponto 2 verificada | | X: 75%, Y: 50% |
| ☐ | Diâmetro dos pontos igual ao Slide 1 | | 24px |
| ☐ | Cores dos pontos idênticas | | Azul #0C326F, Dourado #D4AF37 |
| ☐ | Efeito Magic Move/Morph testado | | Transição suave entre slides |
| ☐ | Tempo de transição definido | | 0.5s |

### Checklist Visual

| # | Item | Status | Observações |
|---|------|--------|-------------|
| ☐ | Paleta de cores aprovada | | Manter consistência TCU |
| ☐ | Tipografia igual ao Slide 1 | | SF Pro Display |
| ☐ | Estilo de sombras consistente | | Drop-shadow suave |
| ☐ | Background não conflita | | Transição sutil branco → cinza claro |

## 5.2 Durante a Produção

### Verificação de Elementos

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHECKLIST DE PRODUÇÃO - SLIDE 2                          │
└─────────────────────────────────────────────────────────────────────────────┘

ELEMENTOS HERDADOS (devem ser idênticos ao Slide 1)
☐ Ponto Azul - posição exata (25%, 50%)
☐ Ponto Dourado - posição exata (75%, 50%)
☐ Cor Azul - #0C326F
☐ Cor Dourada - #D4AF37
☐ Diâmetro - 24px
☐ Sombras - mesmos parâmetros

ELEMENTOS TRANSFORMADOS
☐ Linha reta - mesma posição, novo estilo (tracejada)
☐ Título - mesma tipografia, novo texto
☐ Fundo - transição sutil de cor

ELEMENTOS NOVOS
☐ Terreno topográfico - curvas de nível em #E2E8F0
☐ Estrada sinuosa - caminho em #0C326F
☐ Labels - textos "GUARDRAILS", "RESTRIÇÕES", "REGRAS"
☐ Animações configuradas na ordem correta
```

## 5.3 Pós-Produção (Antes da Apresentação)

### Testes Finais

| # | Teste | Status | Notas |
|---|-------|--------|-------|
| ☐ | Transição Slide 1 → 2 em modo apresentação | | Verificar fluidez |
| ☐ | Timing das animações no hardware real | | Projetor pode afetar |
| ☐ | Cores reproduzem corretamente | | Testar no projetor real |
| ☐ | Animação da estrada desenha corretamente | | Stroke path funcionando |
| ☐ | Pontos não "saltam" na transição | | Verificar alinhamento pixel-perfect |
| ☐ | Narração sincroniza com visual | | Ensaiar 3x |
| ☐ | Backup: exportar vídeo da transição | | Caso falhe o live |

### Validação de Consistência Espacial

```
┌─────────────────────────────────────────────────────────────────────────────┐
│         VALIDAÇÃO DE CONSISTÊNCIA ESPACIAL                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Slide 1 (Origem)                          Slide 2 (Destino)                │
│  ┌─────────────────────┐                   ┌─────────────────────┐          │
│  │                     │                   │    ~~~~~~~~~~~~~~~  │ ← Terreno│
│  │                     │                   │   /               \ │          │
│  │    ●═══════════●    │   ────────→       │  ●≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈●  │ ← Pontos │
│  │   P1         P2     │   Magic Move      │   \               / │  idênticos│
│  │                     │                   │    ~~~~~~~~~~~~~~~  │          │
│  └─────────────────────┘                   └─────────────────────┘          │
│                                                                             │
│  VERIFICAÇÃO:                                                               │
│  ☐ P1: (25%, 50%) → (25%, 50%) ✓ MATCH                                     │
│  ☐ P2: (75%, 50%) → (75%, 50%) ✓ MATCH                                     │
│                                                                             │
│  SE HOUVER DESVIO:                                                          │
│  • Reajustar posição no Slide 2                                             │
│  • NUNCA ajustar Slide 1 (já aprovado)                                      │
│  • Verificar unidades (px vs % vs pt)                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 6. PROMPTS PARA GERAÇÃO DE IMAGENS

## 6.1 Prompt Base - Cena Completa do Slide 2

```
Minimalist corporate presentation slide design, two solid circles perfectly 
aligned horizontally - left circle deep blue #0C326F, right circle gold #D4AF37, 
connected by TWO paths: (1) a faint dashed straight line in gray, and 
(2) a prominent winding curving road in deep blue that snakes around obstacles. 
Top-down view with subtle topographic contour lines in light gray #E2E8F0 
on white background. The winding road represents the "real path" while the 
dashed line represents the "ideal but impossible" straight line. 
Apple Keynote style, clean vector illustration, professional corporate aesthetic, 
4K quality, 16:9 aspect ratio, pure white background with soft gray topographic 
elements, no photorealistic textures, flat design aesthetic.
```

## 6.2 Prompt - Elementos Separados

### Apenas o Terreno Topográfico
```
Minimalist topographic map background for presentation slide, subtle contour 
lines in light gray #E2E8F0 on pure white #FFFFFF background, gentle curves 
suggesting terrain elevation, Apple Keynote style, clean vector lines, 
no text, no other elements, transparent-ready areas for overlay, 
4K quality, 16:9 aspect ratio.
```

### Apenas a Estrada Sinuosa
```
Minimalist winding road illustration for presentation slide, single elegant 
blue #0C326F curved line connecting left side to right side with smooth 
S-curves, top-down view, pure white background, Apple Keynote style, 
vector illustration, clean stroke weight 4px, no other elements, 
transparent background, 4K quality, 16:9 aspect ratio.
```

### Labels/Ícones de Guardrails
```
Minimalist text labels "GUARDRAILS", "RESTRICTIONS", "RULES" in clean 
sans-serif font, dark gray #4A5568, positioned along a curved path, 
Apple Keynote style, clean typography, transparent background, 
suitable for overlay on presentation slide, 4K quality.
```

---

# 7. NOTAS TÉCNICAS PARA IMPLEMENTAÇÃO

## 7.1 Keynote (macOS)

```
CONFIGURAÇÃO NO KEYNOTE

1. TRANSITION (entre Slide 1 e 2)
   • Tipo: Magic Move
   • Duração: 0.5s
   • Aceleração: Automática
   • Nota: Os pontos devem ter exatamente o mesmo nome de objeto

2. ANIMAÇÕES BUILD-IN (Slide 2)
   • Terreno: Fade + Scale (0.8s, ease-out)
   • Estrada: Line Draw (1.2s, ease-in-out)
   • Labels: Fade + Move (0.5s, stagger 0.2s)
   • Linha transforma: Não é animação de build, é estado final

3. ORDEM DE CAMADAS
   • Z-order deve ser configurado no painel Arrange
   • Pontos sempre no topo (Front)
   • Terreno sempre no fundo (Back)
```

## 7.2 PowerPoint (Windows)

```
CONFIGURAÇÃO NO POWERPOINT

1. TRANSIÇÃO (entre Slide 1 e 2)
   • Tipo: Transformar (Morph)
   • Duração: 0.5s
   • Nota: Usar Selection Pane para nomear objetos igualmente

2. ANIMAÇÕES (Slide 2)
   • Terreno: Aparecer + Escala vertical
   • Estrada: Riscar (Wipe) com direção personalizada
   • Labels: Surgir + Subir
   • Linha: N/A (estado final herdado)

3. SELECTION PANE (importante!)
   • Renomear objetos com !! no início
   • Ex: "!!PontoAzul", "!!PontoDourado"
   • Isso garante que o Morph reconheça os objetos
```

## 7.3 Implementação em Código (HTML/CSS/JS)

```css
/* ESPECIFICAÇÕES CSS PARA SLIDE 2 */

/* Pontos - HERDADOS do Slide 1 */
.ponto-azul {
  position: absolute;
  left: 25%;
  top: 50%;
  width: 24px;
  height: 24px;
  background: #0C326F;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 4px 20px rgba(12, 50, 111, 0.3);
  z-index: 50;
}

.ponto-dourado {
  position: absolute;
  left: 75%;
  top: 50%;
  width: 24px;
  height: 24px;
  background: #D4AF37;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 4px 20px rgba(212, 175, 55, 0.3);
  z-index: 50;
}

/* Linha Tracejada - TRANSFORMAÇÃO */
.linha-re {
  position: absolute;
  left: 25%;
  top: 50%;
  width: 50%;
  height: 2px;
  border-top: 2px dashed #4A5568;
  opacity: 0.5;
  z-index: 40;
}

/* Estrada - NOVO */
.estrada {
  position: absolute;
  stroke: #0C326F;
  stroke-width: 4px;
  fill: none;
  z-index: 30;
  /* Path SVG com curvas */
}

/* Terreno - NOVO */
.terreno {
  position: absolute;
  z-index: 20;
  opacity: 0;
  transform-origin: bottom;
  animation: terrenoAparece 0.8s ease-out forwards;
}

@keyframes terrenoAparece {
  from {
    opacity: 0;
    transform: scaleY(0);
  }
  to {
    opacity: 1;
    transform: scaleY(1);
  }
}
```

---

# 8. ROTEIRO DE ENSAIO

## Checklist Pré-Apresentação

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ROTEIRO DE ENSAIO - SLIDE 2                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

FASE 1: PREPARAÇÃO (30 min antes)
☐ Abrir apresentação no hardware de apresentação
☐ Testar transição Slide 1 → 2
☐ Verificar se pontos não saltam
☐ Confirmar cores no projetor
☐ Preparar clicker/controle remoto

FASE 2: ENSAIO DE NARRAÇÃO (10 min)
☐ Praticar: "Exceto... no mundo real."
☐ Pausa dramática de 1 segundo após "Exceto..."
☐ Sincronizar gesto com aparecimento da estrada
☐ Ênfase em "o que é permitido"
☐ Finalização forte: "...todas as decisões de engenharia."

FASE 3: ENSAIO TÉCNICO (10 min)
☐ Timing das animações
☐ Backup preparado (vídeo estático)
☐ Transição para Slide 3 fluida

FASE 4: CHECKLIST FINAL (5 min antes)
☐ Slide 2 carregado corretamente
☐ Todas as animações funcionando
☐ Narração memorizada
☐ Respirar. Você está pronto.
```

---

# 9. RESUMO EXECUTIVO PARA O ORQUESTRADOR

## Checklist de Entregáveis

| Entregável | Status | Responsável |
|------------|--------|-------------|
| Cronograma segundo a segundo | ✅ | Orquestrador |
| Mapa de transição Slide 1→2 | ✅ | Orquestrador |
| Especificações de coordenadas | ✅ | Orquestrador |
| Cores exatas validadas | ✅ | Orquestrador |
| Mapa de sincronização fala/visual | ✅ | Orquestrador |
| Prompts para imagens | ✅ | Orquestrador |
| Checklist de integração | ✅ | Orquestrador |
| Instruções técnicas (Keynote/PPT) | ✅ | Orquestrador |

## Pontos Críticos de Sucesso

```
╔══════════════════════════════════════════════════════════════════════════════╗
║              PONTOS CRÍTICOS - SLIDE 2                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

1. COORDENADAS DOS PONTOS
   → Devem ser IDÊNTICAS ao Slide 1 (25%, 50%) e (75%, 50%)
   → Tolerância: ±2 pixels

2. TRANSIÇÃO MAGIC MOVE/MORPH
   → Duração: 0.5s
   → Deve parecer que o slide "evoluiu", não trocou

3. SINCRONIZAÇÃO FALA/VISUAL
   → "Exceto..." = início da transformação
   → Pausa após "distância geométrica" = plateia processa
   → "o que é permitido" = labels aparecem

4. IMPACTO PSICOLÓGICO
   → Slide 2 é a QUEBRA DE EXPECTATIVA
   → A metáfora da estrada explica toda a apresentação
   → Tempo suficiente para o conceito assentar
```

---

**Documento criado por:** AGENTE ORQUESTRADOR  
**Data:** 21 de Fevereiro de 2026  
**Versão:** 1.0 - Pronto para Produção  
**Status:** ✅ COMPLETO

---

*"A rota ideal é o caminho mais curto entre o que é permitido."*
