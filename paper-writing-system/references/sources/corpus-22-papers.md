# 22 篇精标语料：宏中微观统计与逐字例句（证据文件）

> 2026-11-11 起本文件为证据文件：宏观层规则已移入 `structure.md` §2—§4，各章功能段图谱与句式已移入 `sections/` 各文件并标注【22 篇】。本文件保留统计口径、逐字例句与张力记录，供查证。

日期：2026-10-22。方法：导师层 A39 范文拆解法的规模化——对五套语料逐篇逐章做段落功能标注，再向上聚合。终稿规则只写有计数支撑的共性；个例入附录。

## 0. 用法与证据说明

**语料**：23 个 txt 文件、22 篇唯一论文（subnational-debt 同时在高昊宇池与唐勇军池出现，版本不同，按唯一论文计 1 篇）、约 40 万词。五池构成：高昊宇 6 篇、林晨 5 篇、黄毅 4 篇、唐勇军 3 篇（其中 1 篇为同文校准篇，有效独立样本 2 篇）、Wei Jiang 5 篇。提取产物（逐篇骨架表、逐章功能段表、句式候选表，共 15 份）存原工作区的 macro-meso-micro/ 证据底稿目录（骨架提取/、功能段提取/、句式提取/ 三个子目录；该底稿未随可移植包分发，本文件的数字与例句均为自包含的逐字转录），本文件的一切数字与例句均可回溯到那里。

**计数口径**（读数字前先读这段）：
- 章节词数由各提取员用脚本按原文标题行切分、空白分词实测；占比的分母为各池口径的"正文/主文"（摘要→结论，不含参考文献、表图、附录）。五池分母定义有小差（个别池含卷首残段），量级在 1–2 个百分点内，跨池比较请读区间与中位数，不要读小数点。
- 段落计数：PDF 抽取文本的自然段界部分丢失，各池采用功能段切分（锚点句定位＋脚本计数），引言逐段精标，其余章节粗一档。黄毅池功能段按主题/小节边界切，不与他池的段数直接横比。
- 例句：五池共收集 286 条，全部经归一化子串回读校验（归一只处理断行、空白、引号样式，不动词序与数字）。本文件句式库收录其中约 50 条，选取标准是跨池复现或功能位典型。
- 支撑度标注：规则后标（n/22 篇）的为实测支撑篇数；只有 1–2 篇支撑的观察不进正文，进附录 A。
- 已知污染与降权：林晨池 4/5 篇属 Levine–Xie 团队（只在该簇出现的特征标注"Levine 簇内"，不算跨团队共性）；唐池有效独立样本只有 2 篇；高池 perils 一篇文风疑由一作 Berger 主导，其独有特征已剔除出共性；subnational-debt 在双池只计 1 篇。详见附录 B。

**三层用法**：宏观层决定"这篇文章长什么样"（开工前选型）；中观层决定"这一章由哪几段、按什么顺序构成"（逐章起草时对照）；微观层决定"这一段怎么推进、这句话套哪个骨架"（逐段写作与改稿时查）。三层与已有体系（五份风格文件 v4、导师层、中文语言层）的关系单列于第 4 节。

---

## 1. 宏观层：整篇框架怎么搭

### 1.1 各章篇幅实测分布（22 篇，中位数与区间）

| 章节 | 占正文比（中位） | 区间 | 备注 |
|---|---|---|---|
| 摘要 | 正文外单块，88–184 词（中位 109） | — | 恒为单段/单块（22/22），内部分 3–6 个功能层 |
| 引言 | 21.2% | 9.9%–33.8% | 另有 tail 一篇 6.1%（RFS 短篇幅刊出体例，离群） |
| 制度背景（独立或合并章） | 约 10% | 4.6%–22.1% | 位置与合并方式见 1.3 |
| 数据（含量测度构造时） | 约 10% | 5.1%–38.1% | 高值全部来自测度构建型（见原型 D） |
| 经验设计（独立成章时） | 约 9% | 6.0%–11.8% | 独立成章是少数派（约 6/22），多嵌入数据章或结果章首 |
| 结果类章节合计（基准＋稳健＋机制＋异质性） | 约 45% | 31%–60% | 全篇重心；单章最高为 ownership 结果章 45.6% |
| 结论 | 3.1% | 1.3%–7.3% | 恒为全篇最短或次短章（22/22） |

正文总长：7,274–14,998 词（中位约 10,200）；正文章数 4–10（中位 6）。后置部分（参考文献＋表图＋附录）占全文件 34%–50%，写稿时不要把这部分误算进正文预算。

### 1.2 框架原型五型（按识别与贡献的组织方式分型）

**原型 A：单识别事件评估型**（7 篇：rise、aftermath、BANK、COMM、MWCI、cds、GEO，其中 aftermath/cds/GEO 为变体）。
骨架：引言 → 制度背景 → 数据（＋变量构造）→ [设计嵌入或独立] → 结果链（基准 → 稳健/安慰剂 → 异质性 → 机制）→ 结论。
判据：只有一个外生变异来源（政策冲击、断点、自建 IV），全部结果章都是这一个识别的护栏与含义展开。变体：aftermath 把三个 DID 事件嵌在结果章 4.3 做因果背书（识别后置于描述性基准之后）；GEO 把 OLS 明示为"有偏基准"、IV 章占正文 21.9% 为全篇重心；cds 无独立设计章，设定辩护分散在变量构造与稳健性小节。
选型条件：贡献来自"一个干净冲击的后果评估"，且冲击的制度由来讲得清。

**原型 B：假设驱动—逐条验收型**（3 篇：ownership、subnational、tail；coco 为近亲变体）。
骨架：引言 → 制度背景＋假设发展（编号假设在本章末尾正式陈述）→ 数据（可含"预结果"）→ 结果章按假设编号逐条验收 → 替代解释专节 → 结论。
判据：理论能推出 2–4 条可区分、可编号的预测，且每条预测有独立的经验对应物。subnational 的第 3 章先给现象层"预结果"（单变量＋多变量模式），第 4 章再做行为层正式检验，是本型的加强版。coco 无编号假设，但用整章（§3）把三场政策辩论逐项转成实证问题，§3.4 收敛为两个问题——"辩论转假设"变体。
选型条件：贡献是对一个机制命题的证实/证伪，且命题能拆成编号清单；导师层 A20 的"假设少而尖"在本型内最适用。

