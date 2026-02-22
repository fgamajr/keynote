# SLIDE 6: A ARQUITETURA (Como Fizemos Isso)
## Documento Mestre - Auditoria como Código (TCU)
**Data:** 22 de Fevereiro de 2026  
**Projeto:** Keynote Executiva - 10 minutos

---

## 📋 RESUMO EXECUTIVO

O SLIDE 6 é o **MOMENTO DE REVELAÇÃO TÉCNICA** da apresentação. Após estabelecer o conceito de "código como protocolo" (Slide 5), agora mostramos a arquitetura real: como a IA foi contida, validada e transformada em ferramenta de auditoria confiável. Este slide conecta a metáfora da "estrada" (Slides 1-2) com a implementação prática.

**Função narrativa:** Demonstrar que "guardrails" não são abstratos — são componentes técnicos específicos  
**Duração total:** ~50-55 segundos  
**Tom:** Técnico sem ser hermético, didático sem ser condescendente  
**Impacto esperado:** O público visualiza exatamente como o sistema funciona e por que é confiável

---

## 🎭 AGENTE 1: NARRADOR (Texto Falado)

### Roteiro Completo

> *"Então, como fizemos?"*
> 
> *[PAUSA — deixa a pergunta pairar]*
> 
> *"Nós removemos a liberdade da IA em vez de adicionar inteligência a ela."*
> 
> *[GESTO: "removendo" com as mãos]*
> 
> *"A IA não toma decisões de auditoria. Ela apenas propõe interpretações."*
> 
> *[PAUSA]*
> 
> *"O sistema funciona em três camadas."*
> 
> *[GESTO: três dedos]*
> 
> *"Primeiro: a IA lê e interpreta os documentos — identifica nomes, datas, propriedades, renda."*
> 
> *[PAUSA]*
> 
> *"Segundo: um validador programático verifica se os dados fazem sentido — datas consistentes, valores dentro de limites legais, documentos completos."*
> 
> *[PAUSA]*
> 
> *"Terceiro: apenas então, se tudo estiver correto, a decisão de auditoria é registrada com trilha completa."*
> 
> *[APROXIMAÇÃO]*
> 
> *"A IA pode sugerir. Mas apenas o protocolo aprovado pode concluir."*

### Direção de Performance Detalhada

| Momento | Ação | Expressão/Voz | Notas |
|---------|------|---------------|-------|
| "Como fizemos?" | Mãos abertas, questionando | Curioso, envolvente | Convidativo |
| "removemos a liberdade" | Gesto de "cortar" | Firme, decisivo | Conceito-chave |
| "três camadas" | Três dedos erguidos | Didático, claro | Estrutura visual |
| "Primeiro..." | Aponta para slide | Explicativo | IA como leitora |
| "Segundo..." | Aponta abaixo | Explicativo | Validação programática |
| "Terceiro..." | Aponta final | Explicativo | Decisão com trilha |
| "A IA pode sugerir" | Voz mais baixa | Conclusiva | Mic drop técnico |

**Tempo estimado:** 50-55 segundos

---

## 📝 AGENTE 2: CONTEÚDO VISUAL ESCRITO (Texto no Slide)

### Elementos de Texto

#### TÍTULO PRINCIPAL
```
A Arquitetura: Três Camadas de Controle
```

#### CAMADA 1 — INTERPRETAÇÃO (IA)
```
📄 CAMADA 1: INTERPRETAÇÃO (IA)
   → Lê documentos não estruturados
   → Extrai: nomes, datas, propriedades, renda
   → Sugere interpretações preliminares
   ⚠️ NÃO decide — apenas propõe
```

#### CAMADA 2 — VALIDAÇÃO (Código)
```
⚙️ CAMADA 2: VALIDAÇÃO PROGRAMÁTICA
   → Verifica consistência dos dados
   → Confirma limites legais
   → Valida completude documental
   ✓ Gatekeeper: só passa o válido
```

#### CAMADA 3 — DECISÃO (Protocolo)
```
✓ CAMADA 3: DECISÃO DE AUDITORIA
   → Aplica critérios formais do TCU
   → Registra decisão com justificativa
   → Gera trilha de auditoria completa
   ✓ Apenas o protocolo aprovado decide
```

#### FRASE DE FECHAMENTO
```
A IA sugere.
O Protocolo decide.
```

### Sequência de Aparição

