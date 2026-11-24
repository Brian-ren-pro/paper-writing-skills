# writing_spec：英文顶刊引言写作实验（交接说明）

最后更新：2026-10-22（第 9 轮已完成）。接手的 agent 先读本页，再读最近一轮的 `REPORT.md`。

## 这条线在做什么

目标：给一份填好的**内容工作表（Content Brief）**，让模型写出读起来像 JF/RFS 已发表引言的 Introduction，且**不编造任何事实**。
方法：用已发表论文做"压缩—重写—盲判"实验。把原文压成工作表，让模型只凭工作表重写，再让盲判（Sonnet 子代理）区分原文和生成稿，并逐句审计事实。

## 核心资产（会被持续更新的"规则"）

| 文件 | 内容 |
|---|---|
| `intro_blueprint/INTRO_TEMPLATE_zh.md` | 中文填空手册：版式、段落功能卡、句子规则、空白工作表（§四）。第六节是第 8 轮新增的 **AI 痕迹自查清单** 和工作表新格子 I1–I4。改动前先把旧版备份到当轮目录 |
| `round9/guide_card_en_v5.txt` | 给写作模型看的英文规则卡（最新版）。v4 在 `round8/`，v3 在 `round7/`，v2 在 `round6/` |
| `round8/AI_TRACES.md` | 判官靠什么认出 AI 稿：每条线索、出现次数、该怎么写/不该怎么写 |
| `round7/ws_instructions_v3.md` | 从原文填工作表的指令（"没有就不填"） |
| `intro_blueprint/` 其余文件 | 117 篇语料的统计（`REPORT.md`、`LAYOUT_EVIDENCE.md`、`PHRASE_BANK.md`） |

## 各轮一览

| 轮 | 目录 | 改了什么 | 主要结论 |
|---|---|---|---|
| 5 | `round5/` | 工作表 v1 + 规则卡 v1，DeepSeek flash | 原文 18/18 被认出；编造 2.5% |
| 6 | `round6/` | 卡 v2（句长目标、段数按长度） | 用卡 8–4 胜不用卡；元叙述泄漏仍在 |
| 7 | `round7/` | 工作表 v3（没有就不填）+ 卡 v3；三个写手；二选一盲判 | 原文 72/72 被认出；用卡对 ds、gemini 有用（9–3），对 luna 无效（5–7）；编造降到 0.3–0.9% |
| 7 补 | `round7/quiz_split/` | 中英文 × 开头/中段 的拆分测验 | 模型判官 60/60 认出原文；Brian 本人中文开头 3/5。判官看的是作者声音、逐步搭概念、历史、例子、文献嵌入，以及原文的 PDF 噪声 |
| 8 | `round8/` | AI 痕迹清单 → 卡 v4；工作表 v4（+I1–I4）；原文去噪；写手 luna + ds；W（不给卡）vs C（给卡） | 给卡更好：ds 9–1、luna 7–3；原文仍 40/40 被认出，判官信心 4.1–4.9/5；去噪单独无效；luna 稿的识别线索转向原文对脚注/图/章节的指涉。详见 `round8/REPORT.md` |
| 9 | `round9/` | 原文二次去噪；卡 v5（评价不外推、长句目标 3–4%）；luna + ds；新增片段二选一、单篇 1–5 打分、背诵探针 | 原文仍全部被认出（整篇和片段均 0/10，打分原文 5.0、luna 约 2.0、ds 约 1.2）；卡 v5 对 ds 7–3、对 luna 5–5；luna 编造降到 0.7%；判官基本没背过原文。详见 `round9/REPORT.md` |

样本：6 篇 JF/RFS 引言（键名见各轮脚本的 `KEYS`）。第 8 轮起去掉 `ext_JF_177fcb832d`，因为抽取的原文从引言中间开始。原文全文在 `round5/out/{key}_O.md`（有 PDF 噪声），去噪版在 `round8/orig_clean/`，第 9 轮的二次去噪版在 `round9/orig_clean/`，比较时以后者为准。两处的改动都逐条记在各自的 `CLEAN_LOG.md`。

## 每轮的标准流程（脚本可直接复用）

都从**项目根目录**运行（`经管论文写作 skills/`），因为要读 `config.yaml`。

1. **工作表**：`roundN/ws_vX/{key}.json`。第 8 轮由 `round8/r8_ws_v4.py` 在 v3 上加 I 格。
2. **生成**：`python writing_spec/round8/r8_gen.py` 只生成 prompt；`GEN=luna,ds python writing_spec/round8/r8_gen.py` 调模型，已存在的稿子会跳过，所以断了重跑即可。日志在 `gen_log.jsonl`。
   - luna = `gpt-6-luna`，走本机代理 `127.0.0.1:8317`（代理要先开着）；ds = `deepseek-v4-flash`，max_tokens 32000；温度 0.7；只接受 `finish_reason=stop`。
3. **评测包**：`python writing_spec/round8/r8_eval_prep.py` 生成 `eval/packets/` 和答案钥匙 `eval/keys/`。
4. **盲判**：每个 packet 交给一个**全新的 Sonnet 子代理**，只让它读自己的 packet，把 JSON 写到 `eval/answers/<同名>.json`。子代理不能看到 prompt、规则卡或钥匙。
   - `2w_*`：原文 vs 一篇稿，二选一，两种顺序，第 8 轮加了 1–5 置信度
   - `pw_*`：两稿对比，两种顺序
   - `audit_*`：对照工作表逐句找无依据的句子
5. **出表**：`python writing_spec/round8/r8_report.py` → `eval/results.json`、`eval/report_tables.md`；再手写 `REPORT.md`（顶部放中文摘要）。

## 铁律

- **密钥**：DeepSeek key 只在脚本里从 `~/.deepseek_key` 读；代理 key 只在脚本里从 `config.yaml` 读。永远不要打印、记录、复制密钥或 `config.yaml`。
- **不改** `src/`、`corpus/`、`runs/`、`haiku_trial/`、`archive/`。每轮只在自己的 `roundN/` 里写；改模板前先备份。
- **语料摘录**写进文件时每段不超过 25 个词。工作表用意译笔记，不抄原句。
- **规则只管怎么写，不管写什么**：例子、历史、理想实验、作者评价这类内容，只有工作表给了才写，绝不编。
- 盲判必须用全新子代理、去掉换行、两种顺序都跑；事实审计必须附工作表。

## 第 9 轮进度：已完成

结果见 `round9/REPORT.md`，顶部有中文摘要。Claude 本人的逐篇打分（非盲）在 `round9/my_scores.md`。脚本 `round9/r9_*.py` 可以直接复用：
- 生成脚本只给已有稿子的写手打包，写手被限额时可以先评另一个，之后补上；
- 评测包新增 `2x_*`（片段二选一）和 `rate_j*`（单篇打分）两类；
- `memprobe/` 是背诵探针。

luna 走代理时可能遇到 `429 model_cooldown`（用量上限），响应里会给出 reset 时间，到点重跑 `GEN=luna` 即可。

## 下一轮建议（第 10 轮从这里开始）

1. **规则卡**：针对稿子自己的毛病再改一版。
   - ds：不写自我宣告结构的路标句（"X provides the first force"、"We consider two opposing channels"），不写口号句，不按清单罗列渠道；
   - luna：少用套话式限定，减少润色感的过渡，不重复陈述结果。
2. **评测**：主指标改为单篇 1–5 打分，再加 Brian 本人盲读；二选一只作底线检查，因为它已到顶。
3. **流程**：生成稿之后由作者本人过一遍，加入判断和语气。规则不应该伪造笔误和个人瑕疵。
