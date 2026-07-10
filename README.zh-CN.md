`npx skills add TableSpark/gdpr-compliance-audit`

[English](README.md) | **简体中文**

# gdpr-compliance-audit

一个用于 **GDPR 合规审计**的智能体技能（agent skill）：对组织、系统、产品或政策进行审计，
输出结构化、逐条引用 GDPR 条款的发现（findings），并附带风险评级、按领域的 0–4 成熟度评分，
以及可直接落地执行的整改计划。

你可以直接粘贴隐私政策文本、供应商清单、数据流描述、AI 功能、数据泄露场景，或让它审计整个
组织。它按分阶段的审计方法论执行（范围界定 → 数据映射 → 合法性 → 透明度 → 数据主体权利 →
治理 → 安全与泄露 → 供应商与跨境传输 → 发现汇总），每条发现都标注对应的 GDPR 具体条款。

## 安装

```bash
# 跨 agent 安装（Claude Code、Codex、Cursor 等 60+ 种 agent）
npx skills add TableSpark/gdpr-compliance-audit

# 仅安装到 Claude Code（全局）
npx skills add TableSpark/gdpr-compliance-audit -a claude-code -g
```

## 适用范围与限制

- **仅覆盖 GDPR / 欧盟数据保护法。** 对于 CCPA、PIPL 或其他法域的问题，它会明确说明
  GDPR 不适用并停止，而不是强行套用 GDPR 分析。
- **不构成法律意见。** 输出是结构化的差距分析，供你交给 DPO 或法律顾问参考。
- 只基于你提供的证据进行评估；证据缺失的部分会归入"无法评估"，绝不默认合规。
- 设计上**不会**估算罚款金额、不会引用具体执法案例。

## ⚠️ 内容基准时间：2026 年 7 月

本技能编码的是会变化的法律。内置的 `references/current-landscape.md` 描述的是
**2026 年 7 月**时几个易变事项的状态——依赖以下任何内容前，请先核实最新进展：

- **欧美数据隐私框架（DPF）**——正面临法律挑战；请查阅官方 DPF 名单及充分性认定的复审动态。
- **Digital Omnibus 改革**——GDPR 修订仍在立法进程中，尚无定论。
- **AI 法案（AI Act）时间表**——高风险义务自 2026 年 8 月起分阶段生效。

技能本身被指示对这些内容"核实而非断言"，但过期的仓库副本无法标记它不知道的变化。
凡涉及跨境传输或 AI 的审计，请重新核实上述易变事项。

## 目录结构

```
skills/gdpr-compliance-audit/
├── SKILL.md                    # 触发描述 + 审计流程 + 输出格式契约
├── references/
│   ├── articles.md             # 适用范围、原则、合法性基础、权利、义务、条款速查表
│   ├── audit-phases.md         # Phase 0–8 审计方法论 + 成熟度量表
│   └── current-landscape.md    # 易变内容（DPF、Digital Omnibus、AI 法案）——会过期！
├── scripts/
└── evals/evals.json            # 开发本技能时使用的测试用例与断言
```

采用 `skills/<name>/` 布局，为将来的姊妹法域模块（CCPA、PIPL、英国 DUAA）预留空间。

## 许可证

MIT——见 [LICENSE](LICENSE)。
