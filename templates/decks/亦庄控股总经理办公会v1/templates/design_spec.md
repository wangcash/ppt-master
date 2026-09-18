---
deck_id: "亦庄控股总经理办公会v1"
kind: deck
category: government
summary: 亦庄控股各部门向总经理办公会汇报、事项审议与情况报告的棕金国企视觉 Deck 模板，用于会前通读、会上审议决策与会后归档传阅。
keywords: ["总经理办公会", "亦庄控股", "部门汇报", "审议决策", "棕金国企风"]
primary_color: "#BF8E2B"
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 960
source_canvas_height: 540
source_viewbox: "0 0 960 540"
replication_mode: standard
native_structure_mode: structured
page_count: 6
placeholders:
  06_ending: []
---

# 亦庄控股总经理办公会v1 — Design Specification

## I. Template Overview

| Application context | Definition |
|---|---|
| Recurring presentation family | 公司各部门向总经理办公会（及总经理主持的专题会、办公例会）作事项汇报、研究审议、前置研究和情况报告等会议材料。 |
| Intended audiences and outcomes | 总经理、副总经理及列席部门负责人；支持会前材料通读、会上审议决策、会后归档传阅。 |
| Delivery and reading assumptions | 以会议室投屏宣讲为主、会后传阅为辅；标题在缩略图尺度可辨，正文按 24–36px 级字号排布，单页信息量以 10–12 行为宜。 |
| Representative narrative/page roles | 封面 → 前言 → 目录 → 章节页 → 默认空白页（正文，可重复）→ 结束页。 |

整体为白底棕金国企视觉：`#BF8E2B` 金色承担识别与强调，`#6A3F10` 深棕承担页眉与标题，`#632523` 深绛棕承担页眉与信息文字；封面与结束页以金色通栏加左侧深棕压块构成首尾呼应的固定幕布，前言、章节与正文页共用同一套页眉横线与方块。全篇仅棕、金、灰、白四个色族，不使用第二种彩色。

## II. Color Scheme

| Role | Hex | Usage |
|---|---|---|
| Primary gold | `#BF8E2B` | 封面通栏、章节标题与前导「Part:」、前言大标签底色、章节页角标括号 |
| Deep gold | `#A37925` | 结束页通栏、前言虚线卡片描边、前言正文 |
| Chrome brown | `#6A3F10` | 页眉横线与右端方块、正文页标题前导标记、目录条目文字、封面/结束页压块（86% / 78%） |
| Ink maroon | `#632523` | 页眉「产业新城运营商」、封面信息行、正文页标题、封面与结束页网址行 |
| Panel grey | `#F2F2F2` | 章节页内容面板（实色）、正文页内容面板（67%） |
| Hatch grey | `#808080` | 首尾通栏下沿斜纹条、章节页说明占位文字 |
| Site grey | `#404040` | 源文件页码文字色，本模板无页码槽位，保留为兼容参考 |
| Neutral white | `#FFFFFF` | 页面底色、前言卡片、反白文字、目录分隔线、章节角标白色错位块 |

## III. Typography

| Role | Typeface stack | Size / weight |
|---|---|---|
| 封面主标题 | 方正小标宋简体, Microsoft YaHei, sans-serif | 64px / 常规（反白渐变填充） |
| 封面部门与日期行 | 方正大标宋_GBK, Microsoft YaHei, sans-serif | 24.89px / 常规 |
| 页眉「产业新城运营商」 | 方正小标宋_GBK, Microsoft YaHei, sans-serif | 19.56px / 常规，letter-spacing 4 |
| 页眉网址行 | Microsoft YaHei, sans-serif | 18.67px / 常规 |
| 章节标题（含固定「Part:」前缀） | 黑体, Segoe UI Black, Microsoft YaHei, sans-serif | 35.56px 粗体 / 前缀后标题 32px |
| 前言大标签 | 方正小标宋_GBK, Microsoft YaHei, sans-serif | 42.67px / 常规，居中反白 |
| 前言正文 | Microsoft YaHei, sans-serif | 28.44px / 常规 |
| 目录序号 | Arial, Microsoft YaHei, sans-serif | 32px / 粗体，反白 |
| 目录条目 | Microsoft YaHei, sans-serif | 32px / 粗体 |
| 正文页标题 | 黑体, Segoe UI Black, Microsoft YaHei, sans-serif | 35.56px / 粗体 |
| 正文页正文 | Microsoft YaHei, sans-serif | 28.44px / 常规 |
| 结束语 | 方正大标宋_GBK, Microsoft YaHei, sans-serif | 96px / 常规（反白渐变填充） |

