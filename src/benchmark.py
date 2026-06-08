import json


class ReliabilityBenchmark:
    def __init__(self, data_path, model_name="gpt-4.1"):
        self.data_path = data_path
        self.model_name = model_name

    def load_tasks(self):
        with open(self.data_path, "r") as file:
            return json.load(file)

    def simulate_task_result(self, task):
        category = task["category"]

        if category == "prompt_robustness":
            return self.simulate_prompt_robustness(task)

        if category == "tool_robustness":
            return self.simulate_tool_robustness(task)

        if category == "context_robustness":
            return self.simulate_context_robustness(task)

        return {
            "correct": False,
            "consistent": False,
            "failure_reason": "unknown_category"
        }

    def simulate_prompt_robustness(self, task):
        variant = task.get("variant", "original")

        if variant == "original":
            return {
                "correct": True,
                "consistent": True,
                "failure_reason": None
            }

        if variant == "rephrased":
            return {
                "correct": True,
                "consistent": True,
                "failure_reason": None
            }

        if variant == "noisy":
            return {
                "correct": False,
                "consistent": False,
                "failure_reason": "prompt_sensitivity"
            }

        return {
            "correct": False,
            "consistent": False,
            "failure_reason": "prompt_unknown"
        }

    def simulate_tool_robustness(self, task):
        tool_available = task.get("tool_available")

        if tool_available is True:
            return {
                "correct": True,
                "consistent": True,
                "failure_reason": None
            }

        if tool_available is False:
            return {
                "correct": True,
                "consistent": False,
                "failure_reason": "tool_unavailable"
            }

        if tool_available == "wrong_tool":
            return {
                "correct": False,
                "consistent": False,
                "failure_reason": "wrong_tool"
            }

        return {
            "correct": False,
            "consistent": False,
            "failure_reason": "tool_unknown"
        }

    def simulate_context_robustness(self, task):
        context_length = task.get("context_length", 0)

        if self.model_name == "gpt-4.1" and context_length <= 50000:
            return {
                "correct": True,
                "consistent": True,
                "failure_reason": None
           }

        if self.model_name == "claude-3.5" and context_length <= 10000:
            return {
                "correct": True,
                "consistent": True,
                "failure_reason": None
            }
            

        return {
            "correct": False,
            "consistent": False,
            "failure_reason": "long_context_degradation"
        }

    def run(self):
        tasks = self.load_tasks()
        results = []

        for task in tasks:
            simulated_result = self.simulate_task_result(task)

            results.append(
                {
                    "model": self.model_name,
                    "task_id": task["task_id"],
                    "category": task["category"],
                    "correct": simulated_result["correct"],
                    "consistent": simulated_result["consistent"],
                    "failure_reason": simulated_result["failure_reason"],
                    "metadata": {
                        "variant": task.get("variant"),
                        "tool_available": task.get("tool_available"),
                        "context_length": task.get("context_length")
                    }
                }
            )

        return results
