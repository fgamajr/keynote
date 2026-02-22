#!/usr/bin/env python3
"""
Script para gerar imagens da apresentação usando a API do Gemini (Google Imagen).

Uso:
    python generate_images.py
    
Requisitos:
    - GEMINI_API_KEY configurada no arquivo .env (na pasta pai)
    - Biblioteca google-generativeai instalada
    
Instalação:
    pip install google-generativeai python-dotenv
"""

import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env na pasta pai
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Verificar se a API key está configurada (opcional - usamos apenas para TXT)
API_KEY = os.getenv('GEMINI_API_KEY')
if API_KEY:
    print("🔧 GEMINI_API_KEY encontrada. Modo API disponível.")
else:
    print("⚠️  GEMINI_API_KEY não encontrada. Executando em modo TXT apenas.")
    print("   (Os prompts serão salvos para uso manual no Midjourney/DALL-E)")

# Mapeamento de slides para seus prompts
SLIDES_PROMPTS = {
    "SLIDE_0": {
        "titulo": "Abertura Pessoal - Globo com Cuiabá",
        "prompts": [
            {
                "nome": "globo_terrestre",
                "prompt": "Minimalist 3D globe showing Earth from space, Apple Keynote presentation style. Full Earth view, centered on South America. Clean, photorealistic but stylized rendering. Soft atmospheric glow around the planet. Subtle grid lines suggesting latitude/longitude. Brazil clearly visible, highlighted subtly. Background: Deep space gradient (dark blue to black). Style: Elegant, cinematic, professional. No text, no labels, no UI elements. High quality, suitable for presentation opening. 4K, 16:9."
            },
            {
                "nome": "zoom_america_sul",
                "prompt": "Minimalist map highlight of South America with focus on Cuiabá, Brazil, Apple Keynote style. South American continent in elegant blue tones (#0C326F at 60% opacity). Brazil highlighted with slightly stronger color. Cuiabá, Mato Grosso marked with glowing dot (#D4AF37 gold glow). Subtle pulsing effect suggested around Cuiabá. Clean vector-style map, not photorealistic. Surrounding countries in lighter shade. Style: Clean, institutional, geographic precision. No text labels, no clutter. Dark slate gradient background. 4K, 16:9."
            },
            {
                "nome": "transicao_escuro",
                "prompt": "Minimalist transition element - globe fading to darkness, Apple Keynote style. Bottom half: Earth/South America fading into darkness. Top half: Dark space with single point of light (suggesting transition to Slide 1). Gradient from light (bottom) to dark (top). Style: Cinematic, atmospheric, suggesting 'zoom into abstraction'. Clean edges for transition effect. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_1": {
        "titulo": "Dois Pontos - Linha Reta",
        "prompts": [
            {
                "nome": "dois_pontos_linha",
                "prompt": "Two simple dark graphite dots on a pure white background, perfectly horizontally aligned, connected by a perfect, thin, straight black line. Minimalist, geometric, presentation slide asset. Clean pure white background. Apple Keynote style. No shadows, no gradients, flat design. 4K, 16:9."
            },
            {
                "nome": "apenas_dois_pontos",
                "prompt": "Two solid dark graphite circles perfectly aligned horizontally on pure white background, isolated dots with no connecting line. Minimalist, geometric shapes. Apple Keynote style. Clean geometric shapes. Professional corporate aesthetic. Centered composition. Vector-like crisp edges. 4K, 16:9. Flat design, no shadows."
            },
            {
                "nome": "apenas_linha",
                "prompt": "Single thin horizontal straight black line centered on pure white background, isolated line element for animation. Apple Keynote style. Clean geometric stroke. Professional corporate aesthetic. Perfectly horizontal orientation. Vector-like crisp edges. 2px stroke weight. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_2": {
        "titulo": "A Estrada - Caminho Real",
        "prompts": [
            {
                "nome": "estrada_topo",
                "prompt": "Top-down view of a winding mountain road crossing topographical lines. The road curves elegantly around invisible obstacles. Overlaying the road is a faint, dashed straight line connecting a starting dot to an ending dot. Super clean, Apple-style illustration. Colors: soft grays, minimal blue accents for the winding road, pure white background. 4K, 16:9."
            },
            {
                "nome": "apenas_estrada",
                "prompt": "Isolated winding road element for animation overlay. Elegant S-curve road in warm earth tones (#8B7355 for pavement), starting from left and ending at right. Road width: consistent medium width, smooth curves flowing naturally. Clean edges suitable for masking/layering. Pure white background. 4K, 16:9."
            },
            {
                "nome": "terreno_paisagem",
                "prompt": "Subtle landscape terrain background. Rolling hills: soft undulating forms in muted sage green (#9CAF88) and warm taupe (#BCAAA4). Low mountains: gentle silhouettes in background, dusty blue-gray (#B0BEC5). Horizon line: positioned below vertical center. Empty space at center: clear pathway area. No roads, no paths visible. Soft gradient sky from pale blue (#E8F4F8) at top to warm cream (#F5F1E8) near horizon. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_3": {
        "titulo": "O Planeta - Restrição Real",
        "prompts": [
            {
                "nome": "globo_wireframe",
                "prompt": "Minimalist 3D wireframe globe on a clean dark slate background. A subtle highlight on central-west Brazil and another on Amsterdam. A glowing blue curved line wraps beautifully around the surface connecting the two dots. A red, straight dashed line pierces directly through the solid center of the sphere. Elegant, educational, scientific visualization presentation asset. Dark slate (#1A1A2E) background. 4K, 16:9."
            },
            {
                "nome": "globo_elemento",
                "prompt": "Minimalist 3D wireframe globe isolated on dark background, Apple Keynote style. Semi-transparent Earth sphere with clean geometric grid lines. Grid color: Deep blue (#0C326F) at 30% opacity. Subtle internal glow, soft lighting. No surface textures, no clouds, no political borders. Clean vector-like 3D rendering. Dark slate gradient background. 4K, 16:9."
            },
            {
                "nome": "linha_vermelha",
                "prompt": "Straight dashed line piercing through a sphere. Reddish-orange color (#E57373), glowing effect. Line passes through center of frame at angle (Brazil left-bottom to Amsterdam right-top). Dashed pattern: consistent medium dashes. Glow effect: soft red halo around the line. Transparent background. 4K, 16:9."
            },
            {
                "nome": "arco_azul",
                "prompt": "Elegant curved arc path around a sphere. Bright cyan color (#4FC3F7), glowing effect. Arc follows natural curvature from left-bottom to right-top. Solid line with soft outer glow. Width: medium, elegant stroke. Represents flight path or surface route. Transparent background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_4": {
        "titulo": "O Problema - 11 Milhões",
        "prompts": [
            {
                "nome": "visualizacao_escala",
                "prompt": "Minimalist abstract visualization of massive data scale, Apple Keynote presentation style. Clean institutional white to very light gray gradient background. Abstract representation of millions of data points. Visual metaphor: Thousands of tiny document icons or data nodes flowing in organized streams. Flow pattern: From left (input) to right (processing). Density: High density in center-left, gradually filtering toward right. Color scheme: Deep blue (#0C326F) for primary data flow, subtle gold (#D4AF37) accents. Ultra-clean, vector-precision, flowing lines. No text, no labels. 4K, 16:9."
            },
            {
                "nome": "icones_documentos",
                "prompt": "Minimalist document icon set for presentation, Apple style. Multiple document/page icons in isometric or flat perspective. Icons representing: ID cards, land titles, certificates, forms. Clean line art style, consistent stroke weight. Color: Outline in #0C326F, subtle fill in #E2E8F0. Arranged in gentle cascade or flow pattern. Transparent background. 4K, 16:9."
            },
            {
                "nome": "dois_auditores",
                "prompt": "Minimalist silhouette representation of two professionals/auditors. Two elegant human silhouettes, side by side. Style: Abstract, not realistic, almost icon-like. Scale: Small relative to overall composition. Color: Dark gray (#1A202C) or muted TCU blue (#0C326F at 60%). Subtle, symbolic. Transparent background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_5": {
        "titulo": "A Solução - Código como Protocolo",
        "prompts": [
            {
                "nome": "conceito_protocolo",
                "prompt": "Minimalist abstract visualization of formalized rules and protocols, Apple Keynote presentation style. Clean institutional white background. Abstract representation of structured frameworks. Visual elements: Geometric 'document' shapes suggesting formal protocols, structured grid lines implying rules and criteria. Flow from unstructured (left) to structured (right). Left side: Slightly chaotic, abstract document forms. Right side: Organized, framed document blocks. Connecting element: Subtle flowing lines suggesting AI processing. Color scheme: Deep blue (#0C326F) for structure, subtle gold (#D4AF37) for highlights. Ultra-clean, vector-precision. 4K, 16:9."
            },
            {
                "nome": "protocolo_vs_programacao",
                "prompt": "Minimalist icon set contrasting traditional programming vs formal protocols, Apple style. LEFT SIDE (NÃO É PROGRAMAÇÃO): Traditional code symbols: </> brackets, { } braces, # hashtags. Style: Technical, monospace aesthetic. Color: Muted gray (#9E9E9E). Arrangement: Scattered, less structured. RIGHT SIDE (É PROTOCOLO): Formal document symbols: Checkmarks, seals, scales of justice, clipboards. Style: Institutional, professional. Color: Deep blue (#0C326F). Arrangement: Organized, structured. Transparent background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_6": {
        "titulo": "Arquitetura - Três Camadas",
        "prompts": [
            {
                "nome": "tres_camadas",
                "prompt": "Minimalist architectural diagram showing three-layer control system, Apple Keynote presentation style. Three horizontal layers stacked vertically, connected by flowing arrows. Layer 1 (top): Soft, cloud-like shape representing AI interpretation — cyan/blue glow (#4FC3F7), fluid edges. Layer 2 (middle): Geometric, structured framework representing validation — TCU blue (#0C326F), rigid grid pattern. Layer 3 (bottom): Solid, golden foundation representing decision — gold (#D4AF37), authoritative block. Connecting elements: Arrows flowing from top to bottom. Background: Clean institutional white. Style: Ultra-clean, vector-precision, architectural blueprint aesthetic. 4K, 16:9."
            },
            {
                "nome": "fluxo_dados",
                "prompt": "Minimalist data flow icons for three-layer architecture, Apple style. Document icon (input): Representing unstructured documents entering the system. Processing icon (middle): Gears or validation marks. Output icon (end): Checkmarked decision or sealed document. Flow arrows connecting the three. Color progression: Cyan (#4FC3F7) → Blue (#0C326F) → Gold (#D4AF37). Clean line art. Transparent background. 4K, 16:9."
            },
            {
                "nome": "guardrails",
                "prompt": "Minimalist representation of guardrails constraining AI, Apple Keynote style. Central element: Soft, glowing, semi-transparent cyan sphere (AI reasoning). Surrounding structure: Elegant metallic or geometric framework 'containing' the sphere. Framework color: TCU blue (#0C326F). Visual metaphor: The AI is not 'caged' but 'guided' — the framework channels its energy. Style: Refined, architectural, not prison-like. Clean lines, professional aesthetic. Transparent background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_7": {
        "titulo": "Demonstração - Fluxo Real",
        "prompts": [
            {
                "nome": "interface_sistema",
                "prompt": "Minimalist UI mockup of an audit processing system, Apple Keynote presentation style. Clean interface layout showing document processing workflow. Left side: Document thumbnail/input area (neutral gray). Center: Data extraction fields showing extracted information (cyan highlights #4FC3F7). Right side: Validation checklist and final decision (gold highlight #D4AF37 for approved). Style: Ultra-clean, modern dashboard aesthetic. Colors: White background, TCU blue (#0C326F) for structure, cyan for AI elements, gold for decisions. No text, no labels. 4K, 16:9."
            },
            {
                "nome": "documento_processando",
                "prompt": "Minimalist illustration of a document being processed by AI, Apple style. Document icon (paper/page) on left side. Flowing lines or particles moving from document to right. Middle zone: Abstract representation of data extraction (floating text fields). Right side: Checkmark or decision indicator. Color flow: Gray (document) → Cyan (processing) → Blue (validation) → Gold (decision). Clean vector-like style. Transparent background. 4K, 16:9."
            },
            {
                "nome": "status_icons",
                "prompt": "Minimalist status icon set for audit system, Apple style. Checkmark icon (validation passed) - green/blue. Alert icon (needs review) - yellow/amber. Decision seal/icon (final approval) - gold with authority feel. Processing/spinner icon (AI working) - cyan. All icons consistent style: clean line art, rounded corners. Transparent background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_8": {
        "titulo": "Conclusão - Mic Drop",
        "prompts": [
            {
                "nome": "jornada_completa",
                "prompt": "Minimalist visual summary of journey from straight line to controlled path, Apple Keynote presentation style. Top: Faint representation of the two dots and straight line (ghosted, 20% opacity). Middle: The winding road (40% opacity). Bottom: Abstract representation of the three-layer architecture (structured, solid). Progression suggests evolution from simple to complex, from uncontrolled to controlled. Color flow: Gray (abstract past) → Blue (structure) → Gold (resolution). Style: Ultra-minimalist, memory-evoking, elegant synthesis. No text. 4K, 16:9."
            },
            {
                "nome": "guardrails_final",
                "prompt": "Minimalist representation of guardrails enabling safe progress, Apple Keynote style. Central path: Elegant curved road or flowing line suggesting progress. Side elements: Subtle, refined guardrail structures (not prison bars, but elegant constraints). The path is clear, directed, safe because of the guardrails. Colors: TCU blue (#0C326F) for structure, gold (#D4AF37) for the path. Style: Architectural, refined, symbolizing 'controlled freedom'. Clean institutional white background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_9": {
        "titulo": "MCP - IA Dentro do Banco",
        "prompts": [
            {
                "nome": "arquitetura_mcp",
                "prompt": "Minimalist technical architecture diagram showing secure AI deployment, Apple Keynote style. Bottom: Solid, heavy cylindrical database icon (PostgreSQL) in graphite gray (#4A5568). Above/Inside: Glowing cyan AI brain/core (#4FC3F7) positioned WITHIN the database perimeter. Connection: High-tech glowing locking mechanism connecting AI to database. Shield elements: Soft red shield icons indicating 'Read-Only Enforcement'. Background: Clean off-white (#F7FAFC). Style: Ultra-clean, engineering aesthetic, InfraSec feel. No text. 4K, 16:9."
            },
            {
                "nome": "inversao_fluxo",
                "prompt": "Minimalist arrows showing flow inversion, Apple Keynote style. Top arrow (faded, grayed out): Pointing OUT from database (representing old insecure model). Bottom arrow (bright, cyan): Pointing IN to database (representing MCP secure model). Visual metaphor: Data staying put, AI coming in. Clean vector style. Transparent background. 4K, 16:9."
            },
            {
                "nome": "cadeado_readonly",
                "prompt": "Minimalist security lock icon for read-only database access, Apple style. Database cylinder with lock overlay. 'READ ONLY' implied through visual design. Cyan/blue glow indicating active security. Clean, professional icon. Transparent background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_10": {
        "titulo": "6 Abordagens Cognitivas",
        "prompts": [
            {
                "nome": "grid_seis_abordagens",
                "prompt": "A highly polished 3x2 grid of crisp, rounded rectangular glassmorphism cards on a pure white background. Each card signifies a distinct technological capability with miniature elegant icons: 1) a stylized camera lens for computer vision, 2) a SQL code snippet box, 3) a Gaussian bell curve graph for statistics, 4) database reverse engineering nodes, 5) stacked document pages for reports, 6) a certified wax-seal badge for validation. Professional, slate gray and muted warm tones, Apple Keynote tech aesthetic. Each card has subtle depth and shadow. Clean typography space. 4K, 16:9."
            },
            {
                "nome": "icones_seis",
                "prompt": "Minimalist icon set representing 6 cognitive capabilities, Apple style: 1) Camera/eye icon for Computer Vision, 2) Code brackets with SQL symbol, 3) Bell curve/statistical graph, 4) Database schema diagram, 5) Document stack with seal, 6) Shield with checkmark for validation. Consistent line art style, rounded corners, professional tech aesthetic. Colors: slate gray (#4A5568) with accents in cyan (#4FC3F7) and gold (#D4AF37). Transparent background. 4K."
            }
        ]
    },
    
    "SLIDE_11": {
        "titulo": "Zero Kelvin Tests",
        "prompts": [
            {
                "nome": "diagrama_invariantes",
                "prompt": "A highly polished, minimalist flowchart depicting exact mathematical preservation. A sequence of pristine white glowing rectangular cards linked by straight, unbending arrows. Inside each card, the identical number '3,175,345' is printed in rigid perfect monospace font, highlighted in deep slate and freezing cold icy blue. A subtle lock or solid state crystal icon indicating invulnerability to change. Apple Keynote data purity aesthetic, pure white background, glistening ice crystal texture subtly suggested. 4K, 16:9."
            },
            {
                "nome": "cristal_congelamento",
                "prompt": "Minimalist representation of mathematical invariance as ice crystals. A number frozen in a perfect ice crystal structure, unchanging and solid. Cold blue tones (#4FC3F7, #0C326F), crystalline geometric patterns. Suggests absolute zero, no molecular movement, complete preservation. Apple Keynote style, elegant scientific visualization. 4K, 16:9."
            },
            {
                "nome": "termometro_zero",
                "prompt": "Minimalist thermometer graphic showing 'Zero Kelvin' temperature. Gauge at absolute zero, with indicator in icy blue. Clean medical/scientific instrument aesthetic. Numbers frozen at zero. Apple Keynote style, pure white background. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_12": {
        "titulo": "Idempotência",
        "prompts": [
            {
                "nome": "terminal_camadas",
                "prompt": "A presentation layout divided into two thematic sides. On the left, a sleek, beautifully angled dark-mode terminal window showing lines of Python code and a glowing output: 'Result: Idempotent. 16,501 Records Verified.' On the right, a stacked pillar of 5 clean, slightly overlapping horizontal rectangles in soft muted colors (sand, slate, pale green) representing 'Anti-Hallucination Layers'. At the bottom, a minimalist equation with small elegant icons (a seed bag, a group of people, a calendar) summing up to a pure mathematical certainty. Off-white background, Apple Keynote style. 4K, 16:9."
            },
            {
                "nome": "icone_semente",
                "prompt": "Minimalist icon representing 'deterministic seed' concept. A seed packet or DNA helix symbol combined with a mathematical sigma symbol. Suggests reproducibility and fixed starting point. Colors: green (#48BB78) and blue (#0C326F). Clean line art, Apple style. Transparent background. 4K."
            }
        ]
    },
    
    "SLIDE_13": {
        "titulo": "Demo ao Vivo",
        "prompts": [
            {
                "nome": "fluxo_isometrico",
                "prompt": "A clean, minimalist isometric assembly-line flow. On the left: messy, tilted, chaotic document folder icons in red/orange tones. In the middle: a rigid, sleek gray metallic square box containing a glowing cyan AI core (the constrained AI). On the right: perfectly stacked, structured, grid-aligned folders in green with checkmarks. Isometric top-down view, highly polished, vector art style conveying automated systemic pipeline. Pure white background. Apple Keynote style. 4K, 16:9."
            },
            {
                "nome": "icones_estado",
                "prompt": "Minimalist icon set for document processing states: 1) Chaotic document (red, tilted, messy lines), 2) Processing machine (gray, with cyan glow center), 3) Organized document (green, neat, checkmarked). Consistent isometric style, Apple Keynote aesthetic. Colors: red (#C53030), cyan (#4FC3F7), green (#48BB78). Transparent background. 4K."
            },
            {
                "nome": "terminal_snapshot",
                "prompt": "Minimalist dark terminal window showing processing logs. Dark background (#1A1A2E), cyan text (#4FC3F7). Lines showing: 'Processing document 1,247...', 'Validation: PASSED', 'Output: audit_report_001.md'. Clean monospace font. Small window, corner presentation. Apple Keynote style. 4K."
            }
        ]
    },
    
    "SLIDE_14": {
        "titulo": "Papéis de Trabalho",
        "prompts": [
            {
                "nome": "fluxo_yaml_latex",
                "prompt": "A highly polished system architecture flowchart. Starting from a simple code icon on the left (YAML Configuration), branching outward horizontally into a complex but neat vertical tree of rounded rectangular blocks labeled as test phases (using soft olive greens and muted salmon/orange tones representing distinct AI robustness tests). Arrows elegantly trace the processing flow from left to right, all converging into a formal structured document icon ('LaTeX Report Final Audit Trail'). Apple Keynote flow style, clean engineering corporate aesthetic, off-white background. 4K, 16:9."
            },
            {
                "nome": "icone_latex",
                "prompt": "Minimalist icon representing formal academic document. Stacked papers with mathematical formulas visible, academic seal/stamp overlay. Color: Gold (#D4AF37) and slate gray (#4A5568). Suggests official report, LaTeX formatting, academic rigor. Apple Keynote style. Transparent background. 4K."
            }
        ]
    },
    
    "SLIDE_15": {
        "titulo": "Os 4 Achados",
        "prompts": [
            {
                "nome": "grid_impacto",
                "prompt": "Four elegant glassmorphism and solid information cards evenly distributed in a 2x2 flawless symmetrical grid on a very bright, soft off-white background. Each rectangular card contains a bold, dominating typography showing huge percentage statistics (27.1%, 45.92%, 90.62%, 94.1%) indicating dramatic errors, accompanied by minimal corporate icons (a stacked document, geospatial map pin, email envelope, empty code brackets). Aesthetic is pure corporate data dashboard, using rich coffee brown, slate gray colors, with red accents for critical issues. Conveying grave systemic discoveries with surgical precision. Pure Apple presentation vibe. 4K, 16:9."
            },
            {
                "nome": "icones_alerta",
                "prompt": "Minimalist warning/alert icon set for audit findings: 1) Document with warning triangle (27%), 2) Map pin with error circle (45%), 3) Email with skull/X mark (90% - deceased), 4) Broken code brackets (94% metadata failure). Colors: Red (#C53030) for critical, Orange (#ED8936) for high. Clean line art. Apple style. Transparent background. 4K."
            }
        ]
    },
    
    "SLIDE_16": {
        "titulo": "Novo Perfil do Auditor",
        "prompts": [
            {
                "nome": "novo_perfil",
                "prompt": "A clean, minimalist presentation slide balancing human and metric elements. On the left side, an elegant vertical list with subtle beautiful icons (a terminal prompt, a speech bubble, an orbit node, a gear) defining the human's new roles: Coder, Interpreter, Orchestrator, Engineer. On the right side, a very simple, sleek bar chart comparing a towering muted-orange bar labeled '~10 months' with a dramatically shorter soft-sage-green bar labeled '~2 months'. A glassmorphism tooltip floats above the empty space indicating 'Reinvested in Analytical Depth'. Pure white background, calm and inspiring corporate tech aesthetic. 4K, 16:9."
            },
            {
                "nome": "icones_evolucao",
                "prompt": "Minimalist icon set representing career evolution: 1) Terminal/code icon (YAML Coder), 2) Brain/understanding icon (Interpreter), 3) Conductor baton/orbit icon (Orchestrator), 4) Gear/engine icon (Engineer). Colors: Deep blue (#0C326F) and gold (#D4AF37) for prestige. Apple Keynote style. Transparent background. 4K."
            }
        ]
    },
    
    "SLIDE_17": {
        "titulo": "O Legado",
        "prompts": [
            {
                "nome": "dashboard_tres_colunas",
                "prompt": "A masterfully organized 3-column executive summary dashboard on a pure white background. Left column: Glassmorphism cards highlighting massive numeric impacts like 'R$ 51 Billion' and '210+ Memos'. Center column: A wide, elegant frosted-glass panel listing 'Impossible Feats' with tiny, sharp minimalist icons next to bullet points (3.7M records analyzed, 12.8M CPFs crossed). Right column: A sleek vertical roadmap with subtle arrows pointing to future milestones like 'Academic Publication (RTCU)' and 'YAML Template'. A very subtle, out-of-focus background hint of modern IDE code editor. Extremely polished Apple Keynote finale aesthetic. 4K, 16:9."
            }
        ]
    },
    
    "SLIDE_18": {
        "titulo": "Mic Drop Final",
        "prompts": [
            {
                "nome": "background_tipografia",
                "prompt": "Pure solid color background for typography presentation. Option 1: Pure white (#FFFFFF) with charcoal text. Option 2: Deep space black (#0D0D1A) with white text. No images, no icons, no decorations. Absolute minimalism for maximum impact. 4K, 16:9."
            }
        ]
    }
}


def criar_pasta_saida():
    """Cria a pasta de saída para as imagens."""
    pasta = Path(__file__).parent / 'nanobanana'
    pasta.mkdir(exist_ok=True)
    print(f"📁 Pasta de saída: {pasta.absolute()}")
    return pasta


def salvar_prompt_txt(prompt, nome_arquivo, pasta_saida):
    """Salva o prompt em um arquivo TXT para geração manual."""
    caminho = pasta_saida / f"{nome_arquivo}_PROMPT.txt"
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(prompt)
    return caminho


def main():
    """Função principal."""
    print("=" * 60)
    print("🎨 GERADOR DE IMAGENS - APRESENTAÇÃO TCU")
    print("=" * 60)
    print()
    
    # Criar pasta de saída
    pasta_saida = criar_pasta_saida()
    
    print("💡 MODO: Salvando prompts em TXT para geração manual")
    print("   Você pode usar esses prompts no:")
    print("   • Midjourney (Discord): /imagine [prompt]")
    print("   • DALL-E 3 (ChatGPT): Cole o prompt")
    print("   • Leonardo.ai: Cole o prompt")
    print()
    
    contador = 0
    
    # Processar cada slide
    for slide_id, slide_info in SLIDES_PROMPTS.items():
        print(f"\n📑 {slide_id}: {slide_info['titulo']}")
        
        # Criar subpasta para o slide
        pasta_slide = pasta_saida / slide_id.lower()
        pasta_slide.mkdir(exist_ok=True)
        
        for prompt_info in slide_info['prompts']:
            nome = f"{slide_id.lower()}_{prompt_info['nome']}"
            prompt = prompt_info['prompt']
            
            # Salvar em TXT
            caminho_txt = salvar_prompt_txt(prompt, nome, pasta_slide)
            print(f"  📝 {caminho_txt.name}")
            contador += 1
    
    print()
    print("=" * 60)
    print(f"✅ CONCLUÍDO! {contador} prompts salvos.")
    print(f"📁 Local: {pasta_saida.absolute()}")
    print()
    print("🚀 PRÓXIMOS PASSOS:")
    print("  1. Acesse a pasta 'KEYNOTE/nanobanana'")
    print("  2. Cada slide tem sua própria subpasta")
    print("  3. Use os arquivos _PROMPT.txt nos serviços de IA")
    print()
    print("💡 DICA: Os prompts estão em inglês para melhor resultado")
    print("   nos geradores de imagem (Midjourney, DALL-E, etc.)")
    print()


if __name__ == "__main__":
    main()
