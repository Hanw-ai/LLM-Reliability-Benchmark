def evaluate_consistency(results):

    consistent = sum(
        1
        for r in results
        if r["consistent"]
    )

    return consistent / len(results)