**原型 C：多路识别—同向收敛型**（2 篇：LOCAL、FIRM）。
骨架：引言（主结果先行）→ 数据/制度前提 → 基准相关（靶子）→ 识别路线一 → 路线二 → 路线三（各路线自带识别假设辩护）→ [方法替代章] → 结论。
判据：没有任何单一路线的识别假设强到可以独扛结论，于是用三条相互独立、共同指向同一机制的路线做三角验证。LOCAL 四章识别路线合计占正文 45.0%，是基准章的近 3 倍；每条路线内部再嵌一层稳健性（第 7.2 节整节复跑），在线附录与正文等量（后置占全篇 49.6%）。FIRM 是本型的裁决变体：两对立观点（Darwinian vs managerial）由四小节证据逐级裁决，稳健性独立成章且三小节全是替代解释拆除。
选型条件：主识别有公认软肋（如现金流敏感性的 KZ 批评），或问题本身存在两个对立理论需要证据裁决。

**原型 D：测度构建型**（4 篇：machine、manplus、fintech、tech）。
骨架：引言（测度与全部主结果先行预告）→ 数据来源 → **测度构造（数据章内）→ 测度验证（独立位置）→ 测度使用（基准回归）** → 异质性/扩展 → 结论。
判据：核心贡献是一个新测度/新指数/新对象。实测共性（4/4）：构造与验证永不同节完成——machine 专设 III.A 效度节、fintech 用 3.1.3 做区分效度、tech 用 3.3 测度事实＋3.4 双指数关系诊断验尺；测度相关章节是各篇最大或次大章（fintech §3 占正文 38.1%、tech §3 占 32.3%、machine §II 占 29.5%、manplus 构建＋验证合计 41.8%）。manplus 是"对象构建"变体：构建的是参赛选手（AI 分析师），验证形态是"达标验证"（胜过 53.7% 的人类预测）而非效度检验。
选型条件：贡献句能写成"我们构建了一个此前不存在的 X，并用它回答 Y"；若测度只是工具变量或控制变量，不要选本型。

**原型 E：多部分复合型**（1 篇：FIN，低频但结构完整，列为可选原型）。
骨架：引言 → 独立文献章 → 独立制度章 → 数据 → 描述分析（第一部分）→ 因果评估（第二部分，FRDD）→ 优势维度与机制（第三部分）→ 稳健性 → 结论。
判据：论文同时含一个描述性问题与一个因果问题，两部分共享同一数据与制度场景。注意 FIN 是 Hau 团队的展开式骨架（10 章），与 Levine 簇的压缩式骨架（4–7 章、无独立文献/制度章）恰成对照——本型的"独立文献章＋独立制度章"在全语料中只出现 2 次（FIN、FIRM 的 Related Literature），属少数派选择，采用时要有自觉。
选型条件：描述部分本身有独立贡献（如"国有银行黑洞"假说），且期刊/篇幅容得下展开式骨架。

### 1.3 跨原型的结构共性（高频，近乎无例外）

- **引言是全文的压缩预演**（22/22）：引言按正文的结果顺序逐项预告每个结果小节，发现、量级、异质性在引言内给齐；cds 引言 P3–P7 与 4.1–4.5 一一对应、IMM 五组特征、DEP 四组含义检验均可验证。推论：引言段序＝正文章节序，写引言时先定正文骨架。
- **结论只回收不展开**（22/22）：结论占正文中位 3.1%，功能是发现压缩复述＋至多一个含义/外推动作；fintech 结论仅 139 词，因为总结功能已在引言结果段的 "In sum" 收束句中提前完成——结论短不是缺陷，是引言预演的必然结果。
- **制度背景的位置三态**：独立成章（约 11/22，如 subnational §2、cds §2、tech §2）；与假设合并成章（ownership II、subnational 亦属此型）；与数据/设计合并成章（MWCI §2、GEO §2、perils §2）。三态之外，把制度材料全部压进引言的：0 篇。
- **稳健性的三种安置**：独立成章仅 3/22（aftermath、FIRM、FIN）；节内嵌（结果小节正中或段尾，最常见，如 cds 4.3 居五小节正中、BANK 嵌在结果段尾）；下沉脚注＋附录表（Jiang 池 4/4 篇：正文只留一句结论性回指）。三种安置对应三种可信度策略：正面迎战、织入结果链、低调处理——选哪种取决于主识别的公认软肋有多少。
- **可信度防御在机制之前**（在设有独立机制章/节的篇目中近乎一致）：placebo 在 subnational 第 3 章已出现、IV 整节在 tail 3.3、匹配稳健性在 cds 4.3——固定次序是"先立可信度、再讲机制"，不要把稳健性留到全篇最后才补。
- **假设的显性程度谱系**：编号假设正式陈述（ownership、subnational、tail，均置于第 2 章或假设章末尾）→ 辩论转问题（coco）→ 引言内枚举展开（aftermath 的 First/Second/Third/Fourth 调节条件、IMM 的五组预测）→ 条件式预期句散见结果节首（cds、BANK）→ 双力框架＋"a priori ambiguous"（tech、MWCI 引言）→ 单句 hypothesize（fintech §3.2.2）。理论配置越重越靠前、越编号化；没有理论模型的篇目不硬设假设章。

---

## 2. 中观层：逐章功能段落图谱

读法：每章给"标准功能段序列"（按出现频率与位置聚合）、每段的职务、实测变体与频次。段数指功能段（口径见 §0）。

### 2.1 摘要

标准序列（单段内分层，22/22 单段/单块）：
1. **问题或主张**（首句）：或以研究问题起（fintech），或直接以核心主张起（subnational "We provide direct evidence that governments selectively default…"）。
2. **数据/设计一句**：数据来源与粒度、识别一词带过（"using a discontinuity in the credit decision algorithm"，FIN）。
3. **核心发现**：1–2 句，只给头条方向与量级。
4. **机制或第二发现**：机制归因句或异质性指向。
5. **（可选）含义/总括**：subnational 以概念命名收尾（politics-finance nexus），rise 以 trade-off 总括收尾。

层数实测 3–6 层，词数 88–184（中位 109）。变体：coco 摘要含"四项编号发现列举"；cds 摘要以对比结构报告主发现（资产↑而 RWA↓）。与导师层 A13 对照见第 4 节。

### 2.2 引言（本章做到最细）

实测段数 8–18（逐段精标的 18 篇；中位约 11–13），占正文中位 21.2%。标准功能序列（ modal 顺序，标注频次）：

