from datetime import datetime


class Transaction:
    def __init__(self, txn_id, txn_type, category, amount, date):
        self.txn_id = txn_id
        self.txn_type = txn_type
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "txn_id": self.txn_id,
            "txn_type": self.txn_type,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }
