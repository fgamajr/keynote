# 1. Experience Model

A apresentação não utiliza o conceito de "slides", mas de um palco contínuo (viewport) onde elementos entram, ancoram-se (pinning) e transformam-se guiados exclusivamente pelo cursor de rolagem (scroll trigger). O scroll atua como a *timeline* de uma timeline de vídeo.
*   **A Câmera**: O Viewport atua como uma lente fixa. O usuário rola a página fisicamente, mas a sensação é de afundar na narrativa (Z-axis zoom) ou de elementos deslizarem para o quadro sob controle absoluto.
*   **Foco Cognitivo**: Picos de atenção são geridos por manipulação de opacidade e proporção espacial. Apenas um argumento lógico ou métrica vital habita a tela em um dado momento. O resto recua para as sombras ou sofre desfoque (*blur*).
*   **Tempo e Espaço**: A altura da tela (`vh`) é a nossa moeda de tempo. Seções complexas ganham `300vh` ou `400vh` para permitir que o usuário controle a animação quadro-a-quadro de forma lenta, sentindo a magnitude dos números ou da engenharia.

# 2. Rendering Architecture

A arquitetura dependerá de uma árvore DOM fixa com camadas absolutas/estáticas, controladas por estado derivado de scroll.
*   **Orquestração de Eventos**: Framer Motion (`useScroll` e `useTransform` em React) ou GSAP ScrollTrigger. Isso garante performance e vinculação determinística de propriedades CSS ao scroll progressivo `[0, 1]`.
*   **Composição de Layout**: Fortemente escorada em `position: sticky` em contêineres irmãos, empilhados verticalmente.
*   **Estilização**: Tailwind CSS para estruturação responsiva; CSS Module/Inline progressivo via JavaScript para chaves de animação iterativa (`scale`, `translate3d`, `opacity`, `filter: blur()`).
*   **Renderização Gráfica**: Predominância de CSS Transform acelerado por hardware (GPU) e gráficos vetoriais SVG (*stroke drawing*). Nenhum processamento complexo em *main thread* (layout thrashing) durante a rolagem.

---

# 3. Scene Breakdown

# Act 1: The Paradigm Shift

## Scene 1: The Euclidean Illusion

### Scroll Segment: 0% → 100% (0vh - 200vh)

*   **Narrative goal**: Quebrar a intuição de que o caminho da Inteligência Artificial em direção à automação de um problema é uma linha reta.
*   **Visual behavior**: Dois pontos minimalistas flutuam na tela. Uma reta perfeita conecta-os. Ao rolar, a reta subitamente se quebra/distorce, e um mapa topográfico surge atrás, transformando a reta numa "estrada" real com curvas forçadas.
*   **Motion behavior**: `Draw path` via `stroke-dasharray` para a linha. A linha reta é estilhaçada por morphing no SVG path do React, curvando-se abruptamente, enquanto a opacidade do mapa de fundo sobe (`0` para `1`).
*   **Text behavior**: Frase 1 ("O caminho mais curto...") em *sticky* no centro, substituída num fade cruzado brusco pela Frase 2 ("...é inviável sem as regras.") quando o mapa revela as restrições de terreno.
*   **Implementation strategy**: Camada `<svg>` absoluta controlada via Framer Motion `pathLength`. O fundo é carregado preventivamente em WebP e surge com alteração de `opacity` interpolada num `useTransform(scrollYProgress, [0.4, 0.6], [0, 1])`.
*   **Performance notes**: O morphing de paths complexos demanda CPU. Manter as curvas da estrada SVG otimizadas (abaixo de 100 âncoras).
*   **Accessibility fallback**: Se houver preferência por movimento reduzido (`prefers-reduced-motion`), o SVG não é desenhado ativamente; os dois estados (Reta e Estrada) se alternam com transição instantânea durante a rolagem. 

## Scene 2: The Physical Constraint

### Scroll Segment: 0% → 100% (200vh - 350vh)