目标投送端为 Windows Microsoft PowerPoint。方正小标宋简体、方正小标宋_GBK、方正大标宋_GBK 未安装时由栈内 Microsoft YaHei 承接，版式、字号与断行不变；模板不做字体嵌入。

## IV. Signature Design Elements

- **首尾通栏幕布**：封面在 `y=190.83–459.19` 铺满 1280px 宽的 `#BF8E2B` 通栏，结束页在 `y=168.97–437.33` 铺满 `#A37925` 通栏；两页通栏均带 dx=5.33 / stdDeviation=3.56 / 40% 黑的向右投影，并在左端叠压 265.28px 见方的 `#6A3F10` 压块（封面 86%、结束页 78% 不透明），压块位于通栏之上，交叠处形成更深棕的固定色块。标题与结束语居中或左起于通栏安全区内，白色文字使用垂直光泽渐变填充（`#FFFFFF` 至 84%，末段 `#632523` 75%）。封面主标题为可替换占位符，结束页「汇报完毕」为固定版式原子（沿源文件位置与字号、内容不变，不受替换影响），故结束页为零槽版式。
- **通栏下沿斜纹条**：通栏正下方一条 43.19px 高的灰色斜纹带，从 `x=336.97` 起以 45° 平行线条向右延伸至画布右缘，线距 12.1px、线宽 2.4px、颜色 `#808080`；左端按 45° 斜切形成错落起始，整条为一枚原子路径。
- **页眉 chrome**：前言、章节、默认空白页共用同一组页眉——左上横版品牌 Logo（`40.19,36.61`，129.64×31.48）、`#6A3F10` 横线（`x=177.57` 起，通至 1236.45，高 9.16）、右端 `#6A3F10` 方块（43.13×38.45，接画布右缘），右上「产业新城运营商」字距 4 的 `#632523` 文字。
- **金色角标括号**：章节页内容面板左上与右下各一组 121.35×105.84 的 `#BF8E2B` 方块与偏移 10.51×10.29 的白色方块错位叠压，形成外侧金色、内侧反白的 L 形角标；角标绘制在面板之下，只有露出面板外的两条边可见。
- **前言虚线卡片**：白底卡片（887.03×352.8）配 `#A37925` 1.33px 点状描边（`1.33 4`），左端叠压 393.12×252.05 的 `#BF8E2B` 大标签色块，标签文字居中反白。
- **目录通栏**：`y=165.71–553.91` 铺满 1280px 的 `#BF8E2B` 29% 浅金通栏，`x=468.64` 处一条 5.33px 白色竖分隔线通高；分隔线左侧为竖版品牌 Logo（148.21,288.79，182.09×142.05）——Logo 与分隔线同处通栏内但分属两侧；右侧 4 组「01–04 白色粗体序号 + `#6A3F10` 条目」，行距 94.08px 自 `y=228.71` 起。
- **正文页标题前导标记**：`#6A3F10` 方块（43.13×42.31）与其右侧 4.8px 竖条组成标题前导符，标题自 `x=117.65` 起排；下方 1171.81×483.93 的 `#F2F2F2` 67% 面板承载正文区。
- **版式栅格**：页眉横线顶边 48.2、高 9.16；正文页标题基线 154.03；内容安全区自 213.33 起、至 626.66 止；章节页面板 `125.93,195.55`–`1144,622.07`；目录序号列 `x=577.55`、条目列 `x=657.91`。
- **强调色纪律**：全篇只有棕、金、灰、白四个色族。金色只承担识别与强调（通栏、标题、角标、目录条目序号底），深棕承担页眉与标题，灰色承担衬底与纹理，不使用第二种彩色，避免与办公会材料的严肃语境冲突。

