# LLM-Reliability-Benchmark
A benchmark framework for evaluating reliability, robustness, and consistency of LLM systems.

## V2: Robustness Evaluation

This benchmark evaluates three reliability dimensions:

| Dimension | Description |
|---|---|
| Prompt Robustness | Measures whether model outputs remain stable across prompt variants |
| Tool Robustness | Measures whether the system handles missing or incorrect tools |
| Context Robustness | Measures whether performance degrades under longer contexts |

## Metrics

| Metric | Description |
|---|---|
| Accuracy | Overall correctness across benchmark tasks |
| Consistency | Whether results remain stable across conditions |
| Prompt Robustness | Accuracy under prompt variation |
| Tool Robustness | Accuracy under tool failures |
| Context Robustness | Accuracy under long-context conditions |
| Reliability Score | Weighted score combining accuracy, consistency, and robustness |