| 位次 | 功能段 | 职务 | 频次/说明 |
|---|---|---|---|
| ¶1 | 大问题与重要性 | 用量级事实或领域断言立"为什么重要"，中国/具体场景是回答问题的场景、不是问题本身 | 22/22 |
| ¶2 | 谜题/缺口/对立 | 把重要性收窄为一个未决问题：puzzle 句、证据缺口、或双向理论对冲 | 约 20/22（BANK 以要件分解聚焦缺口、FIRM 以问句收尾代之） |
| ¶3 | 本文做法一句话＋研究问题重述 | "In this paper, we…" 宣告对象、数据与问题 | 22/22 |
| ¶4 | 数据与识别交代 | 数据卖点（粒度＋覆盖率）与识别策略各一句到一段；测度构建型在此预告测度 | 约 21/22 |
| ¶5–¶9 | 发现预告（主体块，占引言篇幅约一半） | 按正文顺序逐项预告：基准发现（带量级）→ 异质性/含义检验 → 机制 → 稳健性一句带过；推进词单调有序（First… Second… Next… Finally…） | 22/22；带量级约 20/22 |
| ¶穿插 | 理论/假设预告 | 位置随原型变（见变体） | 见下 |
| ¶倒2 | 贡献定位 | 点名近亲文献并说清差异；首创宣称如用须过事实门（见 3.3 第 16 类） | 约 20/22 有独立定位段或定位块 |
| ¶末 | 路线图 | 逐节一句，节名与正文严格对应 | 约 16/22；缺席者集中于 Levine 簇疫情组（IMM、DEP）与 Cao–Yang 簇（machine、manplus） |

顺序变体（三处系统性分叉）：
- **文献定位的位置**：(a) 前置织入——放在 ¶2–¶3 的文献线里（COMM 两条文献线、IMM 织入五组理论预测段、DEP 以四解释并列代替文献段）；(b) 后置独立段——引言末尾、路线图之前（DEP ¶18、machine ¶8、manplus ¶10）；(c) 引言外独立章（FIRM、FIN，2/22）。三种都成立，但一篇之内只能选一种主位。
- **假设的位置**：引言内枚举（aftermath、IMM、MWCI 的理论歧义段）；留到第 2 章末编号陈述（ownership、subnational、tail）；辩论章转出（coco）。引言内只预告假设的方向与条数，不展开推导。
- **识别辩护的深度**：多数篇目引言只给识别一句话＋一句正交性/平行趋势交代；GEO 是例外——识别辩护专段占引言 46%（IV 构造三段＋五点辩护专段），因为该篇的贡献与软肋都在工具本身。判据：识别越是自建、越招质疑，引言辩护越重。

与导师层 A15 的对照（12–13 段功能互斥：why 两段、制度一段、识别核心一段、数据一段、识别一段、发现数段、外推一段、贡献）：实测序列与 A15 的功能清单大体同构，三个出入点——(1) A15 把制度背景放在引言内一段，语料中引言内至多有制度细节段（rise ¶3 讲 2009 放松细则），制度主体在引言外独立或合并成章（见 1.3 与第 4 节张力 T1）；(2) A15 的独立"外推段"（置于贡献之前）在引言中罕见（约 4/22：credit ¶16、manplus ¶9 条件式外推独立成段等），外推主要落在结论（见张力 T2）；(3) A15 未单列"数据卖点"与"识别辩护"的轻重分级，语料显示这两段的篇幅由原型的软肋位置决定（见上）。
与高昊宇风格文件 2.3 模板对照：模板的"大问题→做法→数据/识别→分条发现→机制→贡献→路线图"与实测 modal 顺序一致，且模板关于推进词单调性、引言数字配额的细则在跨池语料中同样成立（见第 4 节）。

### 2.3 制度背景

标准序列（独立成章时，3–7 段）：
1. 制度总览/起源：制度从何而来、一句法律或政策锚点（cds §2 以 1994 首单 CDS→1996/97 美联储认可的制度史开场）。
2. 与识别直接相关的规则细则：只讲后文要用的那几条（风险权重四档之于 cds、准入细则之于 rise）。
3. 处理组/对照组的可分性交代：制度如何制造出可比的两组（subnational 2.2：银行政治层级差）。
4. （假设驱动型）收束到假设：在本章末尾正式陈述编号假设，或给出条件式预期。
职务：制度章不是背景知识汇总，是"识别的零件箱"——每段讲的制度事实都应在结果章被引用一次；讲不到的删。合并变体：与假设合并（章名即 "Institutional background and hypothesis development"）、与数据合并（"Data and interstate bank deregulation"）、与设计合并（MWCI §2 四合一）。

### 2.4 理论与假设

三种形态（按 1.3 的谱系）：编号假设型（假设以独立短段正式陈述，前置推导段、后置检验路径段——ownership II.B 的 H1/H2 各 29 词独立成段，是最干净的样本）；辩论转问题型（coco §3：三场辩论各一节，末节收敛为实证问题＋模型预测）；框架型（tech 的双力框架：互补 vs 替代、"a priori ambiguous"一句定调，不编号）。共性规则：预测必须在基准结果之前全部出场（22/22 无一篇在结果章临时新增预测）；每条预测在结果章有且只有一个主要验收位置。

### 2.5 数据

标准序列（按数据源逐个走，IMM 的八小节是最规整的样本）：
1. 数据总述：来源清单＋样本期＋分析层级一句话。
2. 逐数据源：来源 → 变量构造 → 描述统计，三拍循环（IMM §2.1–2.8 与结果章 3.2–3.6 一一同构——数据章的小节序就是结果章的小节序，这是可直接借用的组织法）。
3. 关键变量构造专段：处理变量/核心测度的口径、聚合方式、口径选择理由（COMM II.C 旅行时间测算规则、GEO 2.2 Herfindahl 构造）。
4. 样本构造与筛选：合并步骤、筛选规则、最终样本量。
5. 描述统计导读：不逐格念表，只点与后文检验相关的分布事实。
测度构建型变体：构造子节编号化（machine II.B 的 B1–B6）、构造之后果断收尾，把验证留给下一章（见 1.2 原型 D）。

### 2.6 经验设计

独立成章时（约 6/22）的标准序列：识别挑战陈述（"The main identification challenge we face is…"）→ 设定/方程 → 识别假设逐条编号（credit §4 的两条假设各配验证段）→ 固定效应与聚类的识别含义 → 估计口径。嵌入式（多数）：设计段出现在数据章末（MWCI 2.章内）或结果章首节（DEP §3 与 §4 分离、IMM 3.1 与结果同章）。共性：固定效应不只报名字，要写清每组固定效应"吸收什么、留下什么变异"（DEP §3、COMM ¶7 均如此）；IV 型必有独立的工具构造与效度辩护块（GEO §4.1）。

