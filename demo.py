from src.benchmark import ReliabilityBenchmark
from src.metrics import compute_model_summary
from src.judges import compute_judge_agreement
from src.report import generate_report


def main():
    models = [
        "gpt-4.1",
        "claude-3.5",
        "gemini-1.5"
    ]

    all_model_summaries = []
    all_results = []

    for model_name in models:
        benchmark = ReliabilityBenchmark(
            "data/benchmark_tasks.json",
            model_name=model_name
        )

        results = benchmark.run()

        model_summary = compute_model_summary(
            model_name,
            results
        )

        model_summary["judge_agreement"] = compute_judge_agreement(
            results
        )

        all_model_summaries.append(model_summary)
        all_results.extend(results)

    generate_report(
        all_model_summaries,
        all_results,
        "reports/reliability_report.md"
    )

    print("LLM Reliability Leaderboard")
    for summary in all_model_summaries:
        print(summary)

    print("Report generated: reports/reliability_report.md")


if __name__ == "__main__":
    main()
