def rule_based_judge(result):

    if result["correct"]:
        return 1

    return 0


def llm_based_judge(result):

    if result["correct"]:
        return 0.9

    return 0.3
