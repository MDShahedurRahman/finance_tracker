from models.transaction import Transaction
from services.transaction_service import TransactionService
from services.analytics_service import AnalyticsService
from views.finance_view import FinanceView


class FinanceController:

    def __init__(self):
        self.view = FinanceView()
        self.txn_service = TransactionService()
        self.analytics = AnalyticsService()
