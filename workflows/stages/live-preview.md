---
description: Main-pipeline stage for chat-driven SVG edits and applying previously submitted annotations (browser editor disabled in this environment).
---

# Live Preview Stage

> (1) In this environment the browser SVG editor on `127.0.0.1:6060` is **disabled** — do not launch it; the host app's built-in PPT preview panel shows the generated SVGs. (2) Apply previously submitted annotations after Step 7 export. Editor internals are documented in [`svg_editor.md`](../../scripts/docs/svg_editor.md) but the launch workflow is intentionally disabled.

## When to Run

- **Step 1** — the user wants to look at the deck or click an element (post-export re-entry in a fresh chat): direct them to the host app's built-in PPT preview panel; do **not** launch a browser editor.
- **Step 2** — Step 7 has produced at least one PPTX and the user signals that previously submitted annotations should be applied: quoting the old browser prompt (`Changes saved to svg_output...` / `修改已保存到 svg_output...`) or saying `apply my annotations` / `apply my edits` / `应用注解` / `开始应用`.

**When not to run**: a precise chat edit ("change page 3 title to X", "把图加到第 5 页") → run [`edit-single-page`](edit-single-page.md), not this stage; a full regeneration → main workflow; Step 7 has never run → finish the main pipeline first.

---

## Step 1: Preview and edit without the browser editor (DISABLED)

Do **not** run `svg_editor/server.py` or any `6060` preview server. Tell the user, in their language, in one short message:

- the host app's built-in PPT preview panel already shows the generated SVGs (no URL needed, no browser to open);
- for deterministic tweaks (wording, color, coordinates, attributes), the user should describe the change in chat and you edit the SVG directly (or via [`edit-single-page`](edit-single-page.md));
- annotations that require AI judgement are just chat requests in this environment — the user describes the change, you edit the SVG directly.

---

## Step 2: Apply submitted annotations

🚧 **GATE**: `<project_path>/exports/` contains at least one `*.pptx`; otherwise tell the user to finish the main pipeline first.

1. `python3 ${SKILL_DIR}/scripts/check_annotations.py <project_path>` — its output lists each pending change as `file → element_id → annotation text → content preview`; use it directly as the to-do list. If it reports none, tell the user and stop.
2. For each annotation: edit the targeted element in `<project_path>/svg_output/<file>` per the text; remove `data-edit-target` and `data-edit-annotation` from it; append one `annotation_applied` JSONL record (`ts`, `file`, `element_id`, original text) to `<project_path>/live_preview/annotations.jsonl`.
3. Re-enter [`generate-pptx`](../generate-pptx.md) Step 7.2, wait for its success criterion, then run Step 7.3; rerun Step 7.1 only when speaker notes changed.
4. Tell the user, in their language: annotations applied, new PPTX exported; the host preview panel will show the updated SVG after refresh/reselect.
5. More annotations → repeat from 1; "done" → end.