### 2.7 基准结果

标准段落单位（跨池最稳定的章内结构）：**本节问题段 → 设定/因变量段 → "Table X…" 结果段 → 列/Panel 细读段 → 小结段**。小节推进按"先总量、后分解"：主效应 → 分组/交互 → 子样本。结果段的段内写法见 3.2 模式一。特殊形态：DEP 的基准章极短（680 词，只立"供给侧主导"一个裁决），重心后移到含义检验章；GEO 的 OLS 章被明示为有偏基准、只占 IV 章的五分之一——基准章的篇幅服从论证需要，不必与 IV/主结果章等重。

### 2.8 稳健性

按 1.3 的三种安置各有段序：独立成章时按威胁类型分节（FIRM：替代测度→企业退出→产出误测，三节全是替代解释拆除，每节以"X cannot account for…"收束）；节内嵌时按"顾虑自陈→复跑→结论存活"三拍（cds 4.3）；下沉时正文只留一句回指＋附录表号（fintech Table A.1）。引言预告层合并成一句（导师层 A18 在语料中的对应物：引言发现块中稳健性从不逐项展开，22/22）。

### 2.9 机制与异质性

标准序列：机制问题段（"What can explain…?"）→ 机制证据逐条（每条一个子节：逻辑一句 → 设定 → 结果 → 回扣机制）→ 异质性按理论预测的维度逐项（维度在引言或理论章已预告，不临时发明维度）。异质性章篇幅常不低于主效应章（MWCI 21.3% 反超主效应章 15.8%；BANK 最重章是利差＋四路异质性的 V 章 23.0%）——因为异质性承担的是"预测逐项兑现"的验收功能。竞争性解释的裁决也在本章完成（perils 4.1 先排除 biased expectations 再立 agency；DEP 第 5 章四组含义检验在余下解释间继续裁决）。收束句式见 3.3 第 14 类。

### 2.10 结论

标准序列（1–3 段，139–698 词）：发现压缩复述（与摘要同序）→ 一致性总判断 → 至多一个外移动作，三选一：政策含义（FIN、cds）、文献一般命题回扣（FIN 结论 ¶2）、未来研究/未决问题（coco 的标准化选项列举、rise 的未来研究句）。Levine 簇四篇结论无外推、只回收——外推做不做是团队风格差异，不是质量差异；但"复述＋总判断"两件套 22/22 都有。

---

## 3. 微观层：段内逻辑与通用句式库

### 3.1 段内逻辑模式（五种，均为多篇复现的成段形态）

**模式一：结果段五拍——断言→系数→量级翻译→解读→收束。**
形态：首句给方向性发现（不带数字或只带头条数字）→ 次句报系数/点估计 → "This means that…" 给绝对量级、"Given that… this is equivalent to…" 给相对量级（三级翻译，见句式库第 9/10 类）→ "consistent with the view that…" 把数字读回机制 → 末句小结或指向下一小节。实测：ownership 第 IV.A 节至少复现 3 次、引言 ¶5 压缩复现 1 次；COMM 引言 ¶8 是三拍压缩版（发现→双量级→一致性解读，110 词）；IMM §3 各小节以"结果报告→量级翻译→解读"循环。变体：量级翻译的标尺四种——1 个标准差（GEO −13.6%）、双企业分位对比（IMM 25→75 分位、3.2 个百分点）、占标准差份额（FIN 24%）、理论预测值对表（FIRM "only 1/5 of the predicted change"）。纪律：相对量必须同句带基数锚（与中文sections/results.md 一致）；引言里翻最大的头条系数，不得翻小漏大（高昊宇文件 0.2 的实测依据在跨池语料同样成立）。

**模式二：辩护段——威胁自陈→逐项拆解→检验背书→确认收束。**
形态：先把识别威胁自己说出来（遗漏变量、预期性选择、反向因果）→ 编号逐项回应（设定、固定效应、安慰剂、检验）→ 用一个统计检验的结果句封口（F 统计量、Sargan、pretrend 不显著）→ "remains significant / cannot account for" 确认结论存活。实测：tail 引言 P3 整段（双威胁同序拆解）；GEO 引言 ¶7 五点编号辩护专段（355 词）；FIRM 稳健性三小节同构。要点是威胁与回应严格同序——读者按你列威胁的顺序逐个销账。

**模式三：编号预告段——总起报数→逐项编号兑现。**
形态："Our empirical findings are threefold." 先报总数 → First/Second/Third 逐项 → 每项内部再走"结果—量级/分布—含义"小三拍。该编号结构与正文小节一一映射，引言预告即正文目录（FIRM；高池 credit ¶5–¶7、rise ¶6–¶13 同型）。风险：编号必须与正文严格同序且数目对得上，错位是盲测中出现过的生成事故（推进词 First→Next→Second 乱序）。

**模式四：双力对冲段——宣布未决→正臂→转折→负臂→并置收束。**
形态：首句宣布符号未定（"Theoretically, the investment effects of MW are ambiguous."）→ 正向机制（配文献/轶事）→ "Other theories, in contrast…" 翻面 → 负向机制 → "Taken together" 并置，收束为一句未决问题，把站队留给后文证据。实测：MWCI 引言理论段、tech ¶7 双力框架、GEO ¶1 对立理论同段、DEP ¶2–¶5 四解释并列（本模式的扩展版）。这是"理论歧义型"引言与假设章的标准段，也是 示例政策 类 revision 论文引言张力段的原型。

**模式五：测度微缩段——造尺→验尺→用尺在一段内同构复现。**
形态：双测度并置定义 → 逐个交代构造 → 代理正当性双理由 → 外部验证一句 → 主结果（标准化量级）→ 安慰剂对照收尾（machine 引言 ¶4，283 词）。与全篇原型 D 的"构造→验证→使用"宏观顺序同构（分形）：引言里的测度段怎么写，正文的测度章就怎么扩。适用前提：测度本身是贡献；普通工具变量不要套这个段。

段长参考：功能段多在 80–350 词；超过约 250 词的单段（GEO 辩护段 355、FIN 结果段 448、credit 发现段 433）都靠段内编号或小三拍维持可读性——长段必须有内部结构，否则拆段（与 v4 共同层 V4-4 的单段约 250 词参考上限互证）。

### 3.2 句式库使用说明

每类给：句式骨架（槽位用［］标注）、2–3 条语料原文例句（逐字，出处＝篇目 ID）、适用条件与滥用风险。例句的归一化口径见 §0；标"Levine 簇内"的句式只在该团队检出，跨团队使用前要有自觉。风险提示中与盲测三轮、高池文件第零层呼应处已注明。

