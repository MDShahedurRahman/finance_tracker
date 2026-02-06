import json
import os
from models.budget import Budget


class BudgetRepository:
    def __init__(self, file_path="data/budgets.json"):
        self.file_path = file_path
