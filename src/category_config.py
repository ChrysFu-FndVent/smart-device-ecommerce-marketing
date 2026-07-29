"""Validate a cross-category marketing configuration before analysis."""

from __future__ import annotations

import argparse
import json
from typing import Any


REQUIRED_LISTS = (
    "sources",
    "analysis_dimensions",
    "spec_source",
    "risk_rules",
    "required_output",
)


class ConfigError(ValueError):
    pass


def validate_config(raw: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    for key in ("category", "business_question", "target_channel"):
        value = raw.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ConfigError(f"{key} must be a non-empty string")
        normalized[key] = value.strip()

    for key in REQUIRED_LISTS:
        value = raw.get(key)
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
            raise ConfigError(f"{key} must be a non-empty string list")
        normalized[key] = list(dict.fromkeys(item.strip() for item in value))

    normalized["evidence_gate_required"] = True
    normalized["human_release_review_required"] = True
    return normalized


DEMO_CONFIG = {
    "category": "扫地机器人",
    "business_question": "哪些问题应进入详情页首屏与负面风险检查",
    "sources": ["公开评论", "商品问答", "测评", "产品页"],
    "analysis_dimensions": ["清洁力", "避障", "噪音", "维护", "连接", "售后"],
    "spec_source": ["正式规格表", "说明书", "检测或授权资料"],
    "risk_rules": ["性能条件", "认证表述", "禁止虚构配件与功能"],
    "target_channel": "电商详情页",
    "required_output": ["数据观察", "待验证假设", "卖点层级", "元素溯源表"],
}


def run_self_test() -> None:
    result = validate_config(DEMO_CONFIG)
    assert result["evidence_gate_required"] is True
    try:
        validate_config({**DEMO_CONFIG, "spec_source": []})
    except ConfigError:
        return
    raise AssertionError("empty spec_source was accepted")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        run_self_test()
        print("self-test: ok")
        return
    print(json.dumps(validate_config(DEMO_CONFIG), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
