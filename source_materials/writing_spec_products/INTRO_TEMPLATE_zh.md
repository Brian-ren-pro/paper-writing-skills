# 英文经管顶刊引言填空手册（宏观 / 中观 / 微观）

2026-10-20。本手册取代 `EN_intro_fill_in_guide_v2.md` 中关于段落的部分，所用的段落数据是新的一套。

**数据来源**
- 统计口径：`writing_spec/intro_blueprint/` 的语料分析（`REPORT.md`）。
- 句子层面的规则：`writing_spec/EN_writing_spec_v1.md`（v1.1）。
- 几项新增的句子统计：在 117 篇可信引言的重建文本上计算，口径见第三章开头。

**三个样本层级**，下文的每个数字都注明来自哪一层：

| 层级 | 样本 | 用途 |
|---|---|---|
| 全库 | 267 篇英文论文（JF/JFE/RFS/JFQA/MS/JAR/TAR/CAR），清洗规则同 v1.1 | 句子层面的频率 |
| 可信段落集 | 117 篇（金融 77，会计 40）。段落边界从 PDF 版面重建，并通过了质量过滤 | 篇幅、段长、句长 |
| 人工标注集 | 40 篇（金融 25，会计 15），共 565 段。我逐段读完全文，每段标一个功能 | 段落功能、顺序、信息要素 |

**符号**
- 方括号里的区间是四分位距，也就是中间 50%。
- **[数据]** 表示由语料算出；**[编辑]** 表示我的判断，语料只部分支持。
- 所有英文模板都由我抽象而成，变量用 [占位符] 表示，不是语料原句。

---

## 〇、怎么用这份手册

### 0.1 使用顺序

1. **先填第四章的工作表。** 工作表就是新的 Content Brief。凡是标了"必填"的格子，填不出来就说明这部分研究还没想清楚，不要指望写作阶段补上。
2. **按第一章选版式。** 根据论文类型，从四种版式里选一种，得到"第几段写什么"的段落地图。
3. **按第二章逐段写。** 每一段都有一张功能卡，卡上有逐句骨架（S1 做什么、S2 做什么……）、信息要素和开头模板。用工作表里的答案填骨架。
4. **按第三章的微观规则检查句子。** 包括句长变化、we 的用法、限定语强度、引用格式和数字写法。
5. **对照每张卡末尾的"AI 腔错误"清单删改。**

> **总则（来自 v1.1 对照实验）**：本手册只管**怎么写**，不管**写什么**。凡是涉及内容的规则，例如"给量级"或"说清与文献的差异"，只在工作表里已经有这项内容时才执行，没有就跳过，**不许补**。v1 规范缺这一条时，写作模型为了满足"点名文献并说清差异"，编造了被引文献的观点：无依据句子从 11 句升到 34 句（6 篇稿件）。

### 0.2 篇幅预算 [数据，可信段落集 n=117]

| 指标 | 全部 (117) | 金融 (77) | 会计 (40) |
|---|---|---|---|
| 引言总词数 | **1,848** [1,446–2,225] | 1,832 [1,446–2,293] | 1,876 [1,458–2,195] |
| 段落数 | **14** [11–17] | 14 [11–18] | 13 [12–16] |
| 句子数 | **73** [55–90] | 74 [59–92] | 69 [54–82] |
| 每段句数 | **5** [4–6] | 5 [4–6] | 5 [4–6] |
| 每段词数 | **126** [95–163] | — | 主体段略长（第一个五分位段 151 词，金融 124 词） |
| 每句词数 | **25.5** [21.6–29.8] | 24.8 [21.0–29.0] | 26.9 [23.0–31.7] |
| 有路线图段 | 44% | 52% | 30% |
| 有脚注标记 | 91%，中位 6 个 [3–8] | 92%，6 [3–8] | 90%，5 [2–7] |

几条由预算推出的经验：
- **段长几乎不随位置变化。** 从引言前 1/5 到最后 1/5，主体段都在 123–134 词之间。所以不要"开头长段铺垫、结尾短段收尾"。
- **只有路线图一段明显短**：55 词 [43–87]，5 句 [5–6]，基本一节一句。
- **第一段**中位 123 词，5 句，与主体段一样长。
- **分刊参考**：JAR 约 2,087 词，JF 约 1,710 词，CAR 只有约 1,652 词、10 段（n=6，仅供参考）。
- **写作时**先按 14 段、约 1,850 词写满，最后再按目标刊压缩或扩展。模型最常见的问题是写成 600–900 词的"摘要扩写版"。要补篇幅，就补设计细节、量级和稳健性，不要靠复述凑字（见 2.15 节）。

---

## 一、宏观：选版式

### 1.1 四种版式怎么选

人工标注集 47 篇引言（原 40 篇加补标的 7 篇）可以归为四种版式。下表的篇数用的是规则 v3，它与人工归类在 42/47 篇上一致（89%）。成员名单、逐篇理由，以及每种版式各 3 篇的完整原文分析，见 `LAYOUT_EVIDENCE.md` [数据，LAYOUT_EVIDENCE §Summary、A1–A3]：

| 版式 | 篇数 /47 | 金融/会计 | 段数中位 | 词数中位 | 适合什么论文 | 一句话特征 |
|---|---:|---:|---:|---:|---|---|
| **A. 线性** | 22 | 12 / 10 | 14 | 1,780 | 一个主问题、一个主设计，后面的结果都在细化同一个估计。**普通实证因果论文的默认选项** | 问题 → 理论 → 数据和设计 → 结果 → 贡献 |
| **B. 设计-结果循环** | 9 | 7 / 2 | 15 | 2,080 | 有两个或更多独立检验，每个用自己的设计、数据或事件 | 每个检验先交代设计，紧接着报结果，然后进入下一个检验 |
| **C. 文献和缺口前置** | 7 | 4 / 3 | 12 | 1,610 | 卖点是"纠正或补全某几篇具体文献"，例如推翻、细化或换测量 | 在"本文"句之前，至少用一个非开篇段回顾具名文献或它们的测量、数据缺口 |
| **D. 理论/方法领衔** | 9 | 8 / 1 | 16 | 1,720 | 理论模型、结构估计、新方法，或"模型 + 检验"型论文 | 在第一个实证结果之前先讲本文自己的模型或估计方法，卖的是它的预测或产出 |

段数和词数都不计脚注段（X）和无关段（V）；金融刊包括 MS。

**规则 v3（按顺序判断）** [数据，LAYOUT_EVIDENCE §A1]：
1. **C**：至少有 1 个定位段同时满足三个条件：不是开篇段；位于第一个"本文"句之前；位于第一个数据/设计段和第一个结果段之前。定位段指文献段，或者带具名文献和明确缺口、但还没有"本文"句的引子/问题段。
2. **D**：在第一个实证结果段之前，至少有 2 段在讲本文自己的模型设定或模型结论。
3. **B**：在第一个实证结果之后，至少有 2 次引入新的设计或数据，并且每次后面都跟着结果。引入新设计指三种情况之一：一个数据/设计段；一个带设计、数据源、冲击或情境的结果段或补充结果段；一个带设计或冲击的机制段、稳健性段或识别段。
4. **A**：以上都不满足。

C 要先于 D 判断，因为理论或方法论文也可能先做文献回顾。旧版手册的 15/11/11/3 和旧的重新分组规则（理论段 ≥3 为 D 等）已经作废：旧规则只在 18/40 篇上与人工归类一致，而且背后的逐篇名单没有保存下来。

**怎么选** [编辑，与规则 v3 对应]：
- 主结果来自一个设计，后续结果都在细化它 → 选 A。
- 有两个或更多设计，各自独立成立并各有结果 → 选 B。
- 审稿人第一反应会是"这不是 X (Year) 做过吗"，而且你能点名 2–5 篇近邻文献并说清它们的发现 → 选 C，先把差异讲在前面。
- 论文的核心产品是自己的模型或估计方法，并且能在结果前讲清设定和结论 → 选 D。

**篇幅随目标词数调整**：下面 1.2 的段落地图按约 15 段写成。目标词数较短时，段数约等于目标词数 ÷ 125，靠合并相邻行来压缩，例如"数据 + 设计"、"异质性 + 机制"、把几条贡献脉络合成 1–2 段。不要为了省篇幅删掉工作表里的内容。

### 1.2 段落地图

下面四张表中，每段的句数和词数取该功能段的中位数，来自人工标注集的功能画像（REPORT §3a）。

#### 版式 A：线性（15 段，约 1,820 词）

| 段 | 功能 | 句 | 词 | 备注 |
|---:|---|---:|---:|---|
| 1 | 引子/现象（会计刊常直接写问题段） | 6 | 126 | 最后一句转向缺口或问题 |
| 2 | 研究问题/缺口/"本文" | 5 | 138 | "this paper" 句必须在第 1–2 段出现 |
| 3 | 理论/假设 ① | 6 | 128 | 机制论证 |
| 4 | 理论/假设 ②（对立预测或 H2） | 6 | 128 | 可选；理论段中位 2 段 [1–3] |
| 5 | 数据与情境 | 5 | 131 | 数据来源、样本期、N、为什么这个情境好 |
| 6 | 实证设计 | 4 | 121 | 处理组和对照组、变量构造、固定效应 |
| 7 | **主要发现** | 5 | 119 | 第一个结果放在约 37–45% 处 |
| 8 | 经济量级（或并入第 7 段） | 5 | 102 | 只有 8/40 篇单列成段 |
| 9 | 异质性/补充结果 | 5 | 132 | |
| 10 | 机制 | 5 | 133 | 机制段中位 2 段 [1–3] |
| 11 | 稳健性/替代解释 | 4 | 116 | 最短的内容段 |
| 12 | 贡献 ① | 5 | 131 | 一条文献脉络一段 |
| 13 | 贡献 ② | 5 | 131 | |
| 14 | 贡献 ③ 或政策含义 | 5 | 117–131 | |
| 15 | 路线图（可选） | 5–6 | 55 | 写的话放在最后 |