| Elemento | Momento | Efeito | Duração |
|----------|---------|--------|---------|
| Título | 0s | Fade in | 0.6s |
| "Como fizemos?" aparece | 1s | Fade in | 0.5s |
| Camada 1 (IA) | 3s | Slide in from left | 0.8s |
| Seta/fluxo 1→2 | 5s | Draw line | 0.4s |
| Camada 2 (Validação) | 5.5s | Slide in from left | 0.8s |
| Seta/fluxo 2→3 | 8s | Draw line | 0.4s |
| Camada 3 (Decisão) | 8.5s | Slide in from left | 0.8s |
| Frase final | 11s | Fade in + emphasis | 0.8s |

### Especificações Tipográficas

```
TÍTULO PRINCIPAL:
- Fonte: SF Pro Display Bold
- Tamanho: 42px
- Cor: #0C326F (Azul TCU)

CAMADA 1 (IA):
- Fonte: SF Pro Text
- Tamanho: 20px
- Cor: #4FC3F7 (Ciano - representa fluidez/interpretação)
- Fundo: Card com borda ciano sutil

CAMADA 2 (Validação):
- Fonte: SF Pro Text
- Tamanho: 20px
- Cor: #0C326F (Azul TCU)
- Fundo: Card com borda azul

CAMADA 3 (Decisão):
- Fonte: SF Pro Text
- Tamanho: 20px
- Cor: #D4AF37 (Dourado TCU)
- Fundo: Card com borda dourada

FRASE FINAL:
- Fonte: SF Pro Display Heavy
- Tamanho: 32px
- Cor: #0C326F (primeira linha) / #D4AF37 (segunda linha)
```

---

## 🎨 AGENTE 3: NANOBANANA (Prompts de Imagem)

### Imagem Principal - Representação da Arquitetura em Camadas

**Prompt A - Visualização das Três Camadas (Diagrama):**
```
Minimalist architectural diagram showing three-layer control system, Apple Keynote presentation style.

COMPOSITION:
- Three horizontal layers stacked vertically, connected by flowing arrows
- Layer 1 (top): Soft, cloud-like shape representing AI interpretation — cyan/blue glow (#4FC3F7), fluid edges
- Layer 2 (middle): Geometric, structured framework representing validation — TCU blue (#0C326F), rigid grid pattern
- Layer 3 (bottom): Solid, golden foundation representing decision — gold (#D4AF37), authoritative block
- Connecting elements: Arrows flowing from top to bottom, suggesting data pipeline
- Background: Clean institutional white (#FFFFFF) to light gray (#F7FAFC)
- Style: Ultra-clean, vector-precision, architectural blueprint aesthetic
- Visual metaphor: Fluid becomes structured becomes authoritative
- No text, no labels, no cluttered details
- Abstract representation of "guardrails in action"

TECHNICAL:
- Aspect ratio: 16:9
- Resolution: 4K
- Mood: Technical, trustworthy, layered security
- Negative space: Generous, professional
```

**Prompt B - Ícones de Fluxo de Dados (Elementos Separados):**
```
Minimalist data flow icons for three-layer architecture, Apple style.

COMPOSITION:
- Document icon (input): Representing unstructured documents entering the system
- Processing icon (middle): Gears or validation marks
- Output icon (end): Checkmarked decision or sealed document
- Flow arrows connecting the three
- Color progression: Cyan (#4FC3F7) → Blue (#0C326F) → Gold (#D4AF37)
- Style: Clean line art, consistent stroke weight

BACKGROUND: Transparent (PNG alpha)

STYLE: Clean vector icons, corporate architectural aesthetic, 4K quality
```

**Prompt C - Representação de "Guardrails" (Metáfora Visual):**
```
Minimalist representation of guardrails constraining AI, Apple Keynote style.

COMPOSITION:
- Central element: Soft glowing sphere (AI) in cyan (#4FC3F7)
- Surrounding structure: Elegant metallic or geometric framework "containing" the sphere
- Framework color: TCU blue (#0C326F)
- Visual metaphor: The AI is not "caged" but "guided" — the framework channels its energy
- Style: Refined, architectural, not prison-like
- Clean lines, professional aesthetic

BACKGROUND: Transparent or very light institutional

STYLE: Ultra-minimalist conceptual art, Apple Keynote aesthetic, suitable for overlay
```

### Especificações Técnicas

| Parâmetro | Valor |
|-----------|-------|
| Resolução | 3840 x 2160 (4K) |
| Aspect Ratio | 16:9 |
| Formato | PNG |
| Cor IA/Interpretação | #4FC3F7 (Ciano) |
| Cor Validação | #0C326F (Azul TCU) |
| Cor Decisão | #D4AF37 (Dourado TCU) |
| Fundo | #FFFFFF → #F7FAFC |

