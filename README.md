# Advanced Python MVC Project  
## Personal Finance & Budget Tracker (CLI)

A modular, backend-focused **Personal Finance & Budget Tracking System** built in **Python** using the **MVC (Model–View–Controller)** architecture.  
This project helps users track income, expenses, categories, monthly budgets, and financial summaries using a command-line interface with persistent storage.

This is a **portfolio-grade project** designed to demonstrate clean architecture, separation of concerns, commit discipline, and real-world business logic.

---

## 🚀 Features

- Add income transactions
- Add expense transactions
- Update or delete transactions
- Categorize income and expenses
- Set monthly budgets per category
- View transaction history
- Monthly spending summary
- Budget vs actual analysis
- Savings calculation
- Persistent JSON-based storage
- Clean MVC separation
- CLI-driven user interaction

---

## 🏗 Project Architecture (MVC)

```
finance_tracker/
│
├── main.py
│
├── controllers/
│   └── finance_controller.py
│
├── models/
│   ├── transaction.py
│   └── category.py
│
├── services/
│   └── finance_service.py
│
├── repositories/
│   └── finance_repository.py
│
├── views/
│   └── finance_view.py
│
├── utils/
│   ├── date_utils.py
│   ├── validation_utils.py
│   └── calculation_utils.py
│
└── data/
    └── finance_data.json
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher

### Setup

```bash
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
python main.py
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Menu options include:

```
1. Add Income
2. Add Expense
3. View All Transactions
4. Update Transaction
5. Delete Transaction
6. Set Monthly Budget
7. View Monthly Summary
8. Budget vs Actual Report
9. Savings Overview
0. Exit
```

---

## 📊 Example Workflow

- Add salary and side income
- Record daily expenses
- Assign categories (Rent, Food, Travel, Utilities)
- Set monthly budgets
- Review monthly spending
- Track savings and overspending
- Adjust budget based on analytics

---

