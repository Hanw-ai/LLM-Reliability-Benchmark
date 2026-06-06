def generate_report(metrics, results, output_path):
    report = f"""# LLM Reliability Benchmark Report

## Summary

| Metric | Value |
|---|---:|
| Accuracy | {metrics["accuracy"]:.2%} |
| Consistency | {metrics["consistency"]:.2%} |
| Prompt Robustness | {metrics["prompt_robustness"]:.2%} |
| Tool Robustness | {metrics["tool_robustness"]:.2%} |
| Context Robustness | {metrics["context_robustness"]:.2%} |
| Reliability Score | {metrics["reliability_score"]:.2f} |

## Failure Breakdown

"""

    for failure_reason, count in metrics["failure_breakdown"].items():
        report += f"- {failure_reason}: {count}\n"

    report += "\n## Task-Level Results\n\n"

    for result in results:
        report += f"### {result['task_id']}\n\n"
        report += f"- Category: {result['category']}\n"
        report += f"- Correct: {result['correct']}\n"
        report += f"- Consistent: {result['consistent']}\n"
        report += f"- Failure Reason: {result['failure_reason']}\n"
        report += f"- Metadata: {result['metadata']}\n\n"

    report += """## Interpretation

This benchmark evaluates LLM reliability across three robustness dimensions:

- Prompt robustness: stability under prompt variation
- Tool robustness: behavior under tool failure or wrong-tool conditions
- Context robustness: degradation under long-context settings

The reliability score combines accuracy, consistency, and robustness-specific metrics.
"""

    with open(output_path, "w") as file:
        file.write(report)