### 3.3 通用句式库（17 类）

**1. 开篇断言**
骨架：［领域级命题：对象＋状态/变化断言］。／设问式：Does［X］affect［Y］?
例句：
- "Creative destruction is a key feature of a modern, market-oriented economy."（aftermath，引言 ¶1 首句）
- "Advances in financial technology (fintech) are reshaping the landscape of financial services in the United States and globally."（fintech，引言 ¶1 首句）
- "Does the geographic expansion of a bank's assets affect its funding costs?"（GEO，引言 ¶1 首句，设问式）
适用：引言首句；断言须是学界大体接受或本文将证明的命题，不能是争议结论本身。风险：断言过强而后文证据只支撑弱版本，是审稿人最易抓的落差；设问式只在全文真能回答该问句时用。

**2. 谜题提出**
骨架：It has been a puzzle why［反常事实］.／［事实清楚］, it is unclear what drove［X］.／As theories provide mixed guidance,［问题］is therefore an unanswered empirical question.
例句：
- "It has been a puzzle why governments have not defaulted on their debt more often than observed, suggesting that latent factors are restraining governments from capricious defaults."（subnational，引言 ¶1）
- "While it is clear that deposits and savings increased, it is unclear what drove these developments."（DEP，引言 ¶1 末句）
- "As theories provide mixed guidance, how MW affects corporate investment behavior is therefore an unanswered empirical question."（MWCI，引言理论段收束）
适用：引言 ¶1–¶2 收束处。风险：puzzle 必须是真谜——若文献已有公认答案，硬称 puzzle 会被定位段的近亲文献当场拆穿（与 C6 归因纪律联动）。

**3. 文献定位**
骨架：Our research is related to but different from［近亲］.／Our paper differs from the existent literature in that［差异］.／This paper is related to the［大文献］.
例句：
- "Our research is related to but different from Li, Strahan, and Zhang (2020)."（DEP，引言末段首句）
- "Our paper differs from the existent literature in that we are able to explore the internal mechanism of machines we constructed ourselves, and to identify its relative advantages to humans more directly."（manplus，引言文献段）
- "This paper is related to the vast literature on the impact of government debt on investment and growth."（LOCAL，引言文献段首句）
适用：差异句必须紧跟一句说清差异的实质（数据、识别或对象），只说 different 不说 different in what 等于没定位。风险（盲测 C6）：归因与差异陈述都受标题级口径约束——不得把近亲文献没说过的话安到它头上，也不得把本文的差异说成对方的缺陷。

**4. 制度交代**
骨架：During our sample period of［时段］, the［法律/规则］［约束内容］.／The［政策］in［场景］provides us with a unique and rich institutional setting to study［问题］.
例句：
- "During our sample period of 2007–2013, the 1994 Budget Law prohibited local governments in China from borrowing directly in any form (e.g., bank loans or bond issuances)."（subnational，§2.1 首句）
- "The MW policy in China provides us with a unique and rich institutional setting to study the impact of labor on corporate investment policy."（MWCI，§2.1 首句）
- "Nevertheless, the introduction of the Basel III framework, which allows banks to meet part of their regulatory capital requirements with CoCo instruments, created strong incentives for banks to seriously explore the possibilities for issuing CoCos."（coco，引言 ¶1，制度落地句）
适用：一句只交代一条后文要用的规则；制度事实与识别用途同句绑定（第二条例句的句式）。风险：制度章堆与识别无关的沿革（导师层 A22 的"删细碎描述"在英文语料同样成立——制度章每段都要能被结果章引用）。

**5. 数据交代**
骨架：Our primary analysis is based on［粒度］data from［来源］, covering［对象］from［时段］.／［数据］covers about［覆盖率］of［总体］.
例句：
- "Our primary analysis is based on loan-level data from one of China's five major state-owned commercial banks, covering loan issuance from 2011 to 2017."（BANK，§III 首句）
- "After merging I/B/E/S with CRSP and Compustat, the final sample consists of 685,888 analyst target price forecasts on 6,118 firms, issued by 10,287 analysts from 755 brokerage firms."（manplus，§2.1）
- "Our loan-level data set from China's banking regulatory authority covers about 98% of the bank loans to local governments from 2007 to 2013."（subnational，引言 ¶3）
适用：来源＋粒度＋覆盖/样本量＋时段四要素一句齐。风险（盲测第一轮的头号失真）：卖点粒度不得抬级——债券级＋面板数据不能说成逐借款人链接；覆盖率数字必须与数据章一致。

**6. 识别辩护**
骨架：Identifying the effects of［X］is challenging, as［威胁］.／That is, the F-test… is above［值］, indicating that we do not have a weak instrument problem.／For a tighter identification, we further confirm a parallel pre-trend in［变量］between［两组］.
例句：
- "Identifying the effects of MW on corporate investment is challenging, as the determinants of MW may not be orthogonal to economic fundamentals or firm characteristics."（MWCI，§2 经验策略首句：先认难，再给设计）
- "That is, the F-test on the instrument in the first-stage regression is above 25, indicating that we do not have a weak instrument problem."（GEO，引言辩护专段）
- "For a tighter identification, we further confirm a parallel pre-trend in the LM – Harvard Sentiment between firms with high and low (top and bottom terciles of) machine downloads up to 2010."（machine，引言 ¶5）
适用：辩护句要落在可检验的事实上（检验统计量、对照组构造），不落在形容词上。风险：可信度数字（一阶段 F 等）属必留清单 (c) 类，引言配额不得误扫（v3 C3 划界）；辩护强度与识别实际强度对齐，弱工具下主动降级因果语气（高池文件的对冲纪律）。

**7. 假设陈述**
骨架：Hypothesis［n］:［主体］［可检验方向断言］.／We hypothesize that, after［处理］, there will be an increase in［结果］.／Specifically, if［机制］, then［可观测含义］.
例句：
- "Hypothesis 1: In loan screening, borrowers' private information can be passed through the network to banks, helping banks assess the probability of subsequent delinquency more accurately in loan issuance."（ownership，§II.B，独立短段全文 29 词）
- "We hypothesize that, after the reform, there will be an increase in the proportion of secured loans within banks' portfolios."（BANK，§IV 首段：进回归前先押方向）
- "Specifically, if geographic diversification reduces funding costs by lowering risk, then its impact on funding costs should be greater when BHCs expand into states that offer greater risk diversification opportunities."（GEO，引言机制设计段，if–then 式）
适用：编号假设一句一条、独立成段；条件式预期用于无编号形态。风险：假设条数服从导师层 A20（1–2 条关键假设为常态，tail 的 4 条是 RFS 体例下的例外，见张力 T3）；假设不得在结果章被悄悄改写方向。