*   **Narrative goal**: Fixar a ideia de que a Física (as restrições programáticas) não são limitadores, mas as forças que permitem a máquina "orbitar" com consistência, sem se perder no vácuo.
*   **Visual behavior**: A topografia diminui, converte-se numa curva que modela um globo terrestre (O Planeta) no vazio do espaço (Dark Mode progressivo).
*   **Motion behavior**: Zoom-out da topografia gerando distorção circular (CSS `border-radius` transition acoplada com `scale(0.1)`). Transição de paleta off-white global para fundo escuro (`background-color` morfa do Slate Gray Light para Cosmic Black).
*   **Text behavior**: O texto surge debaixo da atmosfera: "A gravidade não é uma prisão. É o que define a órbita previsível."
*   **Implementation strategy**: A transição de cores de fundo deve ocorrer numa *div wrapper* global. Uso de Tailwind dinâmico nos classes baseados na progressão do scroll state para aplicar "dark mode" inverso no bloco de scroll.
*   **Performance notes**: Alterar o background global no meio do scroll dispara um paint pesado ocasional. Fazer cross-fade de dois wrappers `fixed` `w-screen h-screen` com opacidades invertidas performa melhor, pois usa aceleração de opacidade ao invés de repaint de reflow de CSS rules.
*   **Accessibility fallback**: Texto lido diretamente como Parágrafo Subsequente em screen-readers. Fundo escuro fixo para alto-contraste em Fallback sem scroll longo.

---

# Act 2: Institutional Scale

## Scene 3: The 51 Billion Scope

### Scroll Segment: 0% → 100% (350vh - 600vh)

*   **Narrative goal**: Esmagar o espectador conceitualmente com as quantidades financeiras e documentais envolvidas no Tribunal. Apresentar o problema na escala natural do mundo real.
*   **Visual behavior**: Início de cena apresenta o número massivo: R$ 51 Bilhões. Na rolagem, esse *Card* se choca ou se divide em três outros cards colossais. Ao rolar adiante, os cards se multiplicam de forma exponencial e hiper-rápida simulando a avalanche burocrática dos "11 Milhões de Documentos".
*   **Motion behavior**: O efeito deve causar "claustrofobia burocrática". Cards se empilhando vindos do z-axis em direções randômicas. `transform: translate3d()` e `rotate` gerando desordem paramétrica. Após isso, eles perdem o foco (`blur`) sumindo para trás (Z-index scale-out).
*   **Text behavior**: O título trava (sticky) à direita, enquanto os "card visuals" operam à esquerda, rolando livremente (padrão 50vw/50vw split-screen de grid da Apple).
*   **Implementation strategy**: Grid layout com colunas não-tradicionais. Elementos de documentos criados em iteração `Array(50)`. Para orquestrar o stack caótico no React, utilize `scrollYProgress` mapeando índices com um pouco de *parallax* progressivo em CSS Transforms `y`, para que os fundos rolem mais devagar.
*   **Performance notes**: Risco severo de Layout Thrashing aqui, pois serão dúzias de DOM nodes sobrepostos. Dica de arquitetura de alta performance: Promover cada "documento em vôo" a um CSS `will-change: transform`. Não anime topo/left. Somente `transform` tridimensional com `translateZ` nulos.
*   **Accessibility fallback**: Lista de texto com dados estáticos e sem parallax (redução a CSS normal block).

---

# Act 3: Constraining the Machine

## Scene 4: The Vault (MCP Integration)

### Scroll Segment: 0% → 100% (600vh - 800vh)

*   **Narrative goal**: Mitigar preocupações de segurança governamental exibindo a IA trabalhando isolada dentro de um cofre Read-Only (Não vaza dados).
*   **Visual behavior**: Retorna tudo ao fundo bege-silício minimalista e suave (Off-white Keynote). Ícone metálico em peso vetorizado de um Banco de Dados PostgreSQL gigante na base. De cima, um "cérebro sintético" desliza. Cofres ou contornos de barricada se fecham entre eles.
*   **Motion behavior**: Interação física tangível e firme. O cérebro "acopla" com solidez (um ressalto mecânico animado usando Spring Physics do Framer Motion ao invés de um easing linear vago). A Barricada desliza fechando da direita e esquerda (`translateX`).
*   **Text behavior**: "A IA foi introduzida no banco. O banco trancou as saídas de insert." Opacidade síncrona.
*   **Implementation strategy**: GSAP Tween com `ScrollTrigger` amarrado. `ease: "elastic.out(1, 0.5)"` reproduzido ao atingir ponto crítico de cruzamento do scroll map, acoplado rigidamente ao `progress()` do trigger-head. Isso entrega fisicalidade.
*   **Performance notes**: Super limpo (poucos elementos vetoriais). Risco nulo no Paint.
*   **Accessibility fallback**: Alternar SVGs simples descritivos: Ícone Banco + Cérebro -> Troca para versão Unificada e "Trancada".

## Scene 5: Zero Kelvin (The Incorruptible Logic)

### Scroll Segment: 0% → 100% (800vh - 1000vh)

