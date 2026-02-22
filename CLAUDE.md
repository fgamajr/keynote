# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **scroll-driven interactive keynote presentation** for TCU (Tribunal de Contas da União — Brazil's Federal Court of Accounts). The presentation is titled **"Auditoria como Código"** (Audit as Code) and demonstrates how AI was applied to audit R$ 51 billion in government spending (CAF program).

The presentation has **19 scenes** (Slides 0–18) designed as a continuous scroll experience (not traditional slides), inspired by Apple Keynote aesthetics. Total scroll height: ~1900vh.

## Repository Structure

- **`SLIDE_X_MASTER_DOCUMENT.md`** — Master document for each scene (0–18). Each contains sections for 10 specialized "agents": Narrator script, Visual text, Nanobanana (image prompts), Visual model/storyboard, Transitions, Quality supervisor, Sound, Accessibility, Risk management, Metrics.
- **`SLIDE_2_MODELO_VISUAL_COMPLETO.md`** / **`SLIDE_2_ORQUESTRACAO_COMPLETA.md`** — Extended visual model and orchestration details for Scene 2.
- **`presentation_architecture.md`** — Core rendering architecture: scroll-as-timeline mechanics, scene types (Metaphorical/Evidential/Technical/Cinematic), state management, coordinate system, z-index layering.
- **`narrative.md`** — Detailed scene breakdown with motion behavior, implementation strategy, performance notes, and accessibility fallbacks for each scene.
- **`generate_images.py`** — Python script that saves AI image generation prompts as TXT files in `nanobanana/`. Requires `google-generativeai` and `python-dotenv`. Reads `GEMINI_API_KEY` from `../.env`.
- **`nanobanana/`** — Contains per-slide subdirectories with `_PROMPT.txt` files (English prompts for Midjourney/DALL-E/Leonardo) and generated PNG images.
- **`assets_inventory.md`** — Complete inventory of 47+ visual assets with specs (colors, sizes, formats) per scene.
- **`implementation_checklist.md`** — Phase-by-phase build checklist (foundation, scroll system, scenes, animations, assets, testing, deployment).
- **`speaker_script.md`** — Full speaker narration script in Portuguese with timing and stage directions.
- **`executive_presentation.md`** / **`executive_presentation1.md`** — Executive-facing documentation justifying the scroll-based format.

## Key Commands

```bash
# Generate image prompts (saves TXT files to nanobanana/)
python generate_images.py

# Install dependencies for generate_images.py
pip install google-generativeai python-dotenv
```

## Technical Architecture (Planned Web Implementation)

- **Framework**: React with TypeScript
- **Animation**: GSAP ScrollTrigger or Framer Motion (`useScroll`, `useTransform`)
- **Styling**: Tailwind CSS + CSS Modules for scroll-driven animations
- **Graphics**: SVG with stroke-dasharray animations, CSS transforms (GPU-accelerated)
- **Scene states**: Each scene has three scroll-driven phases: `entrance` (0–33%), `settled` (33–66%), `exit` (66–100%)
- **Performance**: Only animate `transform` and `opacity` (no layout thrashing). Use `will-change: transform` sparingly. `backdrop-filter: blur` requires `@supports` fallback for weak hardware.

## Color Palette (TCU Institutional)

| Token | Hex | Usage |
|-------|-----|-------|
| TCU Blue | `#0C326F` | Primary structural elements |
| TCU Gold | `#D4AF37` | Decisions, highlights, Cuiabá marker |
| Cyan | `#4FC3F7` | AI/processing elements |
| Cosmic Black | `#0D0D1A` | Dark backgrounds |
| Dark Slate | `#1A1A2E` | Scene 3/terminal backgrounds |
| Critical Red | `#C53030` | Errors, alerts |
| Alert Orange | `#ED8936` | Warnings |
| Off-White | `#F7FAFC` | Light backgrounds |

## Scene Narrative Arc

- **Act 1 (Scenes 0–3)**: Metaphorical — personal intro, "shortest path" metaphor, physical constraints
- **Act 2 (Scenes 4–8)**: Evidential — institutional scale (R$ 51B, 11M documents), solution architecture, demo, intermediate conclusion
- **Act 3 (Scenes 9–14)**: Technical — MCP/database security, 6 cognitive approaches, zero-kelvin tests, idempotency, live demo, work papers
- **Act 4 (Scenes 15–17)**: Impact — 4 critical findings (27%–94% error rates), new auditor profile, legacy dashboard
- **Act 5 (Scene 18)**: Cinematic conclusion — typography only, no animation

## Language

This is an **international presentation**. All content — slide text, speaker script, documentation, and image prompts — must be written in **English**. Note: existing files may still contain Portuguese from earlier drafts; these should be translated to English when modified.
