import json
import os
from models.budget import Budget


class BudgetRepository:
    def __init__(self, file_path="data/budgets.json"):
        self.file_path = file_path

    def load_all(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            data = json.load(f)
            return [Budget.from_dict(x) for x in data]

    def save_all(self, budgets):
        with open(self.file_path, "w") as f:
            json.dump([b.to_dict() for b in budgets], f, indent=4)