#### 版式 B：设计-结果循环（16 段，约 1,950 词）

| 段 | 功能 | 句 | 词 | 备注 |
|---:|---|---:|---:|---|
| 1 | 引子 | 6 | 126 | |
| 2 | 问题/"本文" + 全文一句话答案 | 5 | 138 | |
| 3 | 数据与情境 | 5 | 131 | 公用的数据先交代一次 |
| 4 | 设计 ①（第一个检验） | 4 | 121 | |
| 5 | 发现 ① + 量级 | 5 | 119 | |
| 6 | 识别挑战（针对发现 ①） | 5 | 132 | 语料中常放在结果**之后**，用来回应质疑 |
| 7 | 设计 ② + 发现 ②（"Next, we exploit…"） | 5 | 125 | 一段之内先讲设计再讲结果 |
| 8 | 发现 ②的细节或异质性 | 5 | 132 | |
| 9 | 设计 ③ + 发现 ③（可选） | 5 | 125 | |
| 10 | 稳健性 | 4 | 116 | |
| 11–12 | 机制 ①、② | 5 | 133 | 一个渠道一段，每段以结论句收尾 |
| 13–15 | 贡献 ①②③ | 5 | 131 | |
| 16 | 路线图（可选） | 5–6 | 55 | |

#### 版式 C：文献和缺口前置（14 段，约 1,850 词）

| 段 | 功能 | 句 | 词 | 备注 |
|---:|---|---:|---:|---|
| 1 | 引子 | 6 | 126 | 引子段 68% 带具名文献 |
| 2 | 近邻文献 ①：它们做到了哪里 | 5 | 130 | 点名 2–5 篇，每篇用一个动词说清发现 |
| 3 | 近邻文献 ②或测量和识别的局限，落到缺口 | 5 | 130 | 以 "However, …" 收束 |
| 4 | "In this paper, we…"：问题和做法 | 5 | 138 | 位置比 A 晚，这一版式允许 |
| 5 | 数据与情境 | 5 | 131 | |
| 6 | 设计 | 4 | 121 | |
| 7 | 主要发现 + 量级 | 5 | 119 | |
| 8 | 异质性 | 5 | 132 | |
| 9 | 机制 | 5 | 133 | |
| 10 | 稳健性 | 4 | 116 | |
| 11–12 | 贡献（较短，1–2 段） | 5 | 131 | 差异前面已讲过，这里只补其余脉络 |
| 13 | 含义 | 5 | 117 | |
| 14 | 路线图（可选） | 5–6 | 55 | |

#### 版式 D：理论领衔（15 段，约 1,800 词）

| 段 | 功能 | 句 | 词 | 备注 |
|---:|---|---:|---:|---|
| 1 | 疑问或"标准理论假定 X" | 6 | 126 | |
| 2 | 问题/"本文提出一个模型…" | 5 | 138 | |
| 3 | 模型设定 | 5 | 125 | 主体、摩擦、关键假设 |
| 4–6 | 模型结论 ①②③ | 5–7 | 125 | 一个结论一段，每段以一句短判断收尾 |
| 7 | 估计、校准或检验方法 | 5 | 121 | |
| 8 | 实证发现 | 5 | 119 | |
| 9 | 补充结果或反事实 | 5 | 132 | |
| 10 | 政策或理论含义 | 5 | 117 | |
| 11–14 | 文献 ①②③④ | 5 | 131 | |
| 15 | 路线图（可选） | 6 | 55 | |

### 1.3 金融刊与会计刊的变体 [数据，人工标注集：金融 25，会计 15]

| 功能 | 金融含该段的比例 | 会计含该段的比例 | 这对你意味着什么 |
|---|---:|---:|---|
| 引子 | 64% | 40% | 会计刊可以直接从问题段开篇 |
| 研究问题/缺口 | 76% | **100%** | 会计刊的问题段常在第 1 段（首次出现位置中位 0.0；金融 0.10） |
| 理论/假设 | 72% | 80% | 会计刊更常明写 H1/H2（9/15，金融 11/25） |
| 识别挑战 | 44% | 33% | 金融刊更常单独讨论识别 |
| 数据与情境 | 48% | 67% | |
| 实证设计 | 52% | 33% | |
| 主要发现 | 96% | 73% | 金融刊结果段更多 |
| 异质性 | 88% | 67% | |
| 机制 | 60% | 47% | |
| 稳健性 | 56% | 67% | |
| 贡献段 | 84% | **100%** | 会计刊必有贡献段 |
| 政策含义 | 44% | 27% | |
| 局限/范围 | 8% | 20% | 会计刊更常写一句因果判断的局限 |
| 路线图（可信段落集，n=117） | 52% | 30% | 会计刊多数不写 |

- **会计刊的套路**：
  - 第 1 段写 "Prior research establishes [X]. What is less well known is [Y]." 然后接 "We posit…" 和 "We predict and find…"。
  - 贡献段 3 [3–3] 段，起点在相对位置 0.75 [0.67–0.82]。**73% 先宣布贡献条数**，例如 "makes three contributions"。
  - 句子平均比金融刊长约 2 词（26.9 对 24.8）。
- **金融刊的套路**：
  - 更常用事实、数字或事件开篇。
  - 结果段多，给量级的也多（19/25 篇；会计 10/15 篇）。
  - 贡献段的长短和位置都更灵活：3 [2–5] 段，起点 0.65 [0.28–0.85]，只有 29% 宣布条数。
- **两类期刊篇幅相同**：都在 1,850 词、13–14 段左右。

### 1.4 关键内容放在哪里 [数据]

| 锚点 | 数据 | 规则 |
|---|---|---|
| "本文研究什么" | 27/40 篇在第 1 或第 2 段 | **第 2 段结束前**必须出现 "In this paper, we…" 或同等的句子。只有版式 C 可以推迟到第 3–4 段 |
| 第一个结果 | 第一个结果段的相对位置：中位 0.38（金融 0.38，会计 0.36） | 15 段的引言里，第 6–7 段开始报结果。第 2 段可以先用一句话预告答案 |
| 贡献段 | 起点 0.71 [0.29–0.85]；75% 连成一整块；31/36 篇最后三段里有贡献段 | 贡献段放在结尾，连续写，不要分散 |
| 路线图 | 可信段落集 44% 有；52 篇有路线图的里，49 篇放在最后一段 | **可选**。写的话放最后，约 55 词 |
| 识别挑战 | 中位位置 0.46，通常在主结果之后 | 先给结果，再回应"你怎么知道是因果"，不要放在设计之前 |
| 稳健性 → 补充结果 | 是最常见的段间转移之一（11 次） | 稳健性可以插在两个结果段之间 |

段间最常见的转移（合并相邻重复后计数）：
- 问题 → 理论：17
- 引子 → 问题：14
- 设计 → 主要发现：12
- 理论 → 数据：11
- 主要发现 → 补充结果：10
- 补充结果 → 贡献：9
- 贡献 → 路线图：9

---

## 二、中观：段落功能卡

**卡片怎么读**
- **出现率**：人工标注集 40 篇中有该功能段的比例。
- **段数**：有这一功能的引言里，这类段的中位数。
- **句数和词数**：每段的中位数 [四分位]。
- **信息要素**："必含"指至少 70% 的同类段块含有该信息，"常含"指 30–69%。都写成你要回答的问题。
- **逐句骨架**：每张卡至少重读 8–10 段该功能的重建原文后归纳。S 编号是典型位置，不是硬性规定。

---

### 2.1 引子 / 现象（Hook）

**任务**：用一个具体的经济事实、制度或理论张力把读者带到问题门口，最后一句转向缺口。

**位置和规模**：出现率 55%（金融 64%，会计 40%）；第 1 段；1 [1–2] 段；6 [4–6] 句；126 [85–169] 词；每段约 2 [1–4] 个引用。

**逐句骨架**（读了 10 段）：
- **S1 主题句**：一句短的陈述，说研究对象本身或它的变化，常见长度 7–20 词，直接点出对象，没有铺垫。
  - 写法一：对象的性质，"[X] is a central tool for [Y]."
  - 写法二：趋势，"[Market] has grown rapidly."
  - 写法三：理论的标准假定，"Standard theory assumes [X]."
- **S2–S3 具体化**：
  - 一个数字或制度细节，例如规模、占比、某一年的事件；
  - 或"已有文献怎么看"，附 1–3 个具名引用。
- **S4 张力**：两种观点（"There are two views on [X]. The first… The second…"），或 "Yet / However, [与 S1 的假定相冲突的事实]"。
- **S5–S6 转向**：为什么重要，以及什么仍然未知，例如 "However, [X] remains largely unexplored."。有 4/10 段在这里直接接上 "this paper" 句。

**信息要素**：
- 必含：无，所以这一段的写法最自由。
- 常含：
  - 具名文献（68%）：开篇引用的是哪 1–3 篇基础文献？
  - 明确缺口（45%）：S5–S6 要转向的那个未知是什么？
  - 趋势（32%）：这件事在变大还是在变化？变化用什么数字衡量？
  - 醒目数字（32%）：有没有一个读者看了会停一下的数字？来源是什么？

**开头模板**：
1. `[Market/practice] has grown to [N] [units] by [year], up from [M] in [year].`
2. `In [month year], [concrete event with a number].`
3. `Standard [theory] assumes that [agents] [behave in way X].`
4. `[Institution X] is designed to [goal], yet [observed tension].`
5. `A long-standing question in [field] is whether [X] affects [Y].`

**AI 腔错误**：
- ❌ **宏大背景句开篇**："In recent years, X has attracted increasing attention from academics and practitioners." 可信段落集 117 篇中，只有 8 篇在引言任何位置出现 "in recent years"，"increasing attention" 只出现在 2 篇里。语料里第一句中位 20 词 [15–29]，而且通常已经点出具体对象。
- ❌ 三四句形容词堆砌的"重要性论证"，例如 "crucial / pivotal / critical role"，却没有一个数字。
- ❌ 引子写完不转向。最后一句必须把读者交给问题段。

