from collections import Counter


def compute_accuracy(results):
    correct = sum(1 for r in results if r["correct"])
    return correct / len(results)


def compute_category_breakdown(results):
    categories = [r["category"] for r in results]
    return dict(Counter(categories))


def compute_reliability_score(
    accuracy,
    consistency_score
):
    return (
        accuracy * 0.7 +
        consistency_score * 0.3
    ) * 100
