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
