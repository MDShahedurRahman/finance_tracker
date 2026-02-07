from models.transaction import Transaction
from services.transaction_service import TransactionService
from services.analytics_service import AnalyticsService
from views.finance_view import FinanceView


class FinanceController:

    def __init__(self):
        self.view = FinanceView()
        self.txn_service = TransactionService()
        self.analytics = AnalyticsService()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_choice()

            if choice == "1":
                self.add_transaction_flow()
            elif choice == "2":
                self.view_transactions_flow()
            elif choice == "3":
                self.delete_transaction_flow()
            elif choice == "4":
                self.monthly_summary_flow()
            elif choice == "0":
                print("Goodbye!")
                break
