import json
import os
from models.transaction import Transaction


class TransactionRepository:
    def __init__(self, file_path="data/transactions.json"):
        self.file_path = file_path