*   **Narrative goal**: Mostrar a certeza matemática e a completa impossibilidade orgânica sistêmica da IA inventar números fictícios nos relatórios finais.
*   **Visual behavior**: Começa centrado em uma pequena tela cinza e áspera exibindo o query number original em monoespaçado: `3,175,345`. Cor azul gelo ou chumbo escuro denso. Conforme rola, esse mesmo número viaja por três caixas (PT-01, PT-02, Output), sendo rigorosamente 'carimbado' no lugar, com flashes progressivos indicando exatidão exata (Zero calor orgânico/Zero kelvin variation).
*   **Motion behavior**: O Scroll congela e ativa um slider horizontal falso (*fake horizontal scroll*). O número `3,175,345` viaja no eixo X como num cano de vidro à esquerda até esbarrar no bloco da ponta direita. É imutável, e bate forte na parede final.
*   **Text behavior**: Título congela à esquerda da tela (Sticky position 100vh); a direita faz o deslizamento lateral como calha industrial exibindo a sequência da pipeline de controle da fraude lógica.
*   **Implementation strategy**: Usar contenção horizontal (X-Scroll Hook) amarrado à variação vertical *Y*. Ou seja, wrapper contêiner fixo ocupa 100vw, transformamos o progresso percentual Y num translate lateral (-X%) num Flex container dos *nodes* do Fluxograma.
*   **Performance notes**: Cuidado especial nas rolagens em touchscreens de celular. Overscroll lateral horizontal nativo do SO pode conflitar com transições horizontais *scroll-jacking*. Deve-se travar `overflow-x: hidden` explicitamente no `.container-root`.
*   **Accessibility fallback**: As caixas e gráficos empilham em vertical clássica ignorando o scroll tracking horizontal. A timeline de passos fica apenas `<ol>` com formatação semântica nativa para Screen Reader sem navegação confusa em 2D de viewport.

---

# Act 4: Determinism & Truth

## Scene 6: The Idempotent Execution

### Scroll Segment: 0% → 100% (1000vh - 1200vh)

*   **Narrative goal**: Provar que o "Robot Estagiário", orquestrado através do paradigma de 'Semente (seed) e Camadas', tem atestado exato determinístico comprovado por máquina em execução real.
*   **Visual behavior**: Elevação de um grande terminal *Dark Mode* contendo o layout autêntico de VSCode da palestra estressada de logs processados. Simultaneamente, caixas "vidro escovado verde macio", as "5 Camadas Anti-Alucinações", surgem empilhadas milimetricamente ao lado.
*   **Motion behavior**: Um movimento vertical lento (*Parallax pesado*). As camadas anti-alucinação empilham-se individualmente, colidindo delicadamente a cada tranco de pixel da rodinha do mouse (`scroll translateY offset`), unindo finalmente o terminal de logs com os módulos teóricos e com a equação `x+y=z`.
*   **Text behavior**: "Mesma semente. Mesma População. Mesmo Achado." Aparece como um adesivo final no layout final que não se move mais.
*   **Implementation strategy**: Camadas independentes CSS `grid` com diferentes `scroll parallax speeds` (`data-speed="1.2"`, etc). Assim a janela do VSCode rola num ritmo mais suave que a velocidade imposta nas "camadas-placas", até estancarem.
*   **Performance notes**: Muitas janelas grandes podem invocar Paint Repaint complexo. O vidro escovado (backdrop-filter: blur) nos cards de camadas podem triturar frames-per-second numa máquina antiga quando movidos verticais. Se prever PCs fracos de executivos, remover o uso do filtro pesado de backdrop via fallback `@supports`.
*   **Accessibility fallback**: Animação de velocidade normal, cortando todos os efeitos de sobreposição (z-index zero natural document flow). O terminal e o gráfico tornam-se figuras `<figure>`. 

## Scene 7: Coroando o Trabalho

### Scroll Segment: 0% → 100% (1200vh - 1400vh)

