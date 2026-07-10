<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://tablespark.uk/assets/brand/tablespark-wordmark-reversed.svg">
  <img src="https://tablespark.uk/assets/brand/tablespark-wordmark.svg" alt="TableSpark" height="44">
</picture>

<br><br>

# gdpr-compliance-audit

**一个 GDPR 合规审计智能体技能——输出的是*可查证的发现*，不是感觉。**

[![Install](https://img.shields.io/badge/npx-skills%20add%20TableSpark%2Fgdpr--compliance--audit-566F46?style=flat-square)](https://github.com/TableSpark/gdpr-compliance-audit)
[![Benchmark](https://img.shields.io/badge/%E8%AF%84%E6%B5%8B%E9%80%9A%E8%BF%87%E7%8E%87-100%25%20vs%20%E5%9F%BA%E7%BA%BF%2066.7%25-3F5334?style=flat-square)](#05--性能数据)
[![Current as of](https://img.shields.io/badge/%E6%B3%95%E5%BE%8B%E5%9F%BA%E5%87%86%E6%97%B6%E9%97%B4-2026%E5%B9%B47%E6%9C%88-71B357?style=flat-square)](#04--合规与审计)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20%E5%93%81%E7%89%8C%E5%A3%B0%E6%98%8E-8C8C8C?style=flat-square)](#07--许可证与品牌声明)

[English](README.md) | **简体中文**

<sub>基于评测驱动的 SKILL-CREATOR 循环构建 &nbsp;✦&nbsp; 每条发现都注明具体条款</sub>

</div>

---

```bash
npx skills add TableSpark/gdpr-compliance-audit                    # 任意 agent（Claude Code、Codex、Cursor 等 60+）
npx skills add TableSpark/gdpr-compliance-audit -a claude-code -g  # 仅 Claude Code，全局安装
```

---

## 01 — 项目概览

<sub>这是什么 &nbsp;·&nbsp; Fig. 01</sub>

**智能体技能（agent skill）**是一个包含指令与参考材料的目录，AI 编程智能体在遇到匹配任务时按需
加载——它改变的是智能体*工作的方式*。这个技能把通用智能体变成一名*有纪律的* GDPR 审计员。

你可以给它：粘贴的隐私政策、供应商清单、数据流描述、AI 功能、数据泄露场景，或整个组织。
它按分阶段的审计方法论执行，并返回：

| 输出 | 形态 |
|---|---|
| **执行摘要** | 整体合规态势、最高风险差距、哪些内容无法评估 |
| **发现（Findings）** | 每条一组记录：领域 · 条款 · 状态（`Compliant / Partial / Non-compliant / N/A`）· 证据 · 风险 · 整改措施 |
| **按领域的成熟度** | `0 缺失 → 1 临时 → 2 有文档 → 3 已运转 → 4 有度量/持续` |
| **无法评估的事项** | 逐项列出缺失的证据——绝不把沉默默认为合规 |

设计目标是*可辩护性（defensibility）*：每个结论都对应具体的 GDPR 条款，每个状态都有输入中的
证据支撑，证据支撑不了的部分明确声明"无法评估"而不是猜测。

**它刻意拒绝做的事**与它做的事同样重要：

- **绝不编造罚款金额、执法案例或 EDPB 决定**——这是合规工具最危险的失败模式，由一条常驻测试断言持续压制为零。
- **绝不把 GDPR 审计强加给范围之外的问题**（仅 CCPA、PIPL、无欧盟数据主体的场景）——它会说明 GDPR 不适用并停止。
- **绝不断言易变的法律**（DPF 状态、Digital Omnibus、AI 法案时间表）——它会标记不确定性并提示你核实最新状态。

## 02 — 目录结构

<sub>解剖图 &nbsp;·&nbsp; Fig. 02</sub>

```
skills/gdpr-compliance-audit/
├── SKILL.md                    # 触发描述 · 分阶段流程 · 锁定的输出契约
├── references/
│   ├── articles.md             # 适用范围、原则、合法性基础、权利、义务 + 条款速查表
│   ├── audit-phases.md         # Phase 0（范围界定）→ Phase 8（发现汇总）方法论 + 成熟度量表
│   └── current-landscape.md    # 易变层（DPF、Digital Omnibus、AI 法案）——核实而非断言
├── scripts/
└── evals/evals.json            # 6 个测试场景 · 53 条断言——本技能的回归测试套件
```

知识按*衰减速率*分层：`articles.md` 是稳定的法律（2018 年至今），而 `current-landscape.md`
把所有还在变动的内容隔离出来，便于独立刷新——以及独立地"不信任"。`skills/<name>/` 布局为
姊妹法域模块（CCPA、PIPL、英国 DUAA）预留了空间。

## 03 — 开发过程

<sub>它是怎么建成的 &nbsp;·&nbsp; Fig. 03</sub>

这个技能不是一次写成的。它用 Anthropic 的 **skill-creator** 循环构建——起草 → 在真实提示词上
运行、*旁边跑一个无技能基线做对照* → 逐条断言评分 → 阅读失败之处 → 泛化地修复——重复直到
输出不再提升。

| 里程碑 | 发生了什么 |
|---|---|
| **脚手架** | 25 页 GDPR 框架按衰减速率拆成三个 reference 文件；在任何测试之前先锁定输出契约 |
| **迭代 1 — 运行** | 6 个场景 × 2 种配置（带技能 / 不带技能）= 12 次独立智能体运行 |
| **迭代 1 — 评分** | 第一轮评分 100% vs 97.7%——评分智能体一致指出断言*缺乏区分度*（测的是通用 GDPR 知识，不是审计契约） |
| **断言升级** | 每个场景新增 4 条契约断言（精确状态词表、逐条款引用、0–4 成熟度、无法评估章节）；重新评分：**98.3% vs 66.7%**——技能的真实价值变得可度量 |
| **迭代 2 — 精修** | 唯一一次带技能失败（复合状态标签 "Non-compliant risk pending action"）通过收紧 SKILL.md 契约措辞修复；全部 12 次运行重跑验证：**100%（53/53），零回归** |

评测套件随仓库发布在 `evals/evals.json`，循环可以继续：改动技能 → 重跑 6 个场景 → 53 条断言
告诉你什么回归了。

## 04 — 合规与审计

<sub>它检查什么 · 它承诺什么 &nbsp;·&nbsp; Fig. 04</sub>

**方法论。** 审计经过九个阶段，每个阶段产出离散、有证据的发现：范围与适用性 → 数据映射
（ROPA）→ 合法性（第 5–10 条）→ 透明度（第 12–14 条，EDPB 2026 年执法重点）→ 数据主体权利
（第 12、15–22 条）→ 治理（第 24–39 条）→ 安全与泄露（第 32–34 条）→ 供应商与跨境传输
（第 28、44–49 条）→ 发现、风险评级与整改。

**由测试套件验证的行为保证**（两轮迭代 12/12 次运行全部干净）：

- 每条发现都从内置条款速查表引用具体条款——没有无出处的结论。
- 所有记录在案的运行中，编造罚款/案例次数为**零**；只允许引用第 83 条的罚款*档位*。
- 证据缺失产出 `Partial`/`N/A` 发现并注明所需材料——沉默绝不升级为 `Compliant`。
- CCPA 近似场景验证了范围门有效：不会对纯美国场景强行输出 GDPR 审计。

> **⚠️ 法律基准时间：2026 年 7 月。** 内置的 `current-landscape.md` 快照涵盖欧美数据隐私框架
> （正面临法律挑战）、Digital Omnibus 改革（尚无定论）与 AI 法案时间表（高风险义务自 2026 年
> 8 月起生效）。技能被指示对这些内容*核实而非断言*——但过期的克隆无法标记它不知道的变化。
> 凡涉及跨境传输或 AI 的审计，请重新核实这些易变事项。

**不构成法律意见。** 输出是结构化差距分析，供你带给 DPO 或法律顾问——它让对话更快，
不能替代对话。

## 05 — 性能数据

<sub>实测，而非宣称 &nbsp;·&nbsp; Fig. 05</sub>

用 skill-creator 的评测框架进行基准测试：每个场景并行运行两次——一次带技能、一次不带
（相同模型、相同提示词）——再由独立的评分智能体对照 53 条断言给两份答案逐条打分。

| 指标 · 迭代 1 | 带技能 | 基线（无技能） | 差值 |
|---|---|---|---|
| 断言通过率 | **98.3%**（52/53） | 66.7%（33/53） | **+31.6 分** |
| 编造罚款 / 案例 | **0** | 0 | — |
| 范围门正确性（CCPA 近似场景） | ✓ 正确拒绝 | ✓ 正确拒绝 | 防线有效 |
| 单次审计耗时 | 103.6 秒 | 68.9 秒 | +34.7 秒 |
| 单次审计 token | ~41.9 k | ~28.2 k | +13.7 k |

| 指标 · 迭代 2（精修后） | 带技能 | 基线（无技能） | 差值 |
|---|---|---|---|
| 断言通过率 | **100%**（53/53） | 66.7% | **+33.3 分** |
| 编造罚款 / 案例 | **0** | 0 | — |
| 单次审计耗时 | 106.9 秒 | 71.6 秒 | +35.3 秒 |
| 单次审计 token | ~42.6 k | ~28.3 k | +14.3 k |

迭代 1 的失败项（复合状态标签）在收紧契约措辞后没有复发——且开销在两轮迭代间保持平稳，
这次修复没有付出任何额外成本。

+32 分的来源：基线能写出*懂行的散文*，但不满足审计*契约*——没有状态词表、没有逐条发现的
条款引用、没有成熟度评分、没有声明评估缺口。而这份契约正是让审计结果可执行、可跨时间对比
的东西，也正是技能所强制的。开销（+35 秒、+14k token）是智能体在开口之前真正去读参考法条
的成本。

测试场景：隐私政策审计 · 跨境传输审计 · 技术栈中的 LLM · CCPA 近似场景（必须拒绝）·
72 小时泄露时钟 · 访问 + 删除请求。

## 06 — 路线图

<sub>下一步 &nbsp;·&nbsp; Fig. 06</sub>

- **触发调优**——用约 20 条触发评测（过触发/欠触发用例）优化技能描述。
- **姊妹法域**——目录布局已为 `ccpa/`、`pipl/`、`uk-duaa/` 参考模块预留空间。
- **`current-landscape.md` 刷新节奏**——易变层设计为可整体替换，不触碰稳定法律层。

## 07 — 许可证与品牌声明

<sub>使用规则 &nbsp;·&nbsp; Fig. 07</sub>

技能源文件（SKILL.md、references、evals）以 **MIT 许可证**发布——见 [LICENSE](LICENSE)——
你可以为自己的合规工作使用、修改和扩展它。

**品牌与材料声明。** 本项目及其文档、编纂的知识库是 **TableSpark** 的资产。TableSpark 名称、
spark 符号与字标（wordmark）为 TableSpark 品牌资产，不得用于为衍生作品背书。
**禁止出售本材料，或将其打包进任何用于销售的商业产品。** 使用它、学习它、为你自己的审计
改编它——但不要转售它。

---

<div align="center">

<a href="https://tablespark.uk/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://tablespark.uk/assets/brand/tablespark-wordmark-reversed.svg">
  <img src="https://tablespark.uk/assets/brand/tablespark-wordmark.svg" alt="TableSpark" height="32">
</picture>
</a>

<sub><a href="https://tablespark.uk/">TABLESPARK</a> 资产 &nbsp;<b>✦</b>&nbsp; BEAUTIFUL WEBSITES FOR RESTAURANTS</sub>

<sub>GDPR COMPLIANCE AUDIT · V1.1 · 2026 &nbsp;·&nbsp; LONDON · 51.5072°N · 0.1276°W</sub>

</div>
