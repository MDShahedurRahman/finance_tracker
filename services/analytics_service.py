class AnalyticsService:

    def monthly_summary(self, transactions):
        summary = {"income": 0, "expense": 0}

        for t in transactions:
            if t.txn_type == "income":
                summary["income"] += t.amount
            else:
                summary["expense"] += t.amount

        summary["balance"] = summary["income"] - summary["expense"]
        return summary
