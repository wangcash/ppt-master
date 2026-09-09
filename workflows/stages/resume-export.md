---
description: Main-pipeline control stage for exporting a validated SVG preview to PPTX after the user clicks "生成 PPT 文件".
---

# Resume Export Stage

> Generate-PPTX control stage for the second half of two-phase delivery:
> the project already completed Step 6 (Default) or §3 (Quick) — SVG preview
> ready and final checker passed. The user has now clicked 「生成 PPT 文件」
> or explicitly asked to export PPTX. This stage only runs Step 7 /
> Quick §4 export; it never regenerates or modifies SVGs.

## When to Run

The user names a project with export intent — “生成 PPT 文件”, “导出 PPTX”,
“下载 PPT”, or the host button in the PPT preview panel — and the project
already has a validated SVG preview.

**Prerequisite**: `svg_output/` non-empty and the matching final quality
report exists (`validation/svg_quality_report.json` for Quick, or the Default
final report). Missing state stops this stage with a prompt to finish the
preview first.

---

## Step 1: Sanity check

Verify in `<project_path>`:

| File / Directory | Required | Recovery when missing |
|---|---|---|
| `svg_output/` | Non-empty, every slide present | Stop; tell the user the SVG preview is incomplete |
| `validation/svg_quality_report.json` (Quick) or the Default final report | Present and `status` final / passed | Stop; rerun the owning checker before export |
| `design_spec.md` + `spec_lock.md` | Default only | Stop; run [`resume-execute`](resume-execute.md) or return to planning |
| `notes/total.md` | Only when Speaker Notes is enabled | Generate/split notes before export |

Do not open `validation/workflow.log` as planning state.

---

## Step 2: Export only

Follow the active Generate authority's export step exactly, without rerunning
planning or SVG authoring:

- Default: [`generate-pptx.md`](../generate-pptx.md) Step 7
  - notes disabled → `python3 ${SKILL_DIR}/scripts/svg_to_pptx.py <project_path> --no-notes`
  - notes enabled → `python3 ${SKILL_DIR}/scripts/svg_to_pptx.py <project_path>`
- Quick: [`quick-generate.md`](../profiles/quick-generate.md) §4
  - `python3 ${SKILL_DIR}/scripts/svg_to_pptx.py <project_path> --quick-generate --no-notes`
  - `python3 ${SKILL_DIR}/scripts/svg_to_pptx.py <project_path> --quick-generate --with-notes`

Run any conditional pre-export stage only if the active authority requires it
(verify-charts / customize-animations / motion flags). Do not run
`finalize_svg.py` in Quick.

**Success criterion**: exits 0 and produces
`exports/<project_name>_<timestamp>.pptx` plus the matching postflight report.

---

## Step 3: Hand-back

Report the exported PPTX path and postflight receipt. If Narration Audio is
enabled, hand off to [`generate-audio`](generate-audio.md) as the authority
describes.
