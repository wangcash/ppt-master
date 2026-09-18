---
deck_id: "党委会模板v1"
kind: deck
category: government
summary: 公司各部门向党委会/党委常委会进行工作汇报、事项审议、前置研究和情况报告的红色党政风 Deck 模板。
keywords: ["党委会汇报", "党政红", "部门汇报", "会议材料", "国企党建"]
primary_color: "#C00000"
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: fidelity
native_structure_mode: structured
page_count: 8
---

# 党委会模板v1 — Design Specification

## I. Template Overview

| Application context | Definition |
|---|---|
| Recurring presentation family | 公司各部门向党委会 / 党委常委会进行工作汇报、事项审议、前置研究和情况报告等会议材料。 |
| Intended audiences and outcomes | 党委委员 / 党委常委；支持审议决策、情况通报与工作部署。 |
| Delivery and reading assumptions | 以会议室投屏宣讲为主，兼顾会后传阅；正文以清晰可读的 16–24px 级字号为主。 |
| Representative narrative/page roles | 封面、前言、目录、章节页、内容更新页、图文页、总结页、结束页。 |

整体为白底红色党政视觉：以 `#C00000` 为主色，封面/结束页使用深红横幅，内容页以红色标题条统一识别，灰白面板承载正文，红色用于关键数据与差异强调。

## II. Color Scheme

| Role | Hex | Usage |
|---|---|---|
| Primary red | `#C00000` | 标题条、关键线条、目录条目、章节标题 |
| Deep red | `#B5261F` | 封面 / 结束页横幅 |
| Dark red | `#99191E` | 深红辅助、版式红带 |
| Auxiliary red | `#90181C` | 章节页装饰线、内容页箭头卡 |
| Highlight red | `#A00112` | 正文重点数据、修订差异标注 |
| Blue accent | `#2F5597` | 章节标签描边等少量点缀 |
| Neutral white | `#FFFFFF` | 页面底色、反白文字 |
| Panel grey | `#F2F2F2` | 内容底板、图片占位底 |
| Gradient grey | `#D9D9D9` | 前言/目录卡片渐变与描边 |
| Secondary text | `#595959` / `#404040` | 说明文字、正文 |
| Ink | `#000000` | 修订/对比正文 |

## III. Typography

| Role | Typeface stack | Size / Weight |
|---|---|---|
| 封面主标题 | 方正小标宋简体, 微软雅黑, sans-serif | 58.67px / bold |
| 章节序号 | Agency FB, 方正黑体简体, sans-serif | 72px / bold |
| 章节标题 | 微软雅黑, sans-serif | 48px / bold |
| 页面标题条 | 微软雅黑, sans-serif | 24px / bold, letter-spacing 4 |
| 前言/目录大标签 | 微软雅黑, sans-serif | 96px / bold |
| 正文 / 卡片 | 微软雅黑, 微软雅黑 Light, sans-serif | 16–32px |
| 结束语 | 方正黑体简体, 微软雅黑, sans-serif | 72px / bold |

字体以 Windows 端 PowerPoint 目标机已安装字体为前提；未安装的方正字体以微软雅黑回退，Agency FB 用于数字和拉丁字符。

## IV. Signature Design Elements

- 封面/结束页：全宽深红横幅（`#B5261F`）横贯画面中部，承载反白标题，形成首尾呼应的固定品牌幕布。
- 前言/目录页：灰白渐变圆角卡片 + 左上红色折角标 + 大号页面标签；卡片带轻微投影，右下角红色折角为识别点。
- 章节页：居中红色菱形叠加灰边菱形，白色序号居中，红色章节标题两侧配细线。
- 内容页标题条：红色矩形标题条 + 白色加粗标题，右接灰色说明区，形成统一页眉。
- 内容更新页：灰色大底板 + 左右两个红框对比栏，固定“修订前/修订后”标签，修订差异以红色强调。
- 图文页：左侧标题与要点文本，右侧 1–2 个图片位，图片使用统一中性占位图。
- 总结页：红色标题条 + 三张浅灰总结卡片，每卡含标题与正文两段占位。
- 布局栅格：页面左右安全边距约 76px，标题条高约 38.67px，正文底板从标题条下方约 124px 开始。

## V. Page Roster

| Page | Layout key | Picker name | Role | Visual character | Reusable slots | Capacity |
|---|---|---|---|---|---|---|
| `01_cover.svg` | cover | 封面页 | 封面 | 深红横幅 + 白色大标题 + 部门/日期 + 两侧红色细线 | `{{TITLE}}`, `{{SUBTITLE}}`, `{{DATE}}` | 标题两行以内；副标题/日期各一行 |
| `02_preface.svg` | preface | 前言页 | 前言 | 灰白渐变卡片 + 红色折角标 + 大号“前言” + 正文 | `{{PAGE_TITLE}}`, `{{CONTENT_AREA}}` | 正文约 5–7 行 |
| `03_toc.svg` | toc | 目录页 | 目录 | 同前言卡片 + 红色目录条目 | `{{PAGE_TITLE}}`, `{{TOC_ITEM_1_TITLE}}`…`{{TOC_ITEM_5_TITLE}}` | 5 条目录 |
| `04_chapter.svg` | chapter | 章节页 | 章节页 | 红色菱形 + 白色章节号 + 红色标题 + 两侧细线 | `{{CHAPTER_NUM}}`, `{{CHAPTER_TITLE}}` | 序号 2 位；标题两行以内 |
| `05_content_update.svg` | content_update | 内容更新页 | 内容更新/修订对比 | 红色标题条 + 灰色底板 + 红框双栏 | `{{PAGE_TITLE}}`, `{{SUBTITLE}}`, `{{BEFORE_TITLE}}`, `{{BEFORE_BODY}}`, `{{AFTER_TITLE}}`, `{{AFTER_BODY}}` | 每栏约 8–10 行正文 |
| `06_image_text.svg` | image_text | 图文页 | 图文展示 | 红色标题条 + 左侧正文 + 右侧两个图片位 | `{{PAGE_TITLE}}`, `{{CONTENT_AREA}}`, 图片位 ×2 | 正文约 8–10 行；图片 16:9 或裁切填充 |
| `07_summary.svg` | summary | 总结页 | 总结 | 红色标题条 + 三张浅灰卡片 | `{{PAGE_TITLE}}`, `{{SUMMARY_1_TITLE}}`, `{{SUMMARY_1_BODY}}`…`{{SUMMARY_3_BODY}}` | 每卡标题一行、正文约 3–4 行 |
| `08_ending.svg` | ending | 结束页 | 结束页 | 深红横幅 + 白色结束语 + 下方细线 | `{{THANK_YOU}}` | 结束语一行 |

## VI. Assets

| Asset | Path | Use |
|---|---|---|
| Brand logo | `../images/image2.png` | 内容更新页、图文页、总结页右下角品牌标识 |
| Picture placeholder | `../images/picture_placeholder.png` | 图文页图片位默认中性占位图 |

源示例中的业务照片（image1、image3–image15）为示例内容，不进入模板资产。
