def generate_report(model_summaries, all_results, output_path):
    report = """# LLM Reliability Benchmark Report

## Model Reliability Leaderboard

| Model | Accuracy | Consistency | Prompt Robustness | Tool Robustness | Context Robustness | Judge Agreement | Reliability Score |
|---|---:|---:|---:|---:|---:|---:|---:|
"""

    sorted_summaries = sorted(
        model_summaries,
        key=lambda x: x["reliability_score"],
        reverse=True
    )

    for summary in sorted_summaries:
        report += (
            f"| {summary['model']} "
            f"| {summary['accuracy']:.2%} "
            f"| {summary['consistency']:.2%} "
            f"| {summary['prompt_robustness']:.2%} "
            f"| {summary['tool_robustness']:.2%} "
            f"| {summary['context_robustness']:.2%} "
            f"| {summary['judge_agreement']:.2%} "
            f"| {summary['reliability_score']:.2f} |\n"
        )

    report += "\n## Failure Breakdown by Model\n\n"

    for summary in sorted_summaries:
        report += f"### {summary['model']}\n\n"

        for failure_reason, count in summary["failure_breakdown"].items():
            report += f"- {failure_reason}: {count}\n"

        report += "\n"

    report += "## Task-Level Results\n\n"

    for result in all_results:
        report += f"### {result['model']} / {result['task_id']}\n\n"
        report += f"- Category: {result['category']}\n"
        report += f"- Correct: {result['correct']}\n"
        report += f"- Consistent: {result['consistent']}\n"
        report += f"- Failure Reason: {result['failure_reason']}\n"
        report += f"- Metadata: {result['metadata']}\n\n"

    report += """## Interpretation

This benchmark compares simulated LLM systems across reliability dimensions:

- Prompt robustness
- Tool robustness
- Context robustness
- Judge agreement
- Overall reliability score

The leaderboard helps compare model behavior under different evaluation stress tests.
"""

    with open(output_path, "w") as file:
        file.write(report)
