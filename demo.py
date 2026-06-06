from src.benchmark import ReliabilityBenchmark
from src.metrics import (
    compute_accuracy,
    compute_consistency_score,
    compute_failure_breakdown,
    compute_prompt_robustness,
    compute_tool_robustness,
    compute_context_robustness,
    compute_reliability_score,
)
from src.report import generate_report


def main():
    benchmark = ReliabilityBenchmark(
        "data/benchmark_tasks.json"
    )

    results = benchmark.run()

    accuracy = compute_accuracy(results)
    consistency = compute_consistency_score(results)
    prompt_robustness = compute_prompt_robustness(results)
    tool_robustness = compute_tool_robustness(results)
    context_robustness = compute_context_robustness(results)

    reliability_score = compute_reliability_score(
        accuracy,
        consistency,
        prompt_robustness,
        tool_robustness,
        context_robustness,
    )

    metrics = {
        "accuracy": accuracy,
        "consistency": consistency,
        "prompt_robustness": prompt_robustness,
        "tool_robustness": tool_robustness,
        "context_robustness": context_robustness,
        "reliability_score": reliability_score,
        "failure_breakdown": compute_failure_breakdown(results),
    }

    generate_report(
        metrics,
        results,
        "reports/reliability_report.md"
    )

    print("LLM Reliability Benchmark Results")
    print(metrics)
    print("Report generated: reports/reliability_report.md")


if __name__ == "__main__":
    main()