---

### 2.2 研究问题 / 缺口 / "本文"（Question / Gap / This paper）

**任务**：说清楚本文问什么，以及为什么已有研究没回答。

**位置和规模**：出现率 85%（会计 100%）；第 1–2 段，相对位置 0.07；1 [1–1] 段；5 [4–7] 句；138 [92–159] 词；1 [0–3] 个引用。

**逐句骨架**（读了 10 段），常见两种走法：

*走法甲：先文献后本文*（缺口型，会计刊常用）
- **S1 已知**："Prior research establishes / As surveyed in [Paper], …"，带 1–2 个引用。
- **S2 未知**："What is less well known is… / However, the literature lacks…"，这一句通常很短。
- **S3 最近的一篇及其局限**（可选）："One important article is [Paper], which concludes [X]. However, [their evidence relies on Y]."
- **S4 本文**："In contrast, in this paper, we [exploit Z] to [directly test X]."
- **S5 为什么这种做法能回答问题**：数据或方法的优势。
- **S6 一句话答案预告**："We predict and find that…"

*走法乙：开门见山*（金融刊常用）
- **S1 本文**："In this paper, we study [object]." 只有 10–20 词。
- **S2 目标**："Our primary goal is to [X]."
- **S3 范围**：样本、时期、单位。
- **S4 一个规模数字**：例如样本单位从 [N1] 增长到 [N2]。

**信息要素**：
- 必含：
  - "本文"句（94%）：用一句话、30 词以内，你研究 [谁] 的 [什么行为或结果] 受 [什么] 影响？
- 常含：
  - 具名文献（62%）：与你最接近的 1–3 篇是哪几篇？各自结论是什么？
  - 明确缺口（41%）：它们**具体**没做什么？是没测量、没识别、没在这个情境里，还是结论有冲突？

**开头模板**：
1. `In this paper, we study whether [X] affects [Y].`
2. `This paper investigates the role of [X] in [setting/event].`
3. `Prior research establishes that [X]. What is less well known is [Y].`
4. `Despite the importance of [X] for [Y], there is limited evidence on [Z].`
5. `Although prior work on [X] examines [A], we study [B].`

**AI 腔错误**：
- ❌ 缺口写成空话："However, the literature remains limited / scarce." 要写清**哪一项**没做。
- ❌ 同一段里连续三句都在说 "this study aims to / seeks to / endeavors to"。只说一次，接下来直接写做法。
- ❌ 拖到第 3 段以后才说本文研究什么（版式 C 除外）。

---

### 2.3 理论 / 假设发展（Theory / Hypotheses）

**任务**：用一条因果链说明为什么 [X] 应该影响 [Y]，最后落成一个可检验的预测。

**位置和规模**：出现率 75%；相对位置 0.15–0.30（中位 0.23）；2 [1–3] 段；6 [4–7] 句；128 [102–167] 词；1 [0–3] 个引用。

**逐句骨架**（读了 10 段）：
- **S1 立论句**：短。"Our hypothesis is simple." 这样不到 5 词的句子在语料中真实存在。或 "There are [two] reasons why [X] may affect [Y]."
- **S2–S4 机制链**：每一步一句，因果连接词明确，用 "because / thereby / as a result"，一般附 1 个具名理论或文献。
- **S5 反方或限定条件**："However / On the other hand, [opposing force]."（对立预测 43%）。也可以是 "This effect is greater when [condition]."
- **S6 预测句**："Collectively / Therefore, we hypothesize that [prediction]." 有 H 编号的就在这里写 H1。
- 多个预测时，并列写 "First / Second / Third, [prediction]"，每个预测后接 "Thus, [observable implication]"。

**信息要素**：
- 必含：
  - 具名文献（73%）：你的机制建立在哪 1–3 篇理论或实证文献上？
- 常含：
  - 理论论证（67%）：从 X 到 Y 的因果链有哪 2–4 步？
  - 明写的假设（47%）：H1 用一句话怎么写？方向是什么？
  - 对立预测（43%）：有没有一个合理的反向力量？它预测什么？哪种力量占优是不是"事前不清楚"？

**开头模板**：
1. `Our central hypothesis is that [X] provides [agents] with [Y].`
2. `There are at least two reasons why [X] may have little effect on [Y].`
3. `On the one hand, [mechanism A] predicts [direction]. On the other hand, [mechanism B] predicts [opposite].`
4. `To motivate the empirical analysis, we draw on [theory/Paper].`
5. `Based on this framework, we hypothesize that [prediction] (H1).`

**AI 腔错误**：
- ❌ 只罗列 "Theory suggests that X may affect Y in several ways"，却没有一步一步的机制。
- ❌ 预测句之前没有反方。没有对立力量的假设段，读起来像结论先行。
- ❌ 编造被引文献的模型细节。工作表里没写某篇文献说了什么，就不要替它说。

---

### 2.4 数据与情境（Data & Setting）

**任务**：交代用什么数据、在什么情境里检验，以及这个情境为什么特别适合回答这个问题。

**位置和规模**：出现率 55%（会计 67%）；相对位置约 0.21；1 [1–2] 段；5 [4–6] 句；131 [110–163] 词。

**逐句骨架**（读了 10 段），常见两种：

*数据型*
- **S1 目的 + 数据**："To test [predictions], we build / use a [unique] dataset of [N] [units] from [source]."
- **S2 测量**：用这些数据怎么构造关键变量，例如频率、方法。
- **S3–S4 补充细节**：分类方法、子类别。
- **S5 合并**："Finally, we merge [data A] with [data B] from [source]."
- **S6 样本规模**："In our sample, [n] out of [N] [units] [satisfy condition]."

*情境型*
- **S1 总论**："[Setting] provides several advantages for identification."
- **S2 优势一**：时点外生，例如由法律预先确定。
- **S3 优势二**：交错实施或横截面变化，便于差分掉混杂因素。
- **S4 小结**："The identification strategy thus alleviates [specific concern]."
- **S5–S6 经济上为什么重要**：这个情境的规模或代表性。

**信息要素**（全部为"常含"，没有必含项）：
- 情境的好处（68%）：这个情境里什么东西是外生的、可观测的、或者别处拿不到的？
- 具名文献（64%）：数据或情境沿用了谁的做法？
- 数据来源（55%）：库名或机构名是什么？是不是手工收集？
- 观测数（50%）：N 是多少？单位是什么，例如公司-年、贷款、用户-股票-日？
- 变量构造（50%）：核心变量用什么方法测出来？
- 样本期（36%）：从哪一年到哪一年？

**开头模板**：
1. `To test these predictions, we use a [unique/hand-collected] dataset of [N] [units] from [source].`
2. `We test these predictions in [market/setting], where [variation] and [granular data] are both available.`
3. `[Setting] offers an ideal laboratory to study [X] because [reason].`
4. `Our sample comprises [N units] over [period].`

**AI 腔错误**：
- ❌ "We use a comprehensive and novel dataset." 形容词不能代替来源和数字。在全库每万词频次中，novel 只有 0.8 次，comprehensive 0.65 次。
- ❌ 只说"数据丰富"，不说为什么这个情境能识别。情境优势是最常见的信息要素（68%），一定要写。

---

### 2.5 实证设计（Empirical Design）

**任务**：用读者能复述的话讲清比较的是谁和谁、变化来自哪里。

**位置和规模**：出现率 45%（金融 52%）；相对位置约 0.35；1 [1–1] 段；4 [4–6] 句；121 [107–177] 词；0 [0–2] 个引用。

**逐句骨架**（读了 10 段）：
- **S1 设计名称**："Our main empirical strategy employs a difference-in-differences framework." 这类句子常常不到 10 词。
- **S2 变化来源**："We exploit [policy change] combined with cross-sectional differences in [exposure]."
- **S3 比较**："In particular, we compare [treated units] with [control units] before and after [event]."
- **S4 暴露怎么测**："To construct exposure groups, we rely on [source/measure]."
- **S5 固定效应和控制变量**（可选）："We include [unit × time] fixed effects to absorb [specific confound]."
- **S6 样本限制**（可选）：为排除某种混杂而做的筛选。

**信息要素**（都是"常含"）：
- 变量构造（67%）：处理强度或暴露变量怎么定义？
- 设计名称（44%）：是 DiD、IV、RD、事件研究还是实验？
- 具名文献（44%）：设计沿用了谁？
- 处理组和对照组（39%）：处理组是谁？对照组是谁？凭什么可比？
- 固定效应：用哪一层固定效应，吸收掉了什么？

**开头模板**：
1. `Our main empirical strategy employs a difference-in-differences design.`
2. `We compare [treated group] with [control group] before and after [event].`
3. `In our main specification, we regress [Y] on [X], controlling for [unit] and [time] fixed effects.`
4. `We measure [construct] using [data/method], following [Paper].`

**AI 腔错误**：
- ❌ 一句里堆满方法名："We employ DiD, PSM, IV, and entropy balancing to ensure robust causal identification." 主设计只写一个，其余放到稳健性段。
- ❌ 写 "rigorous / robust identification strategy"，却没说比较的是谁和谁。

---

### 2.6 识别挑战 / 为什么难（Identification challenge）

**任务**：主动说出审稿人最想问的那个混杂因素，以及你怎么排除它。

**位置和规模**：出现率 40%；相对位置约 0.46，**通常在主结果之后**；1 [1–1] 段；5 [4–7] 句；132 [96–173] 词。

**逐句骨架**（读了 10 段）：
- **S1 点名威胁**："One concern / A potential selection issue is that [confound]." 或 "There are [three] potential concerns for identification."
- **S2 展开偏误的方向**："That is, if [alternative], then [our estimate would be biased upward/downward]."
- **S3 对结论的威胁**："This would undermine our interpretation that [X]."
- **S4 应对**："To alleviate this concern, we [method/test]."
- **S5 结果**："We find that [the alternative test] yields the same conclusion." 通常是短句。
- 有多个威胁时，每个威胁走一遍 S1–S5，用 First / Second 分开。

