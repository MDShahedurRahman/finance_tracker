from repositories.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self):
        self.repo = TransactionRepository()

    def add_transaction(self, txn):
        txns = self.repo.load_all()
        txns.append(txn)
        self.repo.save_all(txns)
