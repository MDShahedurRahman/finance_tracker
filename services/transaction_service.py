from repositories.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self):
        self.repo = TransactionRepository()