**信息要素**：
- 必含：
  - 点名威胁（88%）：最可能的替代解释或混杂因素是什么？它会让估计偏向哪一边？
- 常含：
  - 具名文献（50%）：这个威胁是谁提出的？应对方法沿用了谁？
- 另需回答：
  - 你用什么检验来应对？
  - 那个检验的结果是什么？

**开头模板**：
1. `One concern with this interpretation is that [confound].`
2. `The key empirical challenge in testing this hypothesis is that [X] is [endogenous/unobservable].`
3. `There are [three] potential concerns for identification, which we address as follows.`
4. `Given that [X] is unobservable, it is challenging to [Y]. We address this by [Z].`

**AI 腔错误**：
- ❌ "Endogeneity is a common concern in corporate finance research." 泛泛而谈，没有点名具体的混杂。
- ❌ 只说担心，不给应对结果；或者只给方法名，不说方法解决了**哪个**偏误。
- ❌ 编造工具变量的排他性论证。工作表里没写，就不写。

---

### 2.7 主要发现（Main finding）

**任务**：用一句话说出主结果的方向，紧接着给出它有多大。

**位置和规模**：出现率 88%（金融 96%）；第一个结果段的相对位置中位 0.38；1 [1–2] 段；5 [4–6] 句；119 [91–153] 词；0 [0–1] 个引用。

**逐句骨架**（读了 10 段）：
- **S1 主结果**："We find that [X] [increases/reduces] [Y] following [event]." 常带设计前缀："Using [design], we find…"
- **S2 量级**："A one-SD / unit increase in [X] is associated with a [k]% change in [Y]." 在 10 段里有 6 段把数字放在 S2 到 S4 之间。
- **S3 第二个结果变量或在哪里更强**："The effect is particularly pronounced for [subgroup]."
- **S4 解释**："The results suggest that [interpretation]." 或 "Consistent with [H1/Paper], …"
- 也有一种变体：S1 写 "Our key finding is that [X]."，S2 写 "This result is notable for two reasons."（短句），S3–S4 写 First 和 Second。

**信息要素**：
- 必含：
  - 结果方向（91%）：主系数的符号是什么？对应哪个结果变量？
- 常含：
  - 百分比量级（51%）：主系数等于均值的百分之多少，或变化了百分之几？
  - 具名文献（40%）：结果与哪篇文献一致，或与哪篇冲突？
- 另需回答：显著性水平？结果对哪个子样本最强？

**开头模板**：
1. `We find that [treated units] [increase] [Y] by [k]% after [event].`
2. `Our key finding is that [X].`
3. `Consistent with our first hypothesis, we find that [X].`
4. `Using [design], we find that [X] [raises/lowers] [Y].`
5. `The paper reports three main findings. First, …`

**AI 腔错误**：
- ❌ "significantly improves / substantially increases" 却不给数字。工作表里有系数就必须写出来（v1.1 规则 W6）。人工标注集里有 47% 的主要发现段带数字，29/40 篇引言至少给出一个量级。
- ❌ "Taken together, these findings suggest…" 放在结果段末尾。可信段落集 117 篇中只有 11 篇用过 "taken together"（每千词 0.06 次），而对照实验的 12 篇生成稿里有 10 篇用了。
- ❌ 每个结果后面都复述一遍问题："This finding addresses our research question of whether…"。

---

### 2.8 经济量级（Magnitude / economic significance）

**任务**：把系数翻译成读者能感受的大小，并给出一个比较基准。

**位置和规模**：单独成段的只有 20%（8/40）；大多数情况下并在主要发现段的 S2–S3 里。单独成段时为 5 [4–6] 句，102 [87–209] 词。

**逐句骨架**（读了全部 8 段）：
- **S1 复述方向**：短句，例如 "We find results consistent with this prediction."
- **S2 宣告**："This effect is (also) economically significant." 通常只有 6–7 词，这是语料里真实存在的短句节奏。
- **S3 标准化**："A one-SD increase in [X] is associated with [k] [units], i.e., [m]% of the sample mean / SD."
- **S4 换算或基准**：
  - 换算成美元、基点或每年的数额："Since the average [unit] has [size], this amounts to [$] per [period]."
  - 或与已有估计比较："This compares with [k′] in [Paper]."
- **S5 稳健性一句**（可选）："This result is robust to [FE / alternative estimators]."

**信息要素**（单列段，n=8，都是"常含"）：
- 百分比（62%）：系数折合样本均值或基准的百分之几？
- 绝对单位（50%）：换算成 bp、美元或人数是多少？
- 比较基准（50%）：和样本均值、已有文献的估计或别的已知效应相比，大还是小？
- 标准差刻度（人工标注集 12% 的引言用到）：一个标准差的变化对应多少？

**开头模板**：
1. `This effect is economically significant: [X] corresponds to [m]% of the sample mean.`
2. `A one-standard-deviation increase in [X] is associated with a [k] bp [rise] in [Y].`
3. `Given a sample mean of [μ], this estimate implies a [m]% [increase].`
4. `Relative to [benchmark/estimate in Paper], this effect is [larger/comparable].`

**AI 腔错误**：
- ❌ "The effect is not only statistically significant but also economically meaningful." 说了等于没说，后面必须跟数字。
- ❌ 把同一个数字在摘要式的段落里重复三次。

---

### 2.9 补充结果 / 异质性（Additional results / Heterogeneity）

**任务**：沿一个**有理论理由**的维度切分样本，说明效应在哪里更强，借此支持机制。

**位置和规模**：出现率 80%（金融 88%）；相对位置约 0.61；1 [1–2] 段；5 [4–6] 句；132 [101–157] 词。

**逐句骨架**（读了 10 段）：
- **S1 序列词 + 维度**："Next / Second, we examine whether the effect varies with [dimension]."
- **S2 理论理由**："[Theory/Paper] predicts that [dimension] should [amplify/dampen] the effect."
- **S3 怎么测这个维度**："We measure [dimension] using [proxy]."
- **S4 结果**："We find that the effect is stronger when [condition]."
- **S5 收束**：短句，例如 "These results are consistent with our theoretical predictions."
- 有两个维度时，在 S3 之后用 "First, … Second, …" 并列，每个维度给一个测量和一个结果。

**信息要素**：
- 必含：
  - 维度（78%）：按什么维度切分？为什么理论预测效应在这里不同？
- 常含：
  - 具名文献（47%）：这个维度的理论依据出自谁？
  - 方向（38%）：哪一组更强？强多少？

**开头模板**：
1. `We next examine whether the effect varies with [dimension].`
2. `Consistent with [mechanism], the effect is stronger when [condition].`
3. `To understand [X], we exploit three sources of heterogeneity.`
4. `Second, we find that [subgroup] [responds more strongly].`

**AI 腔错误**：
- ❌ 只列维度、不给理由："We also examine heterogeneity across firm size, age, and industry."
- ❌ 所有段都以 "Furthermore / Moreover / Additionally" 开头。全库每万词只有 2.6、1.7、0.7 次，三者合计每千词不超过约 0.5 次。

---

### 2.10 机制（Mechanism）

**任务**：一次检验一个渠道，每个渠道都给出可证伪的预测和明确的结论。

**位置和规模**：出现率 55%；相对位置约 0.55；2 [1–3] 段；5 [4–7] 句；133 [107–163] 词；1 [0–2] 个引用。

**逐句骨架**（读了 10 段）：
- **S1 总起**："We consider and test [N] possible mechanisms." 或 "As a deeper test of the mechanism, we examine [X]."
- **S2 渠道假说**："We first test the hypothesis that [channel]."
- **S3 可检验的含义**："According to this hypothesis, [Y] should [rise] but [Z] should not."
- **S4 检验**："To test these implications, we analyze [data/split]."
- **S5 结论句**：通常 6–12 词，例如 "Our evidence does not support this channel." 或 "The results confirm these predictions."
- **S6–S7 支撑细节**：两三个具体结果。
- **常规做法**：一个渠道一段，每段都以结论收尾。被排除的渠道也写，而且要写清是被哪项证据排除的。

**信息要素**：
- 必含：
  - 渠道名称（91%）：你认为 X 通过什么影响 Y？有哪些候选渠道？
  - 具名文献（73%）：每个渠道的理论来源是谁？
- 另需回答：每个渠道各预测什么，以及哪项检验能把它和其他渠道区分开？结论是支持还是排除？

**开头模板**：
1. `As a deeper test of the mechanism, we examine [X].`
2. `To test whether [channel] drives the result, we focus on [subsample/agents].`
3. `We consider and test [four] possible mechanisms.`
4. `The first class of explanations is that [X]. If so, [prediction].`

**AI 腔错误**：
- ❌ "This may be driven by several mechanisms, such as information asymmetry, agency costs, and financing constraints." 列了一串渠道，一个都没检验。
- ❌ 机制只有"支持"，没有"排除"。语料里常见 "does not support" 这类句子。
- ❌ 限定语叠用："may potentially suggest"。一处不确定只写一次限定（见 3.3）。

---

### 2.11 稳健性 / 替代解释（Robustness / Alternative explanations）

**任务**：用最少的字排除最具威胁的替代解释。

**位置和规模**：出现率 60%；相对位置约 0.61；1 [1–2] 段；4 [3–6] 句，**是最短的内容段**；116 [81–157] 词。

**逐句骨架**（读了 10 段）：
- **S1 承认**："We acknowledge that [other factor] could also [explain Y]." 或 "We employ a battery of checks to rule out [alternatives]."
- **S2 宣告**："We explicitly check whether these factors subsume our findings." 短句。
- **S3–S5 每项检验一句**：检验和结果写在同一句里，例如 "Our results hold for [subsample/cut-off]." 这几句一般 12–20 词，节奏短促。
- **S6 安慰剂或伪造检验**（有的话放在这里）："A falsification test finds no effect in [placebo period]."
- **S7 收束**："Thus, the change is most likely attributable to [X] rather than [alternative]."

