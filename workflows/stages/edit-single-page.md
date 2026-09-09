---
description: Page-level revision stage for generated SVG previews. Modify exactly one page of svg_output without regenerating the deck.
---

# Edit Single Page Stage

> Generate-PPTX page-level revision stage. Run when the user asks to modify
> one specific page of an existing generated SVG preview — e.g. “修改第 5 页”,
> “把这张图加到第 3 页”, “第 7 页标题改成…”, “只改第 2 页的配色”. This
> stage changes exactly one `svg_output/<NN>_*.svg`; it never regenerates the
> roster, never reruns planning, and never touches other pages.

## When to Run

- The user names one page explicitly (number, title, or unambiguous content)
  AND the project already has a non-empty `svg_output/`.
- The requested change is page-local: wording, layout of one page, add/replace
  an image on one page, local color/position adjustments.

**When not to run**:
- “全部重新生成 / 整体重做 / 重新设计风格 / 调整整体结构” → Default or
  Quick Generate full pipeline.
- The target is a finished PPTX without `svg_output/` → Edit Native PPTX.
- The request spans many pages but is still page-by-page → run this stage once
  per page, sequentially, with a preview stop after each page.

---

## Step 1 — Locate the project and target page

1. **Project path**: use the project from the current conversation if known;
   otherwise list `PROJECTS_ROOT` and match by name. If still ambiguous, ask
   one short question.
2. **Target page**: prefer an explicit page number (“第 5 页”) and resolve it
   against the ordered `svg_output/` roster. For content-based references,
   match the page by its file name or its `design_spec.md §IX` page job; do not
   guess when ambiguous — ask.
3. Resolve the exact SVG file: `svg_output/<NN>_<slug>.svg` (or the filename
   that owns that roster position).

## Step 2 — Read only the necessary context

Read once, in this order:

1. The target page SVG itself.
2. The target page's entry in `design_spec.md` and any `spec_lock.md` slot /
   structure / style anchors that apply to that page.
3. Only the construction references required by the requested change (e.g.
   [`image-layout-patterns.md`](../../references/image-layout-patterns.md) for
   adding an image; [`executor-base.md`](../../references/executor-base.md)
   §2.2/§3 only if topology or checker repair needs it).

**Hard rules**:
- Do NOT re-read Strategist, Confirm UI, template candidates, or routing docs.
- Do NOT re-read every page SVG or scan the whole deck.
- Do NOT re-run `project_manager.py init` or full `import-sources`.
- Do NOT recreate `design_spec.md` / `spec_lock.md`.

## Step 3 — Prepare page-local assets

- For an attachment or user-provided image: copy it into
  `<project_path>/images/` with a page-local name (e.g.
  `page_05_figure.png`) and reference it from the target SVG as
  `href="../images/page_05_figure.png"`.
- For a newly generated/downloaded image: acquire it only for this page and
  store it under `images/`; do not rebuild the deck image manifest.
- If the image row already exists in `spec_lock.md images`, update only that
  row; otherwise keep the image as a page-local asset and do not touch the
  planning artifacts.

## Step 4 — Edit only the target SVG

- Open `svg_output/<target>.svg` and apply the requested change.
- Keep the exact canvas (e.g. `viewBox="0 0 1280 720"`), the existing file
  name, and all other files unchanged.
- Respect the page's existing template / slot / structured metadata contract
  from `spec_lock.md`.
- Do not rename, reorder, create, or delete any other page file.

## Step 5 — Single-page quality gate

Run the checker in page mode against only the edited page.

Default / structured project:

```bash
python3 ${SKILL_DIR}/scripts/svg_quality_checker.py <project_path> \
  --stage page --page <target.svg> --json
```

Quick project:

```bash
python3 ${SKILL_DIR}/scripts/svg_quality_checker.py <project_path> \
  --stage page --page <target.svg> --quick-generate --canonical-authoring --json
```

- Fix every blocking error in the target page and rerun the same command until
  it exits 0.
- Report path: `validation/svg_quality_page_report.json`.
- Do not run the final all-page checker here unless the change affects a
  deck-wide anchor (new color, font, canvas, or global slot); in that case run
  the final checker once before export.

## Step 6 — Refresh preview and stop

1. Tell the host to refresh the preview panel (`ppt:updated`) or reload the
   page in live preview.
2. Report to the user in one short message: page X updated, other pages
   untouched, preview refreshed.
3. Stop at the SVG preview confirmation gate. Do NOT run `svg_to_pptx.py`.
   Wait for the user to request another page edit or confirm export.

## Step 7 — Export after confirmation

When the user clicks 「生成 PPT 文件」 or explicitly asks to export, enter
[`resume-export`](resume-export.md) and only run Step 7 / Quick §4 export.
Do not re-edit SVGs at that point.
