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

**Fast path（默认，必须优先使用）**：对于“插入/替换一张图、改一句文案、
调整位置/颜色”这类单页局部修改，只读目标页 SVG。不要读设计规格全文、
不要读执行器规范、不要读图片布局参考。

**Slow path（仅当 Fast path 无法完成时）**：只有当修改涉及模板 slot /
结构化元数据 / 全局锚点时，才追加读取：

1. `design_spec.md` 中该页的 §IX 条目（不要读全文）。
2. `spec_lock.md` 中与该页/该素材相关的锚点或 slot 行（不要读全文）。
3. 仅当图片布局存在真实歧义时，读
   [`image-layout-patterns.md`](../../references/image-layout-patterns.md)
   的相关小节；否则不读。

**Hard rules**:
- Do NOT re-read Strategist, Confirm UI, template candidates, routing docs,
  `executor-base.md`, `shared-standards-core.md`, or any full workflow file.
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
- **Default / structured project（存在 `design_spec.md` 与 `spec_lock.md`）**：
  新增图片后必须同步登记，否则最终质检会以 `svg_image_missing_spec` 拒绝
  导出：
  - 在 `spec_lock.md` 的 `## images` 段追加一行：
    `<file>.png: images/<file>.png | source=user | crop=no-crop`
  - 在 `design_spec.md` 的 `## VIII. Image Resource List` 表中追加一行，
    Filename / Purpose / Type / Acquire Via / Status / page_role 填该页实际
    用途；其余列可填 `—` 或实测值。
  - 只追加，不重写整个文件。
- Quick project：无需 spec/lock 登记，图片保持页内自包含引用。

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