**信息要素**（都是"常含"）：
- 排除了哪些替代解释（67%）：最强的两个替代解释是什么？分别用哪项检验排除？
- 检验清单（46%）：换度量、换样本、换估计方法，各做了哪些？
- 设计名称（42%）：做安慰剂、前趋势或事件研究图了吗？结果如何？

**开头模板**：
1. `Our results are robust to [alternative measures/samples/estimators].`
2. `We also examine several alternative explanations. First, [X].`
3. `A falsification test using [placebo period/sample] finds no effect.`
4. `We acknowledge that [factor] could also explain [Y]; we show that [test result].`

**AI 腔错误**：
- ❌ 写成很长的清单段："Our results are robust to alternative measures, alternative samples, alternative specifications, alternative clustering, and alternative time windows." 这些检验应该放到正文。引言只写能排除**具体**替代解释的那两三项。
- ❌ 用 "robust" 形容结论本身："our robust findings"。

---

### 2.12 贡献 / 文献定位（Contribution）★ 重点

**任务**：每段对接一条文献脉络：点名这条脉络里的具体论文，用一句话说出本文与它们的差别。

**位置和规模**：
- 出现率 90%（会计 100%）。
- 3 [2–3] 段，约 2 [1–3] 条脉络。
- 起点在相对位置 0.71 [0.29–0.85]；75% 连成一整块；31/36 篇最后三段里有贡献段。
- 每段 5 [4–6] 句，131 [96–171] 词。
- **每段点名约 4 篇文献 [2–6]**。

**几个关键数字** [数据，人工标注集 n=36 篇有贡献段]：

| 指标 | 数值 | 怎么用 |
|---|---|---|
| 至少一段说清差异的引言 | 89% | 必须做 |
| 中位引言里说清差异的段落比例 | 67% | 不必每段都写 "In contrast"，但多数段要写 |
| 先宣布条数（"makes three contributions"） | 47%（金融 29%，会计 73%） | 投会计刊建议宣布 |
| 有"首次"类声明 | 25% 的引言 | 可信段落集的文本里，"we are the first" 只出现在 3/117 篇，"to the best of our knowledge" 只有 5/117 篇。少用，而且要有依据 |
| 段块结构 | 一条脉络一段 | 不要一段里塞三条脉络 |

**逐句骨架**（读了 10 段）：
- **S1 点名脉络**："[Second], our paper contributes to the literature on [topic] ([Paper A]; [Paper B])."，或 "Our paper is related to studies that [do X]."
- **S2–S4 逐篇说它们做了什么**：叙述式引用作主语，每篇用一个**具体动词**和一个具体结论。例如 "[Paper A] show that [finding]. [Paper B] find that [finding]." 一句可以放一篇，也可以放两篇。
- **S5 转折**："While this research shows [A], [what remains open]." 或 "This literature has focused on [A], whereas our focus is on [B]."
- **S6 本文**："We contribute by showing that [our specific result]."
- **S7 外延**（可选）：对这条脉络或政策争论的含义。

**差异的五种写法**（任选，但要具体到对象、数据、识别或结论）：

| 差异类型 | 模板 |
|---|---|
| 换研究对象 | `[Paper] study [A]; we study [B], where [why B matters].` |
| 换测量 | `Whereas [Paper] proxy [X] with [aggregate measure], we observe [X] directly at the [unit] level.` |
| 换识别 | `[Papers] document a correlation between [X] and [Y]; we exploit [shock] to identify its causal effect.` |
| 结论冲突 | `Our evidence contrasts with [Paper], who find [opposite]; the difference arises because [reason].` |
| 扩展边界 | `We extend [Paper]'s finding to [new setting/outcome], showing that [result].` |

**开头模板**：
1. `Our paper makes [three] contributions. First, we contribute to the literature on [topic].`
2. `We also contribute to the growing literature on [topic] ([Paper A]; [Paper B]; [Paper C]).`
3. `This paper relates most closely to [Paper A] and [Paper B], who [do X]. In contrast, we [Y].`
4. `Relative to this literature, our contribution is to [specific action/result].`
5. `Second, our study adds to work on [topic] by documenting [result].`

**信息要素**：
- 必含：
  - 具名文献（97%）：这条脉络里你要点名哪 2–5 篇？**每篇发现了什么？**（这一项必须由你在工作表里填，模型不许补。）
  - 差异（89%）：本文和它们差在对象、测量、识别、结论冲突还是外延？用一句话写。
  - 脉络名称（75%）：这条文献脉络叫什么？
- 常含：
  - 宣布条数（36% 的段块）：一共几条贡献？
  - 重述缺口（33%）：这条脉络缺的东西，和第 2 段说的缺口是不是同一个？

**AI 腔错误**：
- ❌ **只堆引用、不说差别**："Our paper contributes to the literature on X (A, 2010; B, 2012; C, 2015; D, 2018; E, 2020)." 可信段落集中，带年份的括号引用共 2,047 处，其中 89% 只有 1–2 个年份，5 个及以上年份的只有 2.3%（自动计数，近似）。
- ❌ "enriches / extends / deepens our understanding of" 收尾，却没说具体推进了什么。
- ❌ 被引文献的观点或方法是模型补的。对照实验第 1 轮的编造大多出在这里。
- ❌ 每段都用 "To the best of our knowledge, we are the first…"。

---

### 2.13 政策 / 理论含义（Implications）

**任务**：说明结果会改变谁的决策，或者改变学界对哪个结论的解读。

**位置和规模**：出现率 38%（金融 44%）；相对位置约 0.82，常夹在贡献段中间；1 段；5 [3–6] 句；117 [96–145] 词。

**逐句骨架**（读了 10 段）：

*政策型*
- **S1 宣告**：短，6–10 词，例如 "Finally, our paper has policy implications."
- **S2 现行做法或假定**：政策制定者当前怎么假定或怎么做，常带一个数字或规则。
- **S3 本文结果意味着什么**："Our findings imply that [policy] may also [affect Z]."
- **S4 可操作的抓手**：哪个制度参数在政策制定者手里。

*理论解读型*
- **S1**："Our results have implications for how the literature interprets [X]."
- **S2 通行看法**：一般怎么认为。
- **S3 推断错在哪里**："One could erroneously conclude that [X]."
- **S4 本文结果**："In contrast, our findings show that [Y]."

**信息要素**（都是"常含"）：
- 政策含义（60%）：哪个监管者或哪项政策会因你的结果而改变？现行规则或假定是什么？
- 理论含义（33%）：你的结果挑战或支持哪类模型？
- 解读（33%）：你希望读者对哪个已有结论换一种理解？

**开头模板**：
1. `Finally, our results have implications for [regulator/policy].`
2. `Our findings inform the debate on [policy question].`
3. `Our results have implications for how the literature interprets [X].`

**AI 腔错误**：
- ❌ "Our findings offer valuable insights for policymakers, investors, and managers." 一句话照顾三类读者，结果对谁都没说具体的事。
- ❌ 含义超出证据：只有相关性，却写 "policymakers should mandate…"。

---

### 2.14 路线图（Roadmap，可选）

**任务**：一节一句，告诉读者每节**具体**讲什么。

**位置和规模**：可信段落集中 44% 有（金融 52%，会计 30%），而且总在最后一段；55 [43–87] 词；5 [5–6] 句，人工标注集为 6 [5–6] 句、54 [47–61] 词。

**逐句骨架**（读了 10 段）：
- **S1**："The remainder of the paper is organized as follows." 5–9 词。
- **S2 至 S(n−1)**：一节一句，每句 5–20 词，说出这一节的具体内容，例如 "Section 2 describes [the X data] and [the Y setting]."。
- **S(n)**："Section [N] concludes." 只有 3 词。

**信息要素**：
- 必含：章节清单（100%）：每一节具体讲什么？

**模板**：
1. `The remainder of the paper is organized as follows. Section 2 describes [institutional setting]. Section 3 presents [data and sample]. … Section [N] concludes.`
2. `The paper proceeds as follows.`

**AI 腔错误**（盲判点名过）：
- ❌ **空路线图**：把章节压成一个范围，例如 "Sections 2 to 7 present the analyses"；或只写 "Section 3 presents the results" 这种没有信息的句子。语料中的路线图也是一节一句，但每句都说出该节的**具体对象**。
- ❌ 元叙述：例如 "This overview sets up…"、"Readers should keep in mind…"。
- ❌ 路线图前面再加一段"总结前文"的过渡。
- ✅ 不写路线图也完全可以：56% 的引言没有。

---

### 2.15 贯穿全篇的 AI 腔清单（盲判线索汇总）

对照实验里，判官认出生成稿的线索全部是"凑字"痕迹（`spec_ablation_report_20261020.md`）：

| 错误 | 表现 | 改法 |
|---|---|---|
| 空路线图 | "organized across Sections 2 to 7" | 一节一句写具体对象，或者干脆不写 |
| 复述凑字 | 每个结果段末尾把前面的结论重说一遍 | 删掉。段长靠细节撑，不靠复述 |
| "Taken together" 总结 | 12 篇生成稿中 10 篇出现；人类 117 篇中 11 篇出现 | 删掉总结句，直接进入下一段的新信息 |
| 引用堆在括号里不说差别 | "(A; B; C; D; E)" | 拆成叙述式，每篇一个动词加一个发现，再写一句差异 |
| 宏大开篇 | "In recent years, … increasing attention" | 第一句写对象本身或一个数字 |
| 元叙述 | "This overview sets up…"、"It is worth noting…"（全库每千词 0.06 次） | 删掉 |
| 每段同一种开头 | 连续用 "Furthermore / Moreover / Additionally" | 换成 "We also / Next / Second, / In contrast" |
| 段内句长相同 | 每句都 22–26 词 | 见 3.1：每段放一句短判断句 |

---

## 三、微观：句子层面的规则

口径：
- 3.1 节新增的统计，在 117 篇可信引言的重建文本上计算，句子切分与 `rebuild_paras.py` 相同。
- 其余数据来自全库 267 篇，见 `EN_writing_spec_v1.md` 第三章。