---

## 🎬 AGENTE 4: MODELO VISUAL E STORYTELLING

### Conceito Visual

**Estilo:** Diagrama arquitetônico elegante; "blueprint" de sistema de auditoria  
**Referências:** Diagramas de arquitetura de software (AWS, Azure), fluxogramas jurídicos, infográficos técnicos  
**Mood:** Transparente, técnico, construtivo — "nada escondido"

### Paleta de Cores

```
CORES DAS CAMADAS:
├── Camada 1 (IA):           #4FC3F7 (Ciano) — fluidez, interpretação
├── Camada 2 (Validação):    #0C326F (Azul TCU) — estrutura, regras
├── Camada 3 (Decisão):      #D4AF37 (Dourado TCU) — autoridade, conclusão
│
CORES DE SUPORTE:
├── Fundo:                   #FFFFFF → #F7FAFC
├── Texto principal:         #1A202C
├── Texto secundário:        #4A5568
│
EFEITOS:
├── Sombra cards:            rgba(0, 0, 0, 0.08)
├── Glow camada 1:           rgba(79, 195, 247, 0.2)
├── Borda camada 2:          rgba(12, 50, 111, 0.3)
└── Borda camada 3:          rgba(212, 175, 55, 0.4)
```

### Layout do Slide

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│         A Arquitetura: Três Camadas de Controle            │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 📄 CAMADA 1: INTERPRETAÇÃO (IA)                     │   │
│  │    → Lê documentos não estruturados                 │   │
│  │    → Extrai: nomes, datas, propriedades, renda      │   │
│  │    ⚠️ NÃO decide — apenas propõe                    │   │
│  │                     [cor: ciano #4FC3F7]            │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ⚙️ CAMADA 2: VALIDAÇÃO PROGRAMÁTICA                 │   │
│  │    → Verifica consistência dos dados                │   │
│  │    → Confirma limites legais                        │   │
│  │    → Valida completude documental                   │   │
│  │                     [cor: azul TCU #0C326F]         │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ✓ CAMADA 3: DECISÃO DE AUDITORIA                    │   │
│  │    → Aplica critérios formais do TCU                │   │
│  │    → Registra decisão com justificativa             │   │
│  │    → Gera trilha de auditoria completa              │   │
│  │                     [cor: dourado #D4AF37]          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│              "A IA sugere. O Protocolo decide."            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Storyboard Frame-a-Frame

#### FRAME 0: Transição (0.0s - 1.0s)
- Fundo mantém do Slide 5
- Título aparece: "A Arquitetura: Três Camadas de Controle"

#### FRAME 1: A Pergunta (1.0s - 2.5s)
- "Como fizemos?" aparece subtilmente
- Narração introduz o conceito de "remover liberdade"

#### FRAME 2: Camada 1 - IA (3.0s - 5.0s)
- Card da Camada 1 desliza da esquerda
- Cor ciano (#4FC3F7) — fluidez, interpretação
- Destaque: "NÃO decide — apenas propõe"

#### FRAME 3: Fluxo 1→2 (5.0s - 5.5s)
- Seta desenha-se conectando as camadas
- Sugere pipeline de dados

#### FRAME 4: Camada 2 - Validação (5.5s - 8.0s)
- Card da Camada 2 desliza da esquerda
- Cor azul TCU (#0C326F) — estrutura, regras
- Destaque: "Gatekeeper: só passa o válido"

#### FRAME 5: Fluxo 2→3 (8.0s - 8.5s)
- Segunda seta desenha-se
- Continuidade do fluxo

#### FRAME 6: Camada 3 - Decisão (8.5s - 11.0s)
- Card da Camada 3 desliza da esquerda
- Cor dourada (#D4AF37) — autoridade, decisão
- Destaque: "Apenas o protocolo aprovado decide"

#### FRAME 7: Frase Final (11.0s+)
- "A IA sugere. O Protocolo decide."
- Cores diferenciadas (ciano + dourado)
- Prepara para Slide 7 (demonstração ou resultados)

---

## ⚙️ AGENTE 5: ORQUESTRADOR DE TRANSIÇÕES

### Transição Slide 5 → Slide 6

**Tipo:** Continuidade visual mantida  
**Elemento de transição:** Do conceito abstrato ("código = protocolo") para implementação concreta ("três camadas")  
**Duração:** 0.5s (rápida, momentum técnico)

**Justificativa:** O Slide 5 estabeleceu o "o quê" (código como protocolo). O Slide 6 mostra o "como" (arquitetura em camadas). A transição deve ser fluida, como se estivéssemos "abrindo a caixa" para mostrar o mecanismo.

### Cronograma de Animações

```
00:00 - 00:01 │ Transição rápida mantendo fundo institucional
              │ Narração: "Então, como fizemos?"

00:01 - 00:03 │ Título aparece
              │ Narração: "Nós removemos a liberdade da IA..."

00:03 - 00:05 │ Camada 1 (IA) aparece
              │ Narração: "Primeiro: a IA lê e interpreta..."

00:05 - 00:06 │ Seta 1→2 desenha
              │ [Transição visual]

00:06 - 00:08 │ Camada 2 (Validação) aparece
              │ Narração: "Segundo: um validador programático verifica..."

00:08 - 00:09 │ Seta 2→3 desenha
              │ [Transição visual]

00:09 - 00:11 │ Camada 3 (Decisão) aparece
              │ Narração: "Terceiro: apenas então, a decisão é registrada..."

00:11 - 00:13 │ Frase final aparece
              │ Narração: "A IA pode sugerir. Mas apenas o protocolo aprovado pode concluir."
```

### Sincronização Crítica

| Fala | Elemento Visual | Ação |
|------|-----------------|------|
| "Primeiro..." | Camada 1 aparece | Apontar para card ciano |
| "Segundo..." | Camada 2 aparece | Apontar para card azul |
| "Terceiro..." | Camada 3 aparece | Apontar para card dourado |
| "A IA pode sugerir" | Frase final | Voz baixa, conclusiva |

---

## ✅ AGENTE 6: SUPERVISOR DE QUALIDADE

### Parecer Geral

**Status:** APROVADO PARA PRODUÇÃO  
**Nota Conceitual:** 9.5/10  
**Função:** Transparência técnica que gera confiança institucional

### Pontos Fortes

1. **Tríade clara:** Interpretação → Validação → Decisão — fluxo lógico irreversível
2. **Cores significativas:** Ciano (fluidez) → Azul (estrutura) → Dourado (autoridade)
3. **Negação explícita:** "NÃO decide — apenas propõe" — remove ambiguidade
4. **Frase de fechamento:** "A IA sugere. O Protocolo decide." — binômio perfeito

### Pontos de Atenção

| Risco | Mitigação |
|-------|-----------|
| Pode parecer "muito técnico" | Manter linguagem do roteiro acessível |
| Três camadas podem confundir | Narração lenta, pausas entre cada uma |
| Slide denso demais | Cards com espaçamento generoso |

### Recomendações

- **Pausas obrigatórias:** Entre cada camada, pausar 0.5s para visual assentar
- **Cores de destaque:** Ciano (#4FC3F7) para IA deve ser suficientemente diferente do azul TCU
- **Checklist mental:** "Leu? Validou? Decidiu?" — facilita memorização

---

## 🎵 AGENTE 7: DIRETOR DE SOM/AMBIENTE

### Recomendações Sonoras

**Música de Fundo:**
- Se houver trilha: Manter subida gradual durante apresentação das camadas
- Clímax na Camada 3 (Decisão)

**Efeitos Sonoros (Opcionais):**
- Som suave de "whoosh" quando cada camada aparece
- Som de "clique" ou "lock" quando a decisão é apresentada

**Pausas Sonoras:**
- Após cada camada: 0.3s de silêncio
- Após frase final: 1s de silêncio antes de próximo slide

---

## ♿ AGENTE 8: ESPECIALISTA EM ACESSIBILIDADE

### Requisitos de Acessibilidade

**Contraste:**
- Texto em ciano (#4FC3F7) sobre branco: Verificar contraste (pode precisar de contorno ou fundo)
- Texto em azul (#0C326F) e dourado (#D4AF37): Contraste adequado ✓

**Legibilidade:**
- Cards devem ter tamanho suficiente para leitura distante
- Setas de fluxo devem ser visíveis (mínimo 3px de espessura)

**Estrutura Visual:**
- Fluxo top-to-bottom claro
- Separação visual óbvia entre as três camadas
- Não depender apenas de cor para distinguir camadas (usar ícones/posição)

**Alternativas Verbais:**
- Narrador deve descrever cada camada explicitamente
- Repetir a sequência "Primeiro... Segundo... Terceiro..."

---

## 🛡️ AGENTE 9: GERENTE DE RISCO E BACKUP

### Riscos Identificados

| Risco | Probabilidade | Impacto | Plano B |
|-------|---------------|---------|---------|
| Cores das camadas não distinguíveis | Média | Médio | Adicionar números (1, 2, 3) além das cores |
| Slide parece "fluxograma de TI" | Baixa | Médio | Enfatizar que é "protocolo de auditoria", não "sistema de TI" |
| Três camadas confundem | Média | Alto | Resumir para duas: "IA lê, Protocolo decide" |
| Tempo excedido | Média | Médio | Versão curta: mostrar só os cards, não as setas |

### Plano de Contingência

**Se o público parecer perdido nas três camadas:**
- Simplificar: "Resumindo: a IA lê, o sistema valida, o protocolo decide. Três etapas, zero chance de a IA inventar."

**Se as cores não reproduzirem bem no projetor:**
- Versão backup com:
  - Camada 1: Fundo cinza claro + texto escuro
  - Camada 2: Fundo azul claro + texto escuro
  - Camada 3: Fundo amarelo claro + texto escuro

---

## 📊 AGENTE 10: ANALISTA DE MÉTRICAS E ENGAGEMENT

### Indicadores de Sucesso do Slide

**Engagement Esperado:**
- [ ] Acenos de compreensão na apresentação das camadas
- [ ] Pessoas anotando a sequência "Interpreta → Valida → Decide"
- [ ] Perguntas sobre "como funciona a validação" (indica interesse técnico)

**Métricas de Compreensão:**
- Perguntar após apresentação: "Quem faz a decisão final na arquitetura?"
- Resposta esperada: "O protocolo/validação, não a IA"

**Teste A/B Sugerido:**
- Versão A: Três camadas detalhadas
- Versão B: Duas camadas simplificadas (IA sugere → Protocolo decide)
- Medir qual gera mais confiança/compreensão

### Pontos de Verificação Pós-Apresentação

- O público entendeu a separação entre "interpretação" e "decisão"?
- A tríade de camadas ficou memorável?
- Há clareza sobre onde estão os "guardrails" (na validação)?

---

## 📎 ANEXOS

### Anexo A: Fluxo da Narrativa até o Slide 6

| Slide | Conceito | Transição para Slide 6 |
|-------|----------|------------------------|
| 5 | "A IA interpreta. O Código audita." (conceito) | → "Como fizemos isso na prática?" (implementação) |
| 6 | Três camadas de controle | → Demonstração ou resultados no Slide 7 |

### Anexo B: Resumo da Arquitetura (Para Perguntas)

```
PERGUNTA: "Como vocês garantem que a IA não erra?"
RESPOSTA: "A IA não decide. Ela apenas lê e sugere. Um validador programático 
verifica consistência e regras legais. Só então o protocolo de auditoria aprova 
ou rejeita, com trilha completa."

PERGUNTA: "E se a IA interpretar errado?"
RESPOSTA: "O validador captura inconsistências. E mesmo que passe, a decisão 
final é do protocolo, não da IA. Errar interpretação não significa errar a auditoria."
```

### Anexo C: Versão Curta (Emergência - 25s)

> "Nossa arquitetura tem três camadas: a IA lê os documentos, um validador verifica se os dados fazem sentido, e só então o protocolo de auditoria decide. A IA sugere, mas quem conclui é o código de auditoria."

---

**Documento Consolidado por:** Sistema Multi-Agente (10 Agentes)  
**Status:** ✅ **PRONTO PARA PRODUÇÃO**  
**Próximo Slide:** Slide 7 (Demonstração ou Resultados)

---

## 🚀 CHECKLIST DE PRODUÇÃO

- [ ] Gerar imagens no Nanobanana (Prompts Agente 3)
- [ ] Criar cards das três camadas com cores distintas
- [ ] Configurar animações de aparecimento sequencial
- [ ] Desenhar setas de fluxo entre as camadas
- [ ] Testar contraste das cores em projeção
- [ ] Praticar pausas entre "Primeiro... Segundo... Terceiro..."
- [ ] Preparar versão simplificada (2 camadas) como backup
- [ ] Verificar legibilidade do texto em cada card

**Prioridade Máxima:** Este slide é o "core" técnico da apresentação. A clareza da separação entre "IA interpreta" e "Protocolo decide" é o insight principal que o público deve levar para casa.
