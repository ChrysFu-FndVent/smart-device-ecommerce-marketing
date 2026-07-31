<div align="right"><a href="#简体中文">简体中文</a> | <a href="#english">English</a></div>

<a id="简体中文"></a>

# 智能设备与电商产品数据营销工作流

<div align="center">

<strong>多来源商品文本 → 可回查数据观察 → 待验证营销假设 → 可追溯概念物料</strong>

![Scope](https://img.shields.io/badge/Scope-Cross--Category-EA580C?style=for-the-badge)
![Method](https://img.shields.io/badge/Method-Data%20%2B%20Spec%20Traceability-0369A1?style=for-the-badge)
![Case](https://img.shields.io/badge/Case-134%20Public%20Texts-7C3AED?style=for-the-badge)
![Review](https://img.shields.io/badge/Release-Human%20Review-166534?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)

[跨品类流程](./workflows.md) · [能力契约](./skills.md) · [Prompt 模式](./prompt-engineering.md) · [营销设计](./product-design.md) · [分析模板与案例](./data-analysis.md)

</div>

> [!NOTE]
> 本仓库是一套**跨品类电商数据营销工作流、Prompt 模式库与案例报告**，并提供 Python 品类配置校验器；它不是只服务智能手环的营销工具，也不是完整的分析插件。智能手环仅用于展示完整实例化过程。

## 目录

- [简介](#简介)
- [项目亮点](#项目亮点)
- [效果展示](#效果展示)
- [品类配置接口](#品类配置接口)
- [功能清单](#功能清单)
- [AI 与人工责任](#ai-与人工责任)
- [技术与方法栈](#技术与方法栈)
- [安装与部署](#安装与部署)
- [项目结构](#项目结构)
- [已验证案例：智能手环](#已验证案例智能手环)
- [FAQ](#faq)
- [验收与边界](#验收与边界)

## 简介

商品营销经常在两个环节失真：分析阶段把混合来源文本当成市场总体，生成阶段又把数据观察改写成未经核验的规格或功效。本项目通过 `category_config` 把品类词典、分析维度、正式规格源、风险规则和渠道要求显式配置，再要求每个洞察与物料元素回到数据或规格依据。

适用品类包括但不限于：

`智能穿戴` · `智能家居` · `消费电子` · `家电` · `美妆个护` · `家居日用` · `户外装备` · `宠物用品`

| 输入 | 输出 |
|---|---|
| 品类配置、公开文本、来源标签、正式规格、风险规则、目标渠道 | 描述统计、主题网络、用户/卖点假设、营销架构、元素溯源表、文案或概念视觉 |

## 项目亮点

- 🧰 **品类配置化**：通用的是输入输出契约，不是某个案例的词典与标签。
- 🔗 **来源可回查**：每条文本保留来源类型、URL、时间和版本字段。
- 📐 **动态维度标注**：新品类先试标、校准，再冻结维度和词典版本。
- 🧠 **观察与假设分离**：统计结果不直接等同于购买动机或传播效果。
- 🧾 **数据与规格双溯源**：信息优先级来自数据，具体参数来自正式规格源。
- 🧯 **负面长尾优先检查**：低样本用于风险发现，不用于排名优劣。
- 🎨 **概念物料可审计**：功能元素、可见文字、风险声明和待核对项逐项记录。

## 效果展示

### 通用品类配置

```yaml
category: 扫地机器人
business_question: 哪些问题应进入详情页首屏与负面风险检查
sources: [公开评论, 商品问答, 测评, 产品页]
analysis_dimensions: [清洁力, 避障, 噪音, 维护, 连接, 售后]
spec_source: [正式规格表, 说明书, 检测或授权资料]
risk_rules: [性能条件, 认证表述, 禁止虚构配件与功能]
target_channel: 电商详情页
required_output: [数据观察, 待验证假设, 卖点层级, 元素溯源表]
```

### 跨品类处理链

<p align="center">
  <img src="./assets/readme-architecture.svg" alt="多品类商品通过品类配置、多源文本分析、证据质检、营销策略和物料复核形成输出的流程图" width="100%">
</p>

<p align="center"><sub>可编辑版本：<a href="./assets/readme-architecture.drawio">readme-architecture.drawio</a></sub></p>

## 品类配置接口

| 配置项 | 作用 | 智能手环案例 | 其他品类示例 |
|---|---|---|---|
| `category_terms` | 名称、同义词和型号 | 手环、手表、健康监测设备 | 扫地机、洗地机；精华、面霜 |
| `analysis_dimensions` | 统计属性维度 | 健康、安全、佩戴、续航等 14 维 | 清洁力、避障、噪音；肤感、成分、包装 |
| `spec_source` | 具体参数的事实来源 | 正式产品资料与检测依据 | 规格表、说明书、质检报告、授权素材 |
| `risk_rules` | 禁用词、资质与声明要求 | 医疗健康表述与设备资质 | 功效宣称、儿童安全、环保认证 |
| `target_channel` | 内容结构和规格 | 详情页、海报、短视频 | 搜索广告、直播脚本、社媒图文 |

案例中的维度、阈值和风险词不能直接复制到其他品类。

## 功能清单

| 能力 | 交付物 | 文档 |
|---|---|---|
| 多源文本采集适配 | 来源 Schema、失败日志、授权边界 | [skills.md](./skills.md) |
| 动态文本分析 | 品类词典、维度版本、情感与属性统计 | [skills.md](./skills.md) |
| 主题与问题长尾 | 共现网络、主题社区、负面原文簇 | [data-analysis.md](./data-analysis.md) |
| 强制引用式解读 | 数据观察、分母、反面解释、待验证假设 | [prompt-engineering.md](./prompt-engineering.md) |
| 营销产品设计 | 用户关系、三层卖点、六模块营销架构 | [product-design.md](./product-design.md) |
| 溯源式物料 | 数据依据、规格依据、风险项、可见文字清单 | [skills.md](./skills.md) |

## AI 与人工责任

| 环节 | AI 可承担 | 人工必须负责 |
|---|---|---|
| 配置 | 提取候选术语、属性和风险词 | 确定品类边界、定义、规格源和审核人 |
| 采集与分析 | 辅助生成采集、清洗、统计和可视化代码 | 来源授权、抽样策略、口径、运行验收 |
| 洞察 | 提供带数字引用的候选解释 | 回查结果，区分观察、假设与业务判断 |
| 营销方案 | 生成结构化初稿和文案候选 | 卖点优先级、渠道策略和风险红线 |
| 视觉物料 | 生成概念稿和版式候选 | 规格、资质、品牌、版权与发布审批 |

## 技术与方法栈

| 层级 | 工具或方法 |
|---|---|
| 数据契约 | YAML `category_config`、来源 Schema、版本字段 |
| 文本处理案例 | jieba、自定义词典、双层停用词 |
| 情感案例 | SnowNLP（需用新品类人工集重新校准） |
| 主题网络案例 | Counter、词共现、NetworkX、贪心模块度社区 |
| 参考实现 | Python 3 标准库；品类配置完整性、去重、证据闸门与人工发布复核标记 |
| Agent / Prompt | 约束式代码生成、强制引用解读、受控文案、证据先行视觉 |
| 视觉资产 | 数据图表、AI 概念海报、元素溯源表 |
| 文档 | Markdown、YAML、JSON、draw.io、SVG、GitHub Alerts |

> 案例分析数字来自未随仓库发布的 `problem2_analysis.py` 运行结果。本仓库保留方法、参数与报告，不提供可直接执行的分析脚本。

## 安装与部署

### 获取工作流

```bash
git clone https://github.com/ChrysFu-FndVent/smart-device-ecommerce-marketing.git
cd smart-device-ecommerce-marketing
```

README 和方法文档无需安装依赖。配置校验器使用 Python 3.9 或更高版本，不依赖第三方包：

```bash
python3 src/category_config.py
python3 src/category_config.py --self-test
```

该脚本只校验品类配置，不执行采集、情感分析、主题网络或营销内容生成。若要为新品类实现完整分析代码，应根据 [prompt-engineering.md](./prompt-engineering.md) 的代码生成契约建立独立 Python 环境、测试和数据版本管理。

### 部署方式

配置校验器不是 Web 服务，不需要端口或数据库。可在数据营销流水线开始前调用 `validate_config`，阻止缺少来源、分析维度、正式规格源或风险规则的任务进入后续阶段：

```python
from src.category_config import validate_config
```

采集、清洗、情感分析、主题网络、物料生成和发布审核需要由独立组件部署。不同品类应使用各自版本化配置和人工验证集，不能共用案例阈值。

### 新品类迁移步骤

1. 在 [skills.md](./skills.md) 中填写并评审 `category_config`。
2. 抽取小样本人工试标，修订维度、词典、停用词和风险规则。
3. 按 [workflows.md](./workflows.md) 采集、清洗并保留来源与失败记录。
4. 参考 [data-analysis.md](./data-analysis.md) 冻结参数、分母和输出版本。
5. 用 [prompt-engineering.md](./prompt-engineering.md) 分离数据观察、反面解释和待验证假设。
6. 按 [product-design.md](./product-design.md) 建立卖点层级与元素溯源表。
7. 发布前完成规格、资质、广告、版权、隐私和可访问性审核。

## 项目结构

```text
smart-device-ecommerce-marketing/
├── README.md
├── .gitignore                   # Python 缓存忽略规则
├── workflows.md                 # 品类闸门与六段数据营销流程
├── skills.md                    # 四类能力契约与 category_config
├── prompt-engineering.md        # 四种可验证 Prompt 模式
├── product-design.md            # 用户、卖点与营销模块
├── data-analysis.md             # 通用分析模板与手环案例
├── src/
│   └── category_config.py       # Python 品类配置校验参考实现
└── assets/
    ├── readme-architecture.drawio  # 可编辑跨品类流程图
    ├── readme-architecture.svg     # README 矢量展示图
    ├── feature-radar.png        # 案例功能维度雷达图
    └── marketing-poster-gpt-image-2.png  # AI 概念海报
```

## 已验证案例：智能手环

| 项目 | 记录 | 使用边界 |
|---|---:|---|
| 样本 | **134 条 / 7 个来源标签 / 20 个品牌** | 公开混合文本，不是随机电商评论 |
| 属性 | **14 维**；健康监测提及率 **38.8%** | 提及率不等于购买重要度 |
| 主题 | **4 个主题社区** | 社区命名需回看原文，不等于传播效果 |
| 情感 | SnowNLP 均值 **0.795** | 只描述当前偏正样本 |
| 视觉 | **9 项**海报元素建立初版溯源表 | 具体规格仍需正式资料核验 |

这些数字证明的是工作流能从一个案例走到可核查物料，不是其他品类的默认基线。

## FAQ

<details>
<summary><strong>这个项目是否只适用于智能手环？</strong></summary>

不是。手环是验证案例。迁移时保留数据 Schema、证据质检和双溯源方法，重新建立品类词典、分析维度、模型阈值、规格源与风险规则。
</details>

<details>
<summary><strong>为什么克隆后找不到分析脚本？</strong></summary>

公开仓库交付方法、参数、Prompt、结果、视觉资产和独立编写的配置校验器，不发布原案例分析脚本。配置校验器不能复现案例数字；新品类的完整实现仍需在独立环境中补齐分析代码、依赖锁定和测试。
</details>

<details>
<summary><strong>SnowNLP 情感得分可以跨品类直接复用吗？</strong></summary>

不可以。通用模型在医疗健康、美妆、食品或家电术语中可能误判。应建立小规模人工验证集，重新校准词典、阈值和错误模式。
</details>

<details>
<summary><strong>概念海报可以直接发布吗？</strong></summary>

不可以。先逐项核对所有可见文字、规格、功能、资质、人物形象、版权和必要声明。没有正式规格依据的内容必须删除或保留为内部占位。
</details>

<details>
<summary><strong>低样本品牌能否进行排名？</strong></summary>

不能。低样本只用于发现可能的风险主题，应展示样本量并回看原文，不应外推品牌总体口碑或因果关系。
</details>

<details>
<summary><strong>部署配置校验器后能直接生成营销物料吗？</strong></summary>

不能。校验器只确认品类配置是否完整，并标记证据闸门与人工发布复核要求。文本分析、洞察生成、规格核对、视觉制作和发布审批仍需独立实现并逐步验收。
</details>

## 验收与边界

- 每个策略结论附统计依据，或明确标为待验证假设。
- 数字、型号、材质、尺寸、性能、功效均回到正式规格源。
- 来源授权、隐私、版权、广告规范和品类专项要求由人工复核。
- 混合来源样本不作为市场总体，时间推断不作为严格时序结论。
- 新品类必须重新校准情感模型、词典、维度和阈值。

---

<a id="english"></a>

# Smart Device and E-commerce Product Data Marketing Workflow

<div align="center">

<strong>Multi-source product text → Auditable data observations → Marketing hypotheses to validate → Traceable concept assets</strong>

![Scope](https://img.shields.io/badge/Scope-Cross--Category-EA580C?style=for-the-badge)
![Method](https://img.shields.io/badge/Method-Data%20%2B%20Spec%20Traceability-0369A1?style=for-the-badge)
![Case](https://img.shields.io/badge/Case-134%20Public%20Texts-7C3AED?style=for-the-badge)
![Review](https://img.shields.io/badge/Release-Human%20Review-166534?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)

[Cross-category Workflow](./workflows.md) · [Capability Contracts](./skills.md) · [Prompt Patterns](./prompt-engineering.md) · [Marketing Design](./product-design.md) · [Analysis Templates and Case](./data-analysis.md)

</div>

> [!NOTE]
> This repository contains a **cross-category e-commerce data marketing workflow, prompt-pattern library, and case report**, plus a Python category-configuration validator. It is not a marketing tool exclusively for smart bands, nor a complete analytics plugin. The smart-band case demonstrates the full instantiation process.

## Table of Contents

- [Introduction](#introduction)
- [Highlights](#highlights)
- [Example](#example)
- [Category Configuration Interface](#category-configuration-interface)
- [Capabilities](#capabilities)
- [AI and Human Responsibilities](#ai-and-human-responsibilities)
- [Technology and Method Stack](#technology-and-method-stack)
- [Installation and Deployment](#installation-and-deployment)
- [Project Structure](#project-structure)
- [Validated Case: Smart Bands](#validated-case-smart-bands)
- [FAQ](#faq)
- [Acceptance Criteria and Boundaries](#acceptance-criteria-and-boundaries)

## Introduction

Product marketing often becomes distorted at two points: the analysis stage treats mixed-source text as representative of the whole market, and the generation stage rewrites data observations as unverified specifications or efficacy claims. This project uses `category_config` to explicitly configure category dictionaries, analysis dimensions, authoritative specification sources, risk rules, and channel requirements, then requires every insight and asset element to map back to data or specification evidence.

Applicable categories include, but are not limited to:

`smart wearables` · `smart home` · `consumer electronics` · `home appliances` · `beauty and personal care` · `household goods` · `outdoor equipment` · `pet supplies`

| Input | Output |
|---|---|
| Category configuration, public text, source labels, authoritative specifications, risk rules, and target channel | Descriptive statistics, topic networks, user/selling-point hypotheses, marketing architecture, element traceability table, and copy or concept visuals |

## Highlights

- 🧰 **Category configuration**: input/output contracts are reusable; a case-specific dictionary and labels are not.
- 🔗 **Auditable sources**: every text item retains source type, URL, time, and version fields.
- 📐 **Dynamic dimension labeling**: pilot-label and calibrate a new category before freezing dimensions and dictionary versions.
- 🧠 **Separate observations from hypotheses**: statistical results do not directly equal purchase motivation or communication effectiveness.
- 🧾 **Dual traceability for data and specifications**: data determines information priority; authoritative specifications determine concrete parameters.
- 🧯 **Prioritize negative long-tail checks**: low-sample data finds risks; it does not rank products.
- 🎨 **Auditable concept assets**: record functional elements, visible text, risk statements, and pending checks item by item.

## Example

### Generic Category Configuration

```yaml
category: Robot vacuum
business_question: Which issues belong above the fold on the product page and in negative-risk checks?
sources: [public reviews, product Q&A, evaluations, product pages]
analysis_dimensions: [cleaning, obstacle avoidance, noise, maintenance, connectivity, after-sales]
spec_source: [official specification sheet, manual, testing or authorized material]
risk_rules: [performance conditions, certification wording, no fabricated accessories or features]
target_channel: E-commerce product page
required_output: [data observations, hypotheses to validate, selling-point hierarchy, element traceability table]
```

### Cross-category Processing Pipeline

<p align="center">
  <img src="./assets/readme-architecture.svg" alt="Workflow in which multiple product categories pass through category configuration, multi-source text analysis, evidence quality control, marketing strategy, and asset review" width="100%">
</p>

<p align="center"><sub>Editable source: <a href="./assets/readme-architecture.drawio">readme-architecture.drawio</a></sub></p>

## Category Configuration Interface

| Configuration | Purpose | Smart-band Case | Other Category Examples |
|---|---|---|---|
| `category_terms` | Names, synonyms, and models | band, watch, health-monitoring device | robot vacuum, floor washer; serum, face cream |
| `analysis_dimensions` | Statistical attribute dimensions | 14 dimensions including health, safety, wear, and battery life | cleaning, obstacle avoidance, noise; feel, ingredients, packaging |
| `spec_source` | Factual source for concrete parameters | Official product material and test evidence | specification sheets, manuals, quality reports, authorized assets |
| `risk_rules` | Prohibited terms, qualifications, and disclosure requirements | Medical/health wording and device qualifications | efficacy claims, child safety, environmental certification |
| `target_channel` | Content structure and format | Product pages, posters, short videos | Search ads, livestream scripts, social posts |

Dimensions, thresholds, and risk terms from the case must not be copied directly to another category.

## Capabilities

| Capability | Deliverable | Document |
|---|---|---|
| Multi-source text collection adapters | Source schema, failure log, and authorization boundaries | [skills.md](./skills.md) |
| Dynamic text analysis | Category dictionary, dimension versions, sentiment and attribute statistics | [skills.md](./skills.md) |
| Topics and issue long tail | Co-occurrence network, topic communities, and negative-source clusters | [data-analysis.md](./data-analysis.md) |
| Mandatory citation-based interpretation | Data observations, denominator, counter-explanations, and hypotheses to validate | [prompt-engineering.md](./prompt-engineering.md) |
| Marketing product design | User relationships, three-level selling points, and six-module marketing architecture | [product-design.md](./product-design.md) |
| Traceable assets | Data basis, specification basis, risk items, and visible-text inventory | [skills.md](./skills.md) |

## AI and Human Responsibilities

| Stage | AI May Handle | Humans Must Own |
|---|---|---|
| Configuration | Extract candidate terms, attributes, and risk terms | Define category scope, definitions, specification sources, and reviewers |
| Collection and analysis | Assist in generating collection, cleaning, statistical, and visualization code | Source authorization, sampling, definitions, and execution acceptance |
| Insights | Offer candidate interpretations with numeric citations | Verify results and distinguish observations, hypotheses, and business judgment |
| Marketing plan | Generate structured drafts and candidate copy | Selling-point priority, channel strategy, and risk limits |
| Visual assets | Generate concepts and layout candidates | Specifications, qualifications, brand, copyright, and publication approval |

## Technology and Method Stack

| Layer | Tool or Method |
|---|---|
| Data contracts | YAML `category_config`, source schema, and version fields |
| Text-processing case | jieba, custom dictionary, and two-layer stop-word list |
| Sentiment case | SnowNLP; recalibrate with a human-labeled set for every new category |
| Topic-network case | Counter, word co-occurrence, NetworkX, and greedy modularity communities |
| Reference implementation | Python 3 standard library; category-configuration completeness, deduplication, evidence gates, and human-release-review markers |
| Agent / Prompt | Constrained code generation, citation-required interpretation, controlled copy, and evidence-first visuals |
| Visual assets | Data charts, AI concept poster, and element traceability table |
| Documentation | Markdown, YAML, JSON, draw.io, SVG, and GitHub Alerts |

> Case-analysis figures come from `problem2_analysis.py` runs that are not published with the repository. The repository retains methods, parameters, and reports, but does not provide a directly executable analysis script.

## Installation and Deployment

### Get the Workflow

```bash
git clone https://github.com/ChrysFu-FndVent/smart-device-ecommerce-marketing.git
cd smart-device-ecommerce-marketing
```

The README and method documents require no dependencies. The configuration validator requires Python 3.9 or later and has no third-party dependencies:

```bash
python3 src/category_config.py
python3 src/category_config.py --self-test
```

The script validates category configuration only. It does not collect data, analyze sentiment, build topic networks, or generate marketing content. To implement a full analysis for a new category, use the code-generation contract in [prompt-engineering.md](./prompt-engineering.md) and create an independent Python environment with tests and data-version management.

### Deployment

The validator is not a web service and needs no port or database. Invoke `validate_config` before a data-marketing pipeline starts to prevent tasks missing sources, analysis dimensions, authoritative specification sources, or risk rules from entering downstream stages:

```python
from src.category_config import validate_config
```

Collection, cleaning, sentiment analysis, topic networks, asset generation, and release review must be deployed as separate components. Each category needs its own versioned configuration and human validation set; case thresholds cannot be shared.

### Migration to a New Category

1. Complete and review `category_config` in [skills.md](./skills.md).
2. Human-label a small pilot sample and revise dimensions, dictionaries, stop words, and risk rules.
3. Follow [workflows.md](./workflows.md) to collect and clean data while retaining sources and failure records.
4. Use [data-analysis.md](./data-analysis.md) to freeze parameters, denominators, and output versions.
5. Use [prompt-engineering.md](./prompt-engineering.md) to separate data observations, counter-explanations, and hypotheses to validate.
6. Use [product-design.md](./product-design.md) to build the selling-point hierarchy and element traceability table.
7. Before publication, complete specification, qualification, advertising, copyright, privacy, and accessibility review.

## Project Structure

```text
smart-device-ecommerce-marketing/
├── README.md
├── .gitignore                   # Python cache ignore rules
├── workflows.md                 # Category gate and six-stage data-marketing workflow
├── skills.md                    # Four capability contracts and category_config
├── prompt-engineering.md        # Four verifiable prompt patterns
├── product-design.md            # Users, selling points, and marketing modules
├── data-analysis.md             # Generic analysis template and smart-band case
├── src/
│   └── category_config.py       # Python category-configuration validation reference
└── assets/
    ├── readme-architecture.drawio  # Editable cross-category workflow
    ├── readme-architecture.svg     # README vector diagram
    ├── feature-radar.png        # Case feature-dimension radar chart
    └── marketing-poster-gpt-image-2.png  # AI concept poster
```

## Validated Case: Smart Bands

| Item | Record | Boundary |
|---|---:|---|
| Sample | **134 texts / 7 source labels / 20 brands** | Mixed public text, not a random sample of e-commerce reviews |
| Attributes | **14 dimensions**; health-monitoring mention rate **38.8%** | Mention rate does not equal purchase importance |
| Topics | **4 topic communities** | Community names require source review and do not imply communication effectiveness |
| Sentiment | Mean SnowNLP score **0.795** | Describes only the current positively skewed sample |
| Visual | Initial traceability table for **9 poster elements** | Concrete specifications still require official verification |

These figures demonstrate that the workflow can move one case through to auditable assets; they are not default baselines for other categories.

## FAQ

<details>
<summary><strong>Is this project only for smart bands?</strong></summary>

No. The band is a validation case. When migrating, retain the data schema, evidence quality control, and dual-traceability method, but rebuild the category dictionary, analysis dimensions, model thresholds, specification sources, and risk rules.
</details>

<details>
<summary><strong>Why is the analysis script missing after cloning?</strong></summary>

The public repository delivers methods, parameters, prompts, results, visual assets, and an independently written configuration validator; it does not publish the original case-analysis script. The validator cannot reproduce case figures. A new category still requires analysis code, pinned dependencies, and tests in an independent environment.
</details>

<details>
<summary><strong>Can SnowNLP sentiment scores be reused across categories?</strong></summary>

No. A general model may misclassify medical, health, beauty, food, or appliance terminology. Build a small human validation set and recalibrate dictionaries, thresholds, and error patterns.
</details>

<details>
<summary><strong>Can the concept poster be published directly?</strong></summary>

No. Verify all visible text, specifications, functions, qualifications, people, copyright, and required statements item by item. Remove anything without authoritative specification evidence or keep it as an internal placeholder.
</details>

<details>
<summary><strong>Can brands with small samples be ranked?</strong></summary>

No. Low-sample data is only for identifying possible risk themes. Show sample sizes and review source text; do not extrapolate overall brand reputation or causal relationships.
</details>

<details>
<summary><strong>Will deploying the configuration validator generate marketing assets?</strong></summary>

No. The validator only confirms that category configuration is complete and marks evidence gates and human release-review requirements. Text analysis, insight generation, specification checks, visual production, and publication approval must still be implemented and accepted separately.
</details>

## Acceptance Criteria and Boundaries

- Every strategic conclusion cites statistical evidence or is explicitly labeled as a hypothesis to validate.
- Numbers, models, materials, dimensions, performance, and efficacy map back to authoritative specification sources.
- Humans review source authorization, privacy, copyright, advertising rules, and category-specific requirements.
- Mixed-source samples do not represent the whole market, and time-based inference is not presented as strict temporal causality.
- Every new category requires recalibration of sentiment models, dictionaries, dimensions, and thresholds.

---

<p align="right"><a href="#english">Back to English</a></p>

---
