def generate_report(
    metrics,
    output_path
):

    report = f"""
# LLM Reliability Report

## Summary

Accuracy:
{metrics["accuracy"]:.2%}

Consistency:
{metrics["consistency"]:.2%}

Reliability Score:
{metrics["reliability_score"]:.2f}
"""

    with open(
        output_path,
        "w"
    ) as file:

        file.write(report)
