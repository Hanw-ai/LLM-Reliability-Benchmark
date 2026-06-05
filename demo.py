from src.benchmark import ReliabilityBenchmark
from src.metrics import (
    compute_accuracy,
    compute_reliability_score
)
from src.reliability import (
    evaluate_consistency
)
from src.report import generate_report


benchmark = ReliabilityBenchmark(
    "data/benchmark_tasks.json"
)

results = benchmark.run()

accuracy = compute_accuracy(results)

consistency = evaluate_consistency(
    results
)

reliability_score = (
    compute_reliability_score(
        accuracy,
        consistency
    )
)

metrics = {
    "accuracy": accuracy,
    "consistency": consistency,
    "reliability_score":
        reliability_score
}

generate_report(
    metrics,
    "reports/reliability_report.md"
)

print(metrics)