## V. Page Roster

| Page | Layout key | Picker name | Role | Visual character | Reusable slots | Capacity |
|---|---|---|---|---|---|---|
| `01_cover.svg` | `cover` | 封面页 | 封面 | 白底 + 中部金色通栏 + 左端深棕压块 + 左上品牌 Logo + 通栏下沿斜纹条 + 左下部门/日期两行 + 右下运营商与网址 | `{{TITLE}}`, `{{AUTHOR}}`（承载于「汇报部门：」标签后）, `{{DATE}}`（承载于「时间日期：」标签后） | 标题 1–2 行；部门一行；日期一行 |
| `02_preface.svg` | `preface` | 前言页 | 前言 | 页眉 chrome + 金色点状线卡片 + 左端金色大标签色块 + 右侧前言正文 | `{{TITLE}}`（大标签，默认「前 言」）, `{{CONTENT_AREA}}` | 大标签 2–4 个汉字；正文约 5–7 行 |
| `03_toc.svg` | `toc` | 目录页 | 目录 | 浅金通栏 + 白色竖分隔线 + 左侧竖版品牌 Logo + 右侧 4 组序号与条目 | `{{TOC_ITEM_1_TITLE}}` … `{{TOC_ITEM_4_TITLE}}` | 4 条，每条一行，约 16 个全角字 |
| `04_chapter.svg` | `chapter` | 章节页 | 章节页 | 页眉 chrome + 4 组错位叠压角标括号 + 灰色内容面板 + 金色「Part:」章节标题 | `{{CHAPTER_TITLE}}`（承载于固定「Part:」前缀之后）, `{{CHAPTER_DESC}}` | 标题一行；说明区约 6–8 行 |
| `05_blank.svg` | `blank` | 默认空白页 | 默认空白页 | 页眉 chrome + 深棕方块与竖条前导标记 + `#632523` 标题 + 浅灰内容面板 | `{{PAGE_TITLE}}`, `{{CONTENT_AREA}}` | 标题约 16 个全角字；正文约 10–12 行 |
| `06_ending.svg` | `ending` | 结束页 | 结束页 | 白底 + 深金通栏 + 左端深棕压块 + 通栏下沿斜纹条 + 左上品牌 Logo + 反白结束语 | 无（零槽版式）：「汇报完毕」为固定版式文案，与源文件一致，不参与替换 | 固定文案一行，4 个汉字 |

## VI. Assets

| Asset | Path | Use |
|---|---|---|
| Brand logo (horizontal) | `../images/logo-horizontal.png` | 封面、结束页左上角与前言/章节/正文页页眉的横版「亦庄控股 E-TOWN HOLDINGS」标识 |
| Brand logo (stacked) | `../images/logo-stacked.png` | 目录页分隔线左侧的竖版品牌标识 |

源示例中的业务文字、项目名称与数据（「研究审议/审议XXXXXXXX有关事项」、`Part: 汇报事项的源起`、`概 述`、`一级标题`、`文字编辑区域`、`提请办公会决策事项`、`当前进展` 网格、四圆环图）、示例英文备注，以及 Office 默认主题色与 Calibri 字体均不入模板；源文件中首尾通栏下沿的斜纹贴图已按同等线距、线宽与角度重绘为一枚矢量路径，源文件第 1、10 页继承的幻灯片编号占位符位于画布外未显示，故模板不设页码槽位。
