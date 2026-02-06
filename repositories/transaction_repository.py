import json
import os
from models.transaction import Transaction


class TransactionRepository:
    def __init__(self, file_path="data/transactions.json"):
        self.file_path = file_path

    def load_all(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            data = json.load(f)
            return [Transaction.from_dict(x) for x in data]

    def save_all(self, transactions):
        with open(self.file_path, "w") as f:
            json.dump([t.to_dict() for t in transactions], f, indent=4)