### 3.1 句长与变化 [数据]

| 指标 | 数值（117 篇，中位 [四分位]） |
|---|---|
| 平均句长 | 25.5 词 [21.6–29.8] |
| 每篇引言句长的标准差 | **10.7 词** [9.6–12.0]；变异系数约 0.4 |
| 超过 40 词的句子占比 | 8.6% [5.5–12.3] |
| 不足 12 词的句子占比 | 8.2% [5.2–13.2] |
| 段内最短句（段落 ≥3 句，n=1,534 段） | 14 词 [10–18] |
| 段内最长句 | 37 词 [31–44] |
| 含一句不足 12 词短句的段落 | 33% |
| 引言第一句 | 20 词 [15–29] |

**规则**：
- **每段都要有长短落差**：典型的段落最短句约 14 词，最长句约 37 词。如果一段里每句都在 22–28 词，就是 AI 节奏。
- **短句承担判断**：例如 "This effect is economically significant."、"Our evidence does not support this channel."、"My hypothesis is simple."。大约每三段出现一次不足 12 词的短句，不必每段都有。
- **长句承担设计细节**：样本构造、变量定义、控制变量清单。上表的 8.6% 来自 PDF 抽取文本，被拼进正文的脚注撑高了。第 8 轮把 5 篇原文去噪后，超过 40 词的句子只有 2.2%，平均句长 21 词，不足 12 词的约 16%。实际目标取**约 3–4% 超过 40 词**（`round8/REPORT.md`）。
- **不要为了节奏造句**：v1.1 规范已经指出，句长离散度只作下限检查，标准差不应低于 8，不作为优化目标。

### 3.2 "we" 的用法 [数据，v1.1 §3.2]

- 全库引言和结果节中，we/our/us 每千词约 18 次，稳健性节约 23 次。顶刊大量用 "we"。
- 被动句占 15–19%，集中在数据处理描述中。
- **规则**：
  - 研究动作用 "we" 作主语，例如 *We exploit, We find, We show*。
  - 数据处理可以用被动，例如 *Firms are excluded if…*。
  - 不要全改成 "this paper / the authors"。
  - 独作论文用 "I" 或 "my" 的也常见。
- 对照实验里，无规范稿的 we/our 密度只有每千词约 3.6 次，原文约 10 次。生成时要有意多用 "we"。

### 3.3 限定语与证据强度匹配 [数据 + 编辑，v1.1 §3.4]

引言中每千词：
- *associated with / correlated / consistent with*：2.3 次
- *suggest*：1.2 次
- *causal / leads to*：0.8 次
- 增强语（*strongly, clearly*）：不到 1 次

| 你的证据 | 可用的动词 | 不要用 |
|---|---|---|
| DiD、IV、RD、随机化、自然实验 | *causes, increases, reduces, the effect of* | *may be associated with*（太弱） |
| 带固定效应的面板 OLS，没有外生变化 | *is associated with, predicts, is consistent with* | *causes, leads to*（太强） |
| 机制推测，未直接检验 | *suggests, may, is consistent with the view that* | *shows, demonstrates* |

- 规则是双向的：动词不能强于证据，也不必弱于证据。
- 一处不确定只写一次限定，不要写 "may potentially suggest"。
- 会计刊常加一句因果局限，例如 "establishing causality is difficult"（局限段在会计刊占 20%）。

### 3.4 引用格式 [数据，v1.1 §3.5 + 新增计数]

- **金融刊以叙述式为主**：每千词叙述式 5.7–10.8 次，括号式 1.5–2.4 次。被引文献作句子主语，例如 *[Author] (Year) show that…*。
- **会计刊**：TAR、CAR 括号式更多，每千词 4.7–5.4 次。JAR 的格式是方括号年份，例如 *Author [2017]*。
- 引言中引用总密度约每千词 8 次。贡献段每段约 4 篇 [2–6]，主要发现段和稳健性段基本不引（0 [0–1]）。
- **括号里的篇数**：可信段落集中，带年份的括号引用共 2,047 处；89% 只有 1–2 个年份，≥3 个的占 11%，≥5 个的占 2.3%（按年份自动计数，近似）。**一个括号最多放 3 篇**；要放更多，就拆成叙述句。
- 只引用工作表或文献库里真实存在的条目，没有可用引用时宁可不写。

### 3.5 数字与量级的写法 [数据]

- 引言中每千词有 2.4 处百分比、基点或百分点（全库）；人工标注集 29/40 篇引言至少给一个量级。
- 量级形式的使用比例（人工标注集，按引言计）：
  - 百分比变化（含"占均值的百分比"）：60%
  - 绝对单位（bp、美元、美分、比率）：35%
  - 与基准比较（样本均值、已有估计、别的已知效应）：22%
  - 标准差刻度：12%
- 数字出现的位置：主要发现段 26 处，异质性段 12 处，单列的量级段 8 处，其余各段零星出现。

**写法规则** [编辑]：
- **百分比**：`[X] increases [Y] by [k]%` 或 `by [k] percentage points`。比率变化写 %，比例本身的差写 pp，不要混用。
- **基点或绝对单位**：利差和收益率用 bp，金额用 $ 加单位（million 或 billion），写明期间，例如 "per month"。
- **相对均值**：`[k] bp, or [m]% of the sample mean of [μ]`。先给原始单位，再给相对值。
- **标准差刻度**：`A one-standard-deviation increase in [X] is associated with …`。说明是 X 的标准差，必要时说明是哪个样本的。
- **占比与份额**：`[n] of [N] [units] ([s]%)`，分子分母都写出来。
- **一个结果最多给两种刻度**，例如原始单位加相对均值，不要把四种刻度一起堆上。
- **数字只能来自工作表或结果表。**

### 3.6 脚注：什么放进脚注 [数据 + 编辑]

- [数据] 可信段落集中 91% 的引言有脚注标记，中位 6 个 [3–8]（金融 6，会计 5；MS 和 TAR 约 3 个）。
- [编辑] 脚注**内容**我没有统计，因为重建时脚注被整体剔除了。下面的分工是行业惯例：

| 放进脚注 | 留在正文 |
|---|---|
| 变量定义的技术细节、数据清洗规则 | 核心变量是什么、怎么测（一句） |
| 次要文献，以及"另见 X、Y" | 贡献段要对话的 2–5 篇近邻文献 |
| 次要稳健性的结果（"results are similar when…"） | 排除最强替代解释的那一两项检验 |
| 制度细节的来源、法规条文编号 | 制度对识别为什么重要 |
| 对审稿人可能追问的小问题的预先回答 | 主要识别威胁 |
| 数字的计算过程，例如量级怎么换算 | 换算后的量级本身 |

- **规则**：一篇引言 4–8 个脚注。每个脚注只回答一个问题，在正文中放在句末标点之后。
- 不要用脚注藏主要结果或主要文献差异。

### 3.7 用词底线 [数据，v1.1 §3.6]

- **不用**：delve, landscape, realm, intricate, tapestry（全库每万词约 0 次）；pivotal, underscore, nuanced（约 0.1 次）。
- **慎用**：
  - novel：0.8 次/万词，不要用来形容自己的研究；
  - comprehensive：0.65；
  - crucial：0.5；
  - notably：0.5；
  - shed light on：0.4。
- *leverage* 和 *robust* 是金融术语，不是 AI 腔。
- 不写 "It is worth noting"（每千词 0.06 次）和 "Interestingly"（0.04 次）。

---

## 四、空白工作表（新版 Content Brief）

**填写规则**：
- **【必】**：必填。填不出来就说明内容还没准备好，先别写引言。
- **【选】**：有就填，没有就写"无"，模型会跳过对应句子。
- 所有数字都要写上来源，例如"表 3 第 2 列"。

### A. 基本信息

| # | 问题 | 必/选 |
|---|---|---|
| A1 | 目标期刊；金融刊还是会计刊 | 【必】 |
| A2 | 选用的版式（A 线性 / B 循环 / C 前置 / D 理论），一句话说理由 | 【必】 |
| A3 | 单作者还是多作者（决定用 I 还是 we） | 【必】 |
| A4 | 计划段数和总词数（默认 14 段、约 1,850 词） | 【选】 |

### B. 引子与问题（第 1–2 段）

| # | 问题 | 必/选 |
|---|---|---|
| B1 | 研究对象是什么（一个名词短语） | 【必】 |
| B2 | 开篇事实：一个数字、事件或制度特征，注明来源和年份 | 【选】（金融刊建议填） |
| B3 | 张力或疑问：标准理论或常识预测什么，现实中哪里对不上 | 【选】 |
| B4 | **"本文"句**：我们研究 [谁] 的 [什么] 是否和如何受 [什么] 影响，30 词以内 | 【必】 |
| B5 | 一句话答案预告（主结果的方向） | 【必】 |
| B6 | 最接近的 1–3 篇文献：作者（年份）、它们的结论、它们**具体**没做什么 | 【必】（版式 C 需要 2–5 篇） |
| B7 | 缺口类型：没测量 / 没识别 / 没在这个情境 / 结论冲突 / 其他 | 【必】 |

### C. 理论与假设

| # | 问题 | 必/选 |
|---|---|---|
| C1 | 从 X 到 Y 的因果链，分 2–4 步写，每步一句 | 【必】（理论段占 75%） |
| C2 | 每一步的理论或文献依据：作者（年份）加它说了什么 | 【必】 |
| C3 | 反向力量：什么机制会预测相反方向或零效应 | 【选】（43% 的引言有） |
| C4 | 假设句（H1、H2…），写明方向 | 【选】（会计刊建议填） |
| C5 | 理论模型的设定和结论（仅版式 D 需要）：主体、摩擦，以及 3–5 个结论 | 【选】 |

### D. 数据与情境