**8. 结果报告**
骨架：We find that［处理］leads to［方向＋对象］.／The empirical results show a［方向］effect of［X］on［Y］and support the［假设名］hypothesis.
例句：
- "We find that the introduction of a new airline route that reduces travel time between a bank's headquarters and a branch leads to a sharp increase in the total dollar amount and number of small loans ($100,000 or less) that the bank makes in the branch's county."（COMM，引言发现段首句）
- "The empirical results show a significant positive effect of MWs on corporate investment and support the capital-labor substitution hypothesis."（MWCI，引言预告段首句：结果与假设裁决同句）
- "Similarly, the likelihood of bankruptcy more than doubles (from 0.14% to 0.47%) once a firm is referenced by CDS trading."（tail，引言主效应报告句）
适用：发现段首句给方向与对象，数字随后（模式一）。风险：引言结果句不写 statistically significant 叙事、不报标准误（高池实测：原文引言该词 0 次）；"support the hypothesis" 只在该假设确被本结果验收时用。

**9. 系数解读**
骨架：This means that a［单位变化］increases［Y］by［绝对量级］.／The point estimate indicates that a［1-SD 变化］is associated with a［量级］（whose sample average is［基数］）.
例句：
- "This means that a one-level increase in rating category increases the delinquency probability by 2.8 percentage points."（ownership，§IV.A 表 2 解读段）
- "The point estimate indicates that a 1-standard-deviation increase in the debt-to-GDP ratio (14 percentage points) is associated with a 1.2 percentagepoint decrease in the investment ratio (whose sample average is 8%)."（LOCAL，§4；"percentagepoint" 为 txt 原样）
- "The coefficient estimate on CDB is −0.048 and statistically significant at the 1% level, suggesting that, given the same due time of the loans, when a city defaulted on its loans, the chance that the defaulted loan was from the CDB is 4.8 percentage points lower than from commercial banks."（subnational-debt，§4.1；系数→显著性→概率含义同句完成——同文校准篇例句，归 Gao–Ru 簇）
适用：结果章的系数后第一句解读。风险：百分点与百分比不得混用（sections/results.md）；"suggesting" 领起解读句是机制归因的默认对冲级，不要升格为 proves（对冲四级见language/zh.md §A）。

**10. 量级翻译**
骨架：For example, the estimates imply that a one standard deviation increase in［X］will［Y 变化量］.／Holding other factors constant, … would［结果］by［分位对比量级］more than［对照］.／［系数变化］, amounting to［占样本均值/SD 的份额］.
例句：
- "For example, the estimates imply that a one standard deviation increase in the cross-state dispersion of a BHC's assets will reduce the total interest expense ratio by 13.6% in our sample."（GEO，引言结果段，1-SD 口径）
- "Holding other factors constant, our estimates imply that the stock price of the more internationally exposed firm would fall by 3.2 percentage points more than the less exposed firm over two months."（IMM，引言供应链发现段，双企业分位对比口径）
- "This amounts to about 24% of the standard deviation of these ratings which are expressed on a scale from 0 to 1."（FIN，引言结果二段，占 SD 份额口径）
适用：每个头条系数至少配一种翻译；标尺选读者最有感的一种（SD、分位对比、样本均值份额、货币/GDP 量纲）。风险：翻译口径可以在合法口径中选冲击力大的（导师层 A27），但基数锚必须同句在场（sections/results.md 是底线）；不得只翻对己有利的子样本量级。

**11. 对冲限定**
骨架：Without ruling out that［并存解释］, our analyses suggest that［本文主张］.／We do not find evidence that［零结果如实报告］.／… too short to offer definitive inferences.
例句：
- "Without ruling out that people flee from risky assets into bank deposits, banks increase their demand for deposits, or that national policies contribute to the flow of funds into bank deposits, our branch-county-week analyses suggest that local exposure to COVID-19 cases triggered concerns about the economy that induced a sharp increase in precautionary savings."（DEP，引言总裁决段）
- "We do not find evidence that corporate stock price reactions to COVID-19 vary systematically with board structure or executive compensations systems."（IMM，引言治理发现段，零结果照实报告）
- "Toward the end of our sample (since 2018), we observe signs of increasing decoupling, but the time period is too short to offer definitive inferences."（tech，引言 ¶5，样本长度限定）
适用：总裁决段、零结果报告、样本边界声明。风险：对冲是分级的（suggest/indicate/show 的强度差，见language/zh.md §A 四级表）——机制与识别推断默认 suggest 级；零结果属于必留清单，不得因"不好看"而省略（v3 C2 的实测教训）；样本边界主动认领（BANK "We admit that the sample excludes…"）比被审稿人指出便宜得多。

**12. 替代解释排除**
骨架：To rule out that［替代解释］drives our findings, we show that［复跑/剔除结果］.／We conclude that［替代解释］cannot account for［模式］.／［OLS 反号］, which might reflect reverse causality:［机制］.
例句：
- "To rule out that this government expenditure shock drives our findings, we show that our results are robust to excluding firms with input-output linkages with sectors that are plausibly affected by government induced demand shocks during the stimulus period."（credit，§5.2）
- "We conclude that price mismeasurement cannot account for the cross-sectional pattern of productivity changes in Table 5."（FIRM，稳健性 Output Mismeasurement 小节收束句）
- "When using ordinary least squares (OLS), we find a positive association between diversification and funding costs, which might reflect reverse causality: BHCs with higher funding costs expand to other states in search of lower funding costs, so that OLS yields an upwardly biased coefficient estimate on geographic diversification."（GEO，引言结果段，以反向因果解释基线反号）
适用：排除句要给出排除的动作（剔除、换样本、安慰剂零效应），只说 "unlikely" 不算排除。风险：按导师层 A29 的口径，"排除替代解释"的框架语言属于稳健性/结果章，不进引言发现块的第一位置——引言先立主假设与主结果（示例稿已按此结案）。

