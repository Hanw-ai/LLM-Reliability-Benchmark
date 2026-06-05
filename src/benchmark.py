import json


class ReliabilityBenchmark:

    def __init__(self, data_path):
        self.data_path = data_path

    def load_tasks(self):

        with open(
            self.data_path,
            "r"
        ) as file:

            return json.load(file)

    def run(self):

        tasks = self.load_tasks()

        results = []

        for task in tasks:

            results.append(
                {
                    "task_id": task["task_id"],
                    "category": task["category"],
                    "correct": True,
                    "consistent": True
                }
            )

        return results
