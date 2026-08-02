<a id="readme-top"></a>
<div align="right"><a href="#简体中文">简体中文</a> | <a href="#english">English</a></div>

<div align="center">
<h1>Smart Device Ecommerce Marketing</h1>
<p><em>Cross-category e-commerce marketing workflow documentation with configuration validation.</em></p>
<img alt="Python" src="https://img.shields.io/badge/Reference-Python%20standard%20library-3776AB?style=flat-square&logo=python&logoColor=white">
<img alt="Workflow" src="https://img.shields.io/badge/Workflow-Data%20to%20marketing%20materials-0F766E?style=flat-square">
<img alt="Review" src="https://img.shields.io/badge/Release-Human%20review%20required-F59E0B?style=flat-square">
</div>

<a id="简体中文"></a>

## 概览

本仓库记录跨品类商品数据营销的流程、能力契约、Prompt、产品设计与分析材料。`src/category_config.py` 在分析前校验品类配置是否包含来源、分析维度、规格来源、风险规则和所需输出；它不采集数据、不生成营销素材，也不执行发布。

## 仓库内容

| 内容 | 已有文件 |
|---|---|
| 品类配置与六段数据营销流程 | [workflows.md](workflows.md) |
| 采集、分析、主题与物料 Skill 契约 | [skills.md](skills.md) |
| 可验证的分析、文案与视觉 Prompt | [prompt-engineering.md](prompt-engineering.md) |
| 品类营销架构与智能手环案例分析 | [product-design.md](product-design.md) · [data-analysis.md](data-analysis.md) |
| 配置校验参考 | [src/category_config.py](src/category_config.py) |

## 运行配置校验器

```bash
python3 src/category_config.py --self-test
python3 src/category_config.py
```

校验器要求 `category`、`business_question` 和 `target_channel`，以及非空的 `sources`、`analysis_dimensions`、`spec_source`、`risk_rules` 与 `required_output` 列表。成功结果仍标记证据闸门和人工发布审核为必需。

## 使用边界

- 结论、卖点和视觉素材应回溯到已核验的商品数据与规格来源。
- 示例配置不是对特定商品功能、健康效果或商业结果的承诺。
- 分析、素材生成和发布由独立系统及人工审核流程完成。

<a id="english"></a>

## Overview

This repository contains workflow, capability-contract, prompt, product-design, and analysis material for cross-category e-commerce data marketing. `src/category_config.py` validates that a category configuration contains sources, analysis dimensions, specification sources, risk rules, and required outputs before analysis. It does not collect data, generate marketing assets, or publish content.

## Contents

| Content | Existing file |
|---|---|
| Category configuration and six-stage data-marketing flow | [workflows.md](workflows.md) |
| Collection, analysis, theme, and material Skill contracts | [skills.md](skills.md) |
| Verifiable analysis, copy, and visual prompts | [prompt-engineering.md](prompt-engineering.md) |
| Category-marketing architecture and smart-band case material | [product-design.md](product-design.md) · [data-analysis.md](data-analysis.md) |
| Configuration-validation reference | [src/category_config.py](src/category_config.py) |

## Run the Configuration Validator

```bash
python3 src/category_config.py --self-test
python3 src/category_config.py
```

The validator requires `category`, `business_question`, and `target_channel`, plus non-empty `sources`, `analysis_dimensions`, `spec_source`, `risk_rules`, and `required_output` lists. A successful result still marks an evidence gate and human release review as required.

## Scope

- Trace conclusions, selling points, and visual material back to verified product data and specification sources.
- The example configuration does not promise a product capability, health effect, or commercial result.
- Independent systems and human review complete analysis, material generation, and release.