**13. 转折过渡**
骨架：The last few years, however, have seen［趋势反转］.／Other theories, in contrast, suggest［反向预测］.／［主体］are not expected to be passive players in［冲击］.
例句：
- "The last few years, however, have seen a rise in mutual distrust and actions to unwind from the current level of technological interdependence."（tech，引言 ¶2 首句）
- "Other theories, in contrast, suggest MW hikes may lead to a decline in corporate investments."（MWCI，引言理论段）
- "Firms are not expected to be passive players in a wave of disruption."（fintech，引言 ¶6 首句，由冲击转入企业应对）
适用：转折句承担段际方向切换，必须一句完成、指向明确（转到哪一臂）。风险：转折词密度过高是指纹滥用的高发区（盲测实测生成稿指纹词达语料密度 10–14 倍）；however/in contrast 在一段内至多一个转折点。

**14. 段落收束**
骨架：Taken together, our findings support［假设/判断］.／Together, these findings suggest that［多结果合并为一个机制判断］.／In sum,［双面结论并置］.
例句：
- "Taken together, our findings support Hypothesis 1 that network information can help banks to predict delinquent loan events more accurately at the time of loan screening."（ownership，§IV.A）
- "Together, these findings suggest that the simultaneous shifts in credit demand and supply, triggered by the reform, create offsetting effects on the interest rate spreads of secured loans while enabling borrowers to extract greater leverage from their collateral."（BANK，结论 ¶2）
- "In sum, fintech constitutes a disruptive force for workers but not for (shareholders of) firms, and there is a win-win situation at firms that are originators of new technology."（fintech，引言 ¶7 末句，结果部分总收束）
适用：收束句必须把本段/节的多个结果合并成一个可引用的判断，不能只是重复最后一行数字。风险：收束句的断言强度不得超过段内证据的最弱一环（导师层 A11 的摆位不改变这一条；不利分量在收束句中不得蒸发）。

**15. 路线图**
骨架：The paper is organized as follows.＋Section［n］［动词］［该章职务］.…（逐节一句）
例句：
- "The paper is organized as follows."（LOCAL，引言末段起句，其后逐节列明 2–9 章）
- "Section 4 describes the construction of the instrumental variable for geographic diversification, presents the instrumental variable results, and assesses the validity of the instrument."（GEO，引言路线图段：一节一句、动词领起）
- "Section 2 provides the institutional background, describes the current state of CoCo issuance, and presents an overview of the sample."（coco，引言 ¶8）
适用：多设定、多机制的复杂文章必备（示例政策 批注的加路线图建议与此一致）；单识别短篇可省（约 6/22 无路线图）。风险：路线图宣称的章节功能必须与正文实有内容一致——盲测第三轮 Fan 稿"路线图称 develops the hypotheses 而正文整节缺失"是文实不符的典型事故。

**16. 贡献宣称**
骨架：This paper is the first to［作为］.（须过事实门）／The main contribution of this paper is to［产出类型：定量因果证据/新测度/首个系统证据］.／Our study makes［n］main contributions.（先报数再逐条）
例句：
- "We believe that ours is the first paper to assess cross-firm stock price reactions to COVID-19 as functions of these pre-shock corporate characteristics."（IMM，引言 ¶3，带 We believe 软化）
- "The main contribution of this paper is to produce quantitative evidence for the causal effect of FinTech credit on entrepreneurial growth and development in the e-commerce sector."（FIN，引言 ¶6 首句）
- "Our study makes three main contributions to the assessment of MW effects."（MWCI，引言贡献段首句）
适用：每条贡献＝一个定位动作（近亲＋差异，见第 3 类）。风险（本类是全库风险最高的一类）：first-claim 是盲测三轮反复验证的失真源——无据的"首次"全数翻车；使用前两道检查：事实门（真没人做过？）与适用门（本文设定撑得起这个断言？）。软化版 "We believe that ours is the first…" 只降低语气、不降低举证责任。本体系自己的稿子九个"首次"全是事实义（首次生效），是干净的用法。

**17. 外推**
骨架：While our paper draws evidence from［场景］, the insights apply more broadly to［一般类］.／If there is some external validity from［本文场景］to［一般类］, the inference… is［判断］.
例句：
- "While our paper draws evidence from China, the insights apply more broadly to credit expansions, liquidity injections, and stimulus programs that have been introduced in many countries."（credit，引言外推段首句）
- "If there is some external validity from chess and stock analysis to skilled workers in general, the inference from our study is encouraging news for humans in the age of AI."（manplus，引言 ¶9，条件式外推独立成段）
- "Evidence on these issues can inform the policy debate about the growth contribution and welfare benefits of new credit technologies based on new extensive customer data (He, Huang, and Zhou, 2021)."（FIN，结论 ¶1，政策辩论外推）
适用：外推的主要栖息地是结论（见 2.10 与张力 T2）；引言内出现时以条件式（If…）或让步式（While…）为常态。风险：外推的边界与对冲同行（"While China's political environment differs…" 式让步限定）；不得把单国、单制度的结论无条件升格为一般命题。

---

## 4. 与现有体系的关系（印证 / 新增 / 张力）

对照对象：五份风格文件 v4、导师层（A1–A42）、中文语言层。张力只报告不裁决，裁决权在本体系。

### 4.1 印证（新语料独立复现了既有规则）

- **引言功能模板**：高昊宇文件 2.3 的逐段模板与导师层 A15 的功能清单，被跨池 22 篇的实测 modal 顺序独立复现（大问题→谜题→做法→数据/识别→分条发现→贡献→路线图）。两套既有规则互为表里、新语料为第三方证据。
- **摘要配额（A13）**：导师层的"英文约 100 词、结果 2–3 句、意义半句"与实测摘要中位 109 词、3–6 层结构基本吻合；高池六篇 88–108 词最贴 A13。
- **结论两段/短小（A35）**：实测结论占正文中位 3.1%、1–3 段，"维度要全、不加新料"与语料的"复述＋总判断"两件套一致。
- **引言稳健性预告合并（A18）**：22/22 引言发现块中稳健性均一句带过、不逐项展开——A18 不是导师个人偏好，是语料通例。
- **量级翻译与基数锚（A27＋sections/results.md）**：模式一的三级翻译（This means that…/Given that…）在高池结果章成对复现，LOCAL 例句自带 "(whose sample average is 8%)" 基数锚——"选口径、必带锚"的裁决口径有原文形态支撑。
- **对冲分级（language/zh.md §A）**：suggest 作为机制/裁决解读的默认领起动词在跨池例句中高频出现（第 9、11、14 类），与附则四级表一致；零结果照实报告（IMM 例句）印证 v3 C2 必留清单的零结果条款。
- **识别写高不写细（A25）＋先认难再给设计（导师层 A25 同向）**：引言识别多为一句话＋一个可检验事实，辩护细节留在设计章/辩护专段——与 A25、A25 三方同向。
- **单段粒度上限（V4-4）**：语料长段（>250 词）均靠段内编号/小三拍维持结构，与"超限须有内部结构"的口径互证。

