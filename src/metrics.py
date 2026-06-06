from collections import Counter


def safe_divide(numerator, denominator):
    return numerator / denominator if denominator else 0


def compute_accuracy(results):
    correct = sum(1 for r in results if r["correct"])
    return safe_divide(correct, len(results))


def compute_category_breakdown(results):
    categories = [r["category"] for r in results]
    return dict(Counter(categories))


def compute_failure_breakdown(results):
    failures = [
        r["failure_reason"]
        for r in results
        if r["failure_reason"] is not None
    ]
    return dict(Counter(failures))


def compute_category_accuracy(results, category):
    category_results = [
        r for r in results
        if r["category"] == category
    ]

    correct = sum(
        1 for r in category_results
        if r["correct"]
    )

    return safe_divide(correct, len(category_results))


def compute_prompt_robustness(results):
    return compute_category_accuracy(
        results,
        "prompt_robustness"
    )


def compute_tool_robustness(results):
    return compute_category_accuracy(
        results,
        "tool_robustness"
    )


def compute_context_robustness(results):
    return compute_category_accuracy(
        results,
        "context_robustness"
    )


def compute_consistency_score(results):
    consistent = sum(
        1 for r in results
        if r["consistent"]
    )

    return safe_divide(consistent, len(results))


def compute_reliability_score(
    accuracy,
    consistency_score,
    prompt_robustness,
    tool_robustness,
    context_robustness
):
    return (
        accuracy * 0.30
        + consistency_score * 0.20
        + prompt_robustness * 0.20
        + tool_robustness * 0.15
        + context_robustness * 0.15
    ) * 100