*   **Narrative goal**: Entregar os 4 Resultados gigantes como uma pancada frontal dos escândalos encontrados. É onde a diretoria percebe o retorno financeiro absurdo de adoção de Audit As Code (AAC).
*   **Visual behavior**: Quatro grandíssimos cartões percentuais saltando brutalmente perante a cena 2x2. "45.92% Erro", "90.62% Inválido", acompanhados de silhuetas opacas.
*   **Motion behavior**: Num único movimento contínuo do usuário de arrasto (*Swipe/Scroll down max speed*), os quatro números contam de zero rapidamente para os números brutais (Contador digital acionado de 0% -> 90.62%) explodindo seus frames *outwards*.
*   **Text behavior**: Impacto estatístico dominante em Negrito brutal.
*   **Implementation strategy**: *Counter Animation React Component* com prop acionada baseada via um Booleano do Hook `useInView`. Assim que o viewport atingir a coordenada deste Act, deflagrar `setCount` internamente interpolando a string format. O Card Base cresce suave do scale 0.9 -> 1 via framer variants.
*   **Performance notes**: Componentes rodando setState num array interval em alta velocidade trituram reacts batch renders. Usar o hook interno otimizado `useSpring` da framer-motion ou renderizar diretamente no `useRef.current.textContent` sem acionar um React lifecycle-re-render para rodar o velocímetro na casa dos decimais das estatísticas.
*   **Accessibility fallback**: Contagem progressiva estática pulada — número total carrega instantâneo na tela nativa.

---

# Act 5: The Legacy

## Scene 8: The Auditor Profile & Conclusion Dashboard

### Scroll Segment: 0% → 100% (1400vh - 1650vh)

*   **Narrative goal**: Fechar com um selo calmo, consolador ao servidor público (não vão roubar nosso emprego), e consolidando tudo na diretoria gerencial de prestação de contas dos R$ 51 Bilhões auditados pela inovação.
*   **Visual behavior**: Transição limpa e etérea, em tom suave de Off-White claro. Apresenta o Gráfico de 10 meses retraindo velozmente e macio para 2 meses. O texto enumera as 4 instâncias da revolução mental de orquestração humana. As estatísticas e R$ 51 bilhões reaparecem em blocos limpos, consolidando um painel gerencial da diretoria à direita em cascata lenta e fluida, compondo com o "Future Roadmap: Padrão YAML do TCU".
*   **Motion behavior**: Altíssimo refino no polimento do layout. Tudo já se apoia calmo em estática de tela, exceto a diminuição da Barra de Trabalho Braçal. A cor vai acalmando e os cards emergem (scale In 0.95 -> 1.0) via *opacity staggering*.
*   **Text behavior**: Subtítulo brilha como encarregado e comandante analítico do seu próprio robô.
*   **Implementation strategy**: Scroll position atinge 1500vh, e um `intersectionObserver` libera animações finais não travadas por scroll contínuo e progressivo — agora a cena opera como uma "revelação de página padrão", mas em altíssima qualidade transitória.
*   **Performance notes**: Sem risco extra de render. Painel de resumo calmo.
*   **Accessibility fallback**: Tela limpa com texto semântico e listas CSS cruas. Leitura natural e sequencial dos prêmios alcançados e ROADMAPS prometidos ao fim.

## Scene 9: Deep Silence / Mic-Drop (The Pure Core)

### Scroll Segment: 0% → 100% (1650vh - 1800vh)

*   **Narrative goal**: Gravar permanentemente a filosofia mestra nas mentes de cada participante como uma citação monolítica em um museu de arte. Encerrar de forma colossal sem ruídos técnicos.
*   **Visual behavior**: Rolagem exaustiva vai empurrando todo o dashboard para cima, deixando apenas a vacuidade absoluta do branco puro no ViewPort global. Literalmente deserto. A fonte e uma frase pesada surge muito lentamente no exato centro geométrico: **"A IA decide o que faz sentido. A nossa engenharia decide o que é permitido."** Nada em excesso.
*   **Motion behavior**: Um movimento mínimo (*drifting text up*) e alteração sutil num brilho de tipografia, enquanto tudo recai na quietude (`opacity` lentamente surgindo e preenchendo 100% enquanto as demais imagens das seções passíveis saem do dom node tree unmounted).
*   **Text behavior**: Frase colossal. Fio fino brilhante sutil de sublinha acompanha embaixo.
*   **Implementation strategy**: Pura manipulação de alpha de *font-color*. Efeito `clip-path` numa linha dourada de baixo desenhando (*Line draw in width: 0->100%*). `position: fixed` contêiner full viewport overlay com z-index brutal que intercepta e mascara todas as instabilidades de layout, finalizando a página no pé absoluto do footer vertical final do browser window scrollbar limits.
*   **Performance notes**: Totalmente otimizada (apenas o texto vector fonts pintando a última GPU layer draw-call).
*   **Accessibility fallback**: Lê-se como o parágrafo derradeiro com `<h1>` e sumários de ARIA tag roles. Tudo se encerra no parágrafo text level conclusivo sem poluições. Fim visual e Fim semântico orgânicos.
