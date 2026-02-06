class FinanceView:

    def show_menu(self):
        print("\n=== Finance Tracker Pro ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Monthly Summary")
        print("0. Exit")

    def get_choice(self):
        return input("Enter choice: ")

    def get_transaction_input(self):
        txn_type = input("Type (income/expense): ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        date = input("Date (YYYY-MM-DD): ")
        return txn_type, category, amount, date

    def display_transactions(self, txns):
        for t in txns:
            print(
                f"{t.txn_id} | {t.txn_type} | {t.category} | ${t.amount} | {t.date}")

    def display_summary(self, summary):
        print("\n--- Monthly Summary ---")
        print("Income:", summary["income"])
        print("Expense:", summary["expense"])
        print("Balance:", summary["balance"])