### 4.2 新增（现有体系没有、本轮补上）

- **框架原型五型与选型条件**（1.2）：现有体系只有单篇风格与导师的结构变体（A10 贴身式），没有"按贡献类型选整篇骨架"的决策层。原型 D 的**测度三段式（构造→验证→使用，验证永不与构造同节）**是全新的硬规则（4/4 测度篇），对本体系的 LLM 文本测度支线直接可用。
- **结果章次序"先立可信度、再讲机制"**（1.3）：五份文件有稳健性密度与位置的零散规则，没有这条章际次序规则。
- **段内五模式**（3.1）：模式二（辩护段同序拆弹）与模式五（测度微缩段的分形结构）现有体系未覆盖；模式一的三级翻译此前只在高昊宇文件内有记录，本轮证实其为跨池搭配（IMM、FIN、LOCAL 各有标尺变体）。
- **引言识别辩护的轻重判据**（2.2）：辩护篇幅由"识别是否自建、是否招质疑"决定（GEO 46% vs 常态一句），现有体系只讲辩护的有无、不讲轻重。
- **结论功能可被引言提前完成**（1.3/2.10）：fintech 型"引言收束句代行结论"，解释了结论极短的成因，现有体系未记录。

### 4.3 张力（只报告，不裁决）

- **T1 制度背景的位置**：导师层 A15 把制度背景列为引言内的一个功能段（中文标尺 12–13 段之一）；英文语料中制度主体独立或合并成章（约 15/22），引言内至多一段制度细节。此为标尺差异还是实质分歧，待本体系定：可能与 A15 的适用对象是中文稿有关（导师层 §9 已注"中文段数标尺 vs 英文词数预算"，但位置问题未被那条覆盖）。
- **T2 外推段的位置**：A15 在贡献之前设独立外推段；语料引言中外推独立成段仅约 4/22，外推主要栖息在结论（FIN、cds、machine、manplus）与贡献段内部（credit ¶16 亦在引言后段，但紧随文献串）。若按 A15 写英文稿，引言会出现一个语料中罕见的段位。
- **T3 假设数量上限**：导师层 A20 定"关键假设一到两个"；语料编号假设篇中 ownership 2 条、subnational 2 条合规，但 tail 有 4 条编号假设（RFS 2014 体例、四条各对应一个理论渠道）。是个例（1 篇）还是体例差异（期刊/年代），样本不足以判定，报告备查。
- **T4 文献章的存废**：导师层 A15 与盲测 C1/H1 的既定口径是"综述从简、定位段不可缺"；语料中独立文献章仅 2/22（FIRM、FIN），与口径相容；但 Levine 簇的形态更激进——连独立定位段都没有、文献全织入理论段（IMM）或四解释并列（DEP）。"定位动作"的最低可接受形态到底是独立段、织入段、还是引言末一句 related-to-but-different，现有口径未细化，本轮证据显示三种形态都有顶刊样本。

---

## 5. 附录

### 附录 A：低置信个例（1–2 篇支撑，不进正文规则）

- **正负效应 GDP 量级对账节**：rise §4.6 专设一节把双面效应折算成同一量纲（损失 0.25% vs 收益 0.97% GDP），全语料仅此 1 篇。双面结论的论文可借用，但样本不足以立为规则。
- **轶事/引语开篇**：cds 以 Friedman 引语开篇、machine 以 Buffett 年报轶事开篇、manplus 以 Kasparov 轶事为动机段——3 篇各异，均属高风险修辞（与作者地位与期刊体例相关），不建议模仿立规。
- **结论列举政策选项**：coco 结论列举四个标准化选项，1 篇个例。
- **Levine 簇内句式**（池内 4 篇、跨团队未验证）：系数解读的 "consistent with the view" 型单句、替代解释排除句、转折句候选只在 Levine 簇检出，FIN 未检出同型单句；外推句式则相反，集中在 FIN。两组都只能记为团队文体候选。
- **识别整章前置**：credit 是高池唯一识别独立成章篇（全语料约 6/22 独立设计章），属少数派但非个例，已在正文按频次如实标注。

### 附录 B：语料缺口与打折清单（如实报告）

- **唐池最薄**：落盘全文 3 篇、有效独立样本 2 篇（subnational 为同文校准篇）；另两篇（JAEcon 2019、JAR 2024）只有公开文本通读，未作任何计数与例句来源。凡涉及唐的跨池结论均已按 2 篇降权。
- **tail-wag-dog-cds 计数失真**：RFS 双栏刊出稿 txt 把 Tables 2–9 数字块嵌进第 3 章，该篇结果章占比（71.6%）为抽取伪影，已剔除出一切占比统计；其功能段只做到小节级。
- **林池团队污染**：4/5 篇 Levine–Xie 簇；林/黄共享的 MS 2022 一篇两池均缺。林池共性按"跨簇成立才算共性"过滤，FIN 篇承担了对照功能。
- **高池 perils 降权**：文风疑由一作 Berger 主导，其"制度+数据+变量三合一成章""识别后置"两点已剔除出共性；其余篇目特征正常计入。
- **黄池 LOCAL 连字损坏**：txt 中 firm/finance 等高频词连字普遍损坏，含损坏词的例句或弃收或原样标注，LOCAL 例句数（10 条）为主动打折结果；黄池功能段为主题切分，段数不与他池横比。
- **Jiang 池版本与缺口**：5 篇均为工作论文/投稿稿 txt，与期刊定稿可能有细微出入；治理主线篇目未入池，治理类写作形态在本规则中缺位。
- **段界伪影通例**：各池段词数含混入的脚注文字（个别段偏高已在提取文件中逐处标注）；章节占比的分母口径池间有 1–2 个百分点级差异。所有中位数与区间应按 §0 的口径读，不要当作精密测量。
- **未覆盖**：中文论文语料不在本轮范围（本规则的句式库为英文；中文起草仍走中文语言层）；理论纯模型论文、宏观校准类论文的骨架不在五池覆盖内，原型五型只适用于实证/测度型论文。


## 总纲指针（2026-10-23）

本文件是论文写作规则体系的一层。体系入口与使用协议：`protocol.md`——接手任何论文写作任务先读总纲（文件地图、层级优先级、任务路由、工作纪律 D1–D7、失效模式 F1–F9、待裁决张力 T1–T5），再按路由加载本文件。