| # | 问题 | 必/选 |
|---|---|---|
| D1 | 冲击、政策或情境的名称，以及发生时间（如有交错实施，列出时间表） | 【必】（若使用外生变化） |
| D2 | 这个情境为什么适合识别：2–3 条理由，例如时点外生、交错实施、可观测性 | 【必】 |
| D3 | 数据来源：库名或机构名，是否手工收集 | 【必】 |
| D4 | 样本期：起止年份 | 【必】 |
| D5 | 观测数 N 和观测单位，例如"公司-季度"或"贷款" | 【必】 |
| D6 | 样本筛选的关键条件和剩余规模 | 【选】 |
| D7 | 核心变量（X、Y）怎么测：一句话定义，并说明沿用了谁的做法 | 【必】 |

### E. 设计与识别

| # | 问题 | 必/选 |
|---|---|---|
| E1 | 设计名称：DiD / 交错 DiD / IV / RD / 事件研究 / 实验 / 结构估计 | 【必】 |
| E2 | 处理组是谁，对照组是谁，凭什么可比 | 【必】（因果设计时） |
| E3 | 估计方程的文字版："把 [Y] 对 [X] 回归，控制 [固定效应]" | 【必】 |
| E4 | 固定效应和聚类层级 | 【必】 |
| E5 | 最主要的识别威胁：它是什么，会让估计偏向哪边 | 【必】 |
| E6 | 应对 E5 的检验，以及**检验结果** | 【必】 |
| E7 | 第二个和第三个识别威胁，各自的应对和结果 | 【选】 |

### F. 结果

| # | 问题 | 必/选 |
|---|---|---|
| F1 | 主结果：方向、对应的结果变量、显著性 | 【必】 |
| F2 | **主系数**（原始单位）和来源（表/列） | 【必】 |
| F3 | 主系数折合**样本均值的百分之几**；同时写出样本均值 | 【必】 |
| F4 | 第二种刻度（任选一种）：一个标准差的效应 / bp / 美元 / 与已有估计比较（写明文献和它的数字） | 【选】 |
| F5 | 第二个结果变量和它的结果 | 【选】 |
| F6 | 版式 B：每个后续检验的设计（一句）和结果（含数字） | 【选】 |
| F7 | 异质性维度 ①：维度、理论理由、测量、哪组更强、强多少 | 【必】（80% 的引言有） |
| F8 | 异质性维度 ② | 【选】 |
| F9 | 每个候选机制：名称、理论来源、可检验的预测、检验方法、结论（支持或排除） | 【必】至少 1 个 |
| F10 | 稳健性：最强的两个替代解释，以及排除它们的检验和结果 | 【必】 |
| F11 | 安慰剂、前趋势或伪造检验的结果 | 【选】 |
| F12 | 其余稳健性检验清单（会写进正文或脚注） | 【选】 |

### G. 贡献（每条脉络一组，2–3 组）

| # | 问题 | 必/选 |
|---|---|---|
| G1 | 一共几条贡献；是否在段首宣布条数（会计刊建议宣布） | 【必】 |
| G2-k | **第 k 条脉络的名称** | 【必】 |
| G3-k | 这条脉络要点名的 **2–5 篇文献**：每篇写"作者（年份）——它发现了什么（一句）" | 【必】 |
| G4-k | **本文与它们的差别**（一句话），注明是对象、测量、识别、结论冲突还是外延 | 【必】 |
| G5-k | 本文在这条脉络里的具体结果，引用 F 部分对应的格子 | 【必】 |
| G6 | "首次"类声明及其依据（没有依据就写"无"） | 【选】 |

### H. 含义、局限、路线图与脚注

| # | 问题 | 必/选 |
|---|---|---|
| H1 | 政策含义：哪个监管者，现行规则或假定是什么，结果意味着要改什么 | 【选】 |
| H2 | 理论含义：挑战或支持哪类模型或结论 | 【选】 |
| H3 | 局限：因果判断或外推的边界（会计刊建议写一句） | 【选】 |
| H4 | 是否写路线图；写的话，各节标题和每节的具体内容 | 【选】 |
| H5 | 准备放进脚注的 4–8 件事：变量细节、次要文献、次要稳健性、制度来源 | 【选】 |

---

## 五、示范：一篇虚构论文

> **以下论文、政策、数据和数字全部是虚构的**，只用来演示怎么填和怎么排，与任何真实论文无关。

### 5.1 填好的工作表（节选关键格）

| # | 填写内容 |
|---|---|
| A1 | 金融刊（假设投 JFQA） |
| A2 | 版式 A（线性）：一个主设计，结果逐层递进 |
| A3 | 多作者，用 we |
| B1 | 中小企业银行贷款利率 |
| B2 | 虚构的"Regional Credit Registry Pilot (RCRP)"在 2014–2019 年分四批覆盖 120 个城市，入库企业从 0 增至约 85 万家 |
| B4 | We study whether access to a shared public credit registry lowers the loan spreads that banks charge small firms. |
| B5 | 是的，降低了，而且主要发生在缺乏既有银行关系的企业身上 |
| B6 | [Author A (Year)]：跨国层面，信用信息共享与私人信贷规模正相关，但无法排除同时期的其他改革。[Author B (Year)]：单一国家，研究时点只有一个 |
| B7 | 没识别（只有跨国相关）；没有贷款层面的价格 |
| C1 | 登记系统降低银行获取企业信用信息的成本 → 新进入银行的信息劣势缩小 → 关系银行的信息租金下降 → 利差下降 |
| C2 | 信息租金理论 [Author C (Year)]；信息共享与竞争 [Author D (Year)] |
| C3 | 反向力量：坏信用记录被公开，部分企业的利差可能上升 |
| D1 | RCRP，2014、2015、2017、2019 年分四批，批次由中央部门按行政编号排序决定 |
| D2 | ① 批次顺序与当地信贷周期无关；② 交错实施，可以做城市内的前后对比；③ 有贷款层面的合同利率 |
| D3 | 虚构的"某商业银行联合贷款合同库" |
| D4 | 2011–2021 |
| D5 | 约 412,000 笔贷款，覆盖 96,000 家企业 |
| E1 | 交错 DiD（Callaway–Sant'Anna 类估计量） |
| E2 | 处理组：已纳入试点城市的企业；对照组：尚未纳入的城市的企业 |
| E4 | 企业固定效应 + 银行 × 季度固定效应，按城市聚类 |
| E5 | 威胁：试点城市同时期的地方信贷扩张会压低利率，估计偏向"效果更大" |
| E6 | 加入城市 × 季度的贷款总量控制；在只看同一银行、同一季度、跨城市的样本里，结果不变 |
| F2 | 利差下降 18 bp（表 3 第 2 列） |
| F3 | 样本均值利差 240 bp → 下降约 7.5% |
| F4 | 一个标准差的登记覆盖率提升，对应约 11 bp |
| F7 | 维度：企业是否已有关系银行。无关系的企业下降 29 bp，有关系的下降 6 bp（不显著） |
| F9 | 机制 ① 信息租金：新进入银行的放贷份额上升 → 支持；机制 ② 风险重定价：高风险企业利差未上升 → 不支持"仅仅是重新分类" |
| F10 | 替代解释 ①：同期的地方担保基金 → 剔除有担保的贷款后结果不变。替代解释 ②：银行业竞争本身增强 → 控制城市银行网点数后结果不变 |
| F11 | 事件研究：试点前 8 个季度的系数均不显著 |
| G1 | 三条贡献，金融刊，不宣布条数 |
| G2-1 / G3-1 / G4-1 | 信用信息共享。[A (Year)] 跨国相关；[B (Year)] 单一时点；[E (Year)] 测的是贷款规模而不是价格。差别：贷款层面的价格，加交错的外生实施 |
| G2-2 / G3-2 / G4-2 | 关系借贷与信息租金。[C (Year)] 理论；[F (Year)]、[G (Year)] 用关系长度作代理。差别：用一次外生的信息冲击，直接检验租金 |
| G2-3 / G3-3 / G4-3 | 中小企业融资政策评估。[H (Year)]、[I (Year)] 研究担保和补贴。差别：信息基础设施这种不花财政钱的政策工具 |
| H1 | 为是否推广登记系统提供依据：效果集中在无关系企业 |
| H4 | 写路线图，共 6 节 |

### 5.2 段落地图（版式 A，15 段，约 1,800 词）

| 段 | 功能 | 用到的格子 | 句数 | 骨架要点 |
|---:|---|---|---:|---|
| 1 | 引子 | B1, B2 | 5 | S1 中小企业融资贵（短）；S2 RCRP 的规模数字；S3 信息共享的两种观点；S4 现有证据只到跨国层面；S5 转向：价格是否下降仍未知 |
| 2 | 问题/本文 | B4–B7 | 5 | S1 "In this paper, we study…"；S2 B6 的近邻文献和它的局限；S3 本文的做法（交错试点）；S4 贷款层面的价格数据；S5 答案预告 |
| 3 | 理论 | C1, C2 | 6 | S1 "Our central hypothesis is that…"；S2–S4 信息租金链条；S5 C3 反向力量；S6 "Therefore, we expect…" |
| 4 | 数据与情境 | D1–D5 | 5 | S1 RCRP 分批；S2 为什么外生；S3 交错实施的好处；S4 数据来源；S5 N 和样本期 |
| 5 | 设计 | E1–E4 | 4 | S1 交错 DiD（短）；S2 处理组和对照组；S3 固定效应；S4 估计量的选择 |
| 6 | 主要发现 + 量级 | F2–F4 | 5 | S1 "We find that…" 方向；S2 18 bp，占均值的 7.5%；S3 标准差刻度 11 bp；S4 事件研究图；S5 短句判断 |
| 7 | 识别挑战 | E5, E6 | 5 | S1 点名同期信贷扩张；S2 偏误方向；S3 对结论的威胁；S4 应对；S5 结果（短） |
| 8 | 异质性 | F7 | 5 | S1 "We next examine…"；S2 理论理由；S3 测量；S4 29 bp 对 6 bp；S5 收束短句 |
| 9 | 机制 ① | F9-① | 5 | S1 总起；S2 假说；S3 预测；S4 检验；S5 "The results support…" |
| 10 | 机制 ② | F9-② | 5 | S1 替代渠道；S2 预测；S3 检验；S4 结果；S5 "does not support" |
| 11 | 稳健性 | F10, F11 | 4 | S1 承认两个替代解释；S2 剔除担保贷款；S3 控制网点数；S4 前趋势 |
| 12 | 贡献 ① | G-1 | 5 | 点名 A、B、E，说清它们的发现，差别是价格加外生实施 |
| 13 | 贡献 ② | G-2 | 5 | 点名 C、F、G，差别是外生信息冲击 |
| 14 | 贡献 ③ + 政策 | G-3, H1 | 5 | 点名 H、I，差别是不花财政钱的工具；政策含义一句 |
| 15 | 路线图 | H4 | 5 | 一节一句，写明各节具体内容 |

