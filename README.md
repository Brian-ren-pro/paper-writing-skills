# 经管论文写作 skills

写中英文经管论文用的写作规则体系。2026-11-11 重组为 v3。

## 目录

| 位置 | 内容 |
|---|---|
| `paper-writing-system/` | 技能源文件（可直接编辑）。入口 `SKILL.md`，总纲 `references/protocol.md` |
| `paper-writing-system.skill` | 打包好的技能，安装用这个 |
| `source_materials/writing_spec_products/` | 10 月英文引言实验的成品：引言填空手册、句式库、版式证据、AI 痕迹清单、规则卡 v6、写手笔记 |
| `_archive_2026-10/` | 归档：10 月的自动改写引擎、引言实验过程文件、旧版技能包（v1、v2.0、v2.1） |

`bankdata/` 已移到 `02_Scientific_Research/bankdata/`。

## v3 的分层（写到哪里查哪里）

```
references/
├─ protocol.md          总纲：任务路由、工作纪律、工作方法、失效模式、待裁决张力
├─ workflow.md          标准作业流程：阶段 0—8，每阶段的必需产出与闸门
├─ structure.md         结构层：写作模式（E/ZE/ZC）、总原则、框架选型、篇幅预算、章节间交叉引用
├─ sections/            章节层：摘要、引言（附英文引言规则卡）、背景与文献、理论与假设、
│                       数据与变量、识别、结果（含全稿数字纪律）、稳健性、机制与异质性、
│                       结论、表图公式脚注附录
├─ language/            语言层：zh.md、en.md、ai-tone.md（去 AI 味）
├─ voices/              学者风格插件（可选）
└─ sources/             来源与证据：导师指导原始条目、判例库、Zotero 语料统计、22 篇精标语料、协作元规则
```

每条规则标注来源：【导师 Ax】【语料】【22 篇】【判例 C-xx】【Brian】。

技能根目录另有：
- `scripts/run_checks.py`：一键检查（句式红线、冒号、节首节末、长句、人称、术语、交叉引用、数字、参考文献）；
- `scripts/docx_tools.py`：docx 文本导出与最小替换；
- `plugins/word-layout/`：Word 排版插件（档案 cn-workingpaper、cn-journal、en-submission）；
- `templates/`：开工信息表、事实底稿、术语表、RUNLOG、修订说明。

## 维护

规则修改走"提案 → Brian 批准 → 改源文件 → 写修订日志 → 重新打包"。重新打包：在本目录执行 `zip -qr paper-writing-system.skill paper-writing-system`。语料统计的方法与结果在 `references/sources/corpus-evidence.md`。
