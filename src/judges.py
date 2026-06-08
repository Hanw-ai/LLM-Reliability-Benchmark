def rule_based_judge(result):
    if result["correct"] and result["consistent"]:
        return {
            "judge": "rule_based",
            "label": "pass",
            "score": 1.0
        }

    if result["correct"] and not result["consistent"]:
        return {
            "judge": "rule_based",
            "label": "partial",
            "score": 0.6
        }

    return {
        "judge": "rule_based",
        "label": "fail",
        "score": 0.0
    }


def llm_based_judge(result):
    failure_reason = result.get("failure_reason")

    if result["correct"] and result["consistent"]:
        return {
            "judge": "llm_based_simulated",
            "label": "pass",
            "score": 0.9
        }

    if failure_reason in [
        "tool_unavailable",
        "prompt_sensitivity"
    ]:
        return {
            "judge": "llm_based_simulated",
            "label": "partial",
            "score": 0.55
        }

    return {
        "judge": "llm_based_simulated",
        "label": "fail",
        "score": 0.2
    }


def compute_judge_agreement(results):
    if not results:
        return 0

    agreements = 0

    for result in results:
        rule_result = rule_based_judge(result)
        llm_result = llm_based_judge(result)

        if rule_result["label"] == llm_result["label"]:
            agreements += 1

    return agreements / len(results)