"本文"句在第 2 段；第一个结果在第 6 段（相对位置 5/14 = 0.36）；贡献在最后四段；路线图在最后。四个锚点都落在区间内。

### 5.3 两段示范（虚构内容，演示骨架）

**第 6 段（主要发现 + 量级）**

> We find that loan spreads fall after a city joins the registry. Firms in treated cities pay 18 basis points less on new loans than comparable firms in not-yet-treated cities, a 7.5% decline relative to the sample mean of 240 basis points. Scaled differently, a one-standard-deviation increase in registry coverage is associated with an 11 basis point lower spread. The event-study estimates show no differential trend in the eight quarters before inclusion, and the decline appears within two quarters after it. The effect is economically large.

句长依次为 12、30、17、22、5 词（按空格切分）。前四句在 12–30 词之间起伏，最后一句是 5 词的判断句。

**第 12 段（贡献 ①）**

> First, we contribute to the literature on credit information sharing. [Author A (Year)] show that countries with public registries have deeper private credit markets, and [Author B (Year)] find that a single national registry reform expanded lending to opaque firms. [Author E (Year)] document a similar increase in loan volumes. These studies measure quantities, and their variation comes from one reform date or from comparisons across countries. We instead observe the price of individual loans and exploit staggered city-level rollout, which lets us separate the registry from contemporaneous local shocks. Our estimates show that information sharing lowers the cost of credit, not only its quantity.

结构为 S1 点名脉络；S2–S3 逐篇说发现；S4 共同局限；S5 本文差别；S6 本文结果。共点名 3 篇，没有括号堆叠，也没有 "Taken together"。

---

## 附：数字出处速查

| 数字 | 出处 |
|---|---|
| 1,848 词、14 段、73 句、5 句/段、25.5 词/句、126 词/段 [95–163]、44% 有路线图、91% 有脚注（中位 6 个） | `REPORT.md` §2a；`para_stats.csv`（n=117） |
| 各功能的出现率、位置、句数、词数和信息要素 | `REPORT.md` §3a/§3c；`label_tables.md` 4b（n=40） |
| 四种版式 22/9/7/9（规则 v3，n=47） | `LAYOUT_EVIDENCE.md` §Summary |
| "本文"句 27/40 在第 1–2 段；第一个结果在 0.38；31/36 篇最后三段里有贡献段 | `REPORT.md` §3b |
| 贡献段：每段 4 [2–6] 篇；89% 说清差异；47% 宣布条数（金融 29%，会计 73%） | `REPORT.md` §3d；`label_tables.md` 4c |
| 量级：29/40；% 60%、绝对单位 35%、基准 22%、标准差 12% | `REPORT.md` §3e |
| 句长标准差 10.7、>40 词 8.6%、<12 词 8.2%、段内最短 14 / 最长 37 词、首句 20 词、"taken together" 11/117、括号引用 ≥5 篇占 2.3% | 本次新增计算，117 篇可信引言的重建文本（脚本在会话临时目录，未进仓库） |
| we 每千词 18 次；限定语频率；引用格式；AI 词频 | `EN_writing_spec_v1.md` §3 |
| "Taken together" 在 10/12 篇生成稿中出现；编造句 11→34→4 | `spec_ablation_report_20261020.md` |

**局限**：
- 人工标注只有一个编码员，百分比按 ±10 个百分点理解。
- TAR、CAR、MS 的样本小。
- 样本以实证因果论文为主，理论论文只有 3–5 篇。
- 脚注内容、版式自动重分组时的段数，都是 [编辑] 或近似口径。

---

## 六、AI 痕迹自查清单（第 8 轮新增，2026-10-21）

来源：第 7 轮盲判中判官区分原文和生成稿时给出的理由，共 72 条二选一线索、60 条分段测验理由、72 条两稿对比理由。计数和逐条规则见 `writing_spec/round8/AI_TRACES.md`。英文版是 `guide_card_en_v4.txt` 第 6 节。

**原则**：清单只管"怎么写"。标 * 的条目需要具体内容，只有工作表（I1–I4 或其他格子）给了才写；没给就跳过这一步，绝不编。

| # | 检查项 | 判官提到的次数 | 怎么做 |
|---|---|---|---|
| 1 | 作者的声音 | 二选一 40/72；测验 18/60 | 全文有一两句作者自己的判断：这个空白为什么要紧，什么出乎意料，结果说明了什么、没说明什么。语气克制，用第一人称。有 I4 就用 I4；没有就只评价工作表已写明的内容。评价不能延伸出新的原因、机制、范围或时间（第 8 轮的新增编造句大多出在这里） |
| 2 | 逐步搭概念 | 22/72；14/60 | 读者可能不熟的概念，先用 2–4 个短步骤讲清：它是什么、起什么作用、为什么和本文有关。可以用一句短句点题 |
| 3* | 具体例子或类比（I1） | 11/72；23/60 | 紧跟在它要说明的抽象论断后面，一两句 |
| 4* | 历史或制度背景（I2） | 6/72；12/60 | 按"过去—变化—现在"讲一小段，用工作表里的日期，最后落到研究问题 |
| 5* | 理想实验（I3） | 4/72 | 先说理想实验是什么，再说为什么做不到，最后说本文情境怎样近似它 |
| 6 | 文献织进论证 | 4/72；20/60 | 文献在它支持或反驳的那一步出现，作者作主语，带上它的发现；结论冲突只在工作表写明时才写。不要罗列人名 |
| 7 | 句子节奏有变化 | 测验 39/60 提到"自然、参差" | 每段长短句混用，有一句长句；段首换着写；不要连续同一句型，不要每段都"First/Second/Third" |
| 8 | 每件事只说一次 | 两稿对比 34/72 | 不复述结果，不写回顾段，不写只预告下一句的句子 |
| 9 | 连接而不是罗列 | 27/72 | 检验、机制、文献之间用逻辑词连起来（因为、所以、相反），不排成清单 |
| 10 | 问题和答案在前 | 11/72 | 先提问题、预告答案，再展开长的理论或方法 |
| 11 | 只写完整句子 | 12/72 | 不出现残句、标签、格子编号或笔记句式 |

**配套的工作表新格子（第 8 轮试用，均为【选】，没有就不填）**：

| # | 问题 |
|---|---|
| I1 | 具体例子或类比：一个能把抽象论断说具体的例子（公司、数字、情境），或一个类比 |
| I2 | 历史或制度背景：事情怎么演变到现在，带日期 |
| I3 | 理想实验：最理想的识别是什么，为什么做不到，本文情境怎样近似 |
| I4 | 作者的评价：作者自己对问题、空白、情境或结果的判断（为什么要紧、哪里意外、边界在哪） |

### 6.1 直接说，不要"搭台"（第 10 轮新增，2026-10-22）

来源：第 9 轮单篇打分里判官对稿子的扣分理由。英文版是 `round10/guide_card_en_v6.txt` 第 7 节和 `round10/writer_notes_v6.txt`。这些规则只改"包装"，不增删工作表里的任何内容。

**通用**：
1. 段首直接给内容（事实、论断、结果、被引文献的发现），不写"这一段要讲什么""下面这一点为什么重要"。
2. 每一句都要承载工作表内容；只起铺垫、预告、贴标签、总结、复述作用的句子删掉。
3. 段落停在最后一条内容上，不加收尾的解释句或复述句。
4. 交稿前按下面对应写手的注意事项逐段过一遍。

**按写手的注意事项**（同一份规则卡，各写手只附自己那一条）：

| 写手 | 判官的评价 | 不要这样写 | 应该怎样 |
|---|---|---|---|
| luna（gpt-6-luna） | "流畅但泛泛""润色过的改写" | L1 套话式限定：每个论断后面条件反射地加平衡句（"净效应取决于哪一方占优""解读需要谨慎""必须与……权衡"） | 只有设计需要时才限定，每个论断最多一处；局限只在工作表写明时写一次 |
| | | L2 路标句：专门引出下一点、或宣布某事重要的句子（"X 与 Y 的区分说明了……""这些事件引出了我们的问题"） | 直接从要说的内容开始 |
| | | L3 重复陈述结果：结果后面加解释性复述（"这些发现表明……"），在机制、含义、贡献段再把主结果说一遍 | 每个结果只在它该出现的地方说一次；后文只用几个词指代，然后只写新增的东西 |
| ds（deepseek-v4-flash） | "清单式结构""口号句""电报体" | D1 清单式段落：把渠道、反向力量、公司名、检验一个一句或用分号串起来 | 把段落写成论证：每句从上一句推出来（因为、所以、这意味着、但是） |
| | | D2 口号句：短而上口的机制复述（"X 换来 Y，Y 换来 Z"），对仗、格言 | 机制只说一次，用完整的解释句 |
| | | D3 电报体：名词堆叠句、用破折号和分号拼接的短分句、连续的 12 词以下短句 | 写完整连贯的句子，多数句子 18–32 词 |
| | | D4 自我宣告结构：先给论证贴结构标签（"第一种力量是……""我们考虑两个相反的渠道""反向力量往另一边推"） | 直接让渠道、力量或机制本身带着内容做句子主语；每个数字只给一次 |
