from .budget_categories import Categories
from .notion_trans import create_income_page, create_expense_page
from datetime import datetime

class Transactions:
    def __init__(self):
        self.income = []     # list of income entries
        self.expenses = []   # list of expense entries
        self.budgets = Categories().budgets

    # ---------------- Income ---------------- #
    def add_income(self, category, amount, description="Income", date=None):
        try:
            amount = float(amount)
            entry_date = (
                datetime.strptime(date, "%m/%d/%Y") if date else datetime.now()
            )
            entry = {
                "category": category,
                "subcategory": None,
                "description": description,
                "amount": amount,
                "date": entry_date
            }
            self.income.append(entry)

            # ✅ Push to Notion with correct date
            create_income_page(category, amount, entry["date"], description)
            return True, f"Added {amount} income: {description}"
        except ValueError:
            return False, "Invalid amount."

    def summary_income(self):
        """Return a summary of all income transactions"""
        summary = []
        for entry in self.income:
            summary.append({
                "category": entry["category"],
                "description": entry["description"],
                "amount": entry["amount"],
                "date": entry["date"].strftime("%Y-%m-%d")
            })
        return summary

    # ---------------- Expenses ---------------- #
    def add_expense(self, category, amount, subcategory=None, description="Expense", date=None):
        try:
            amount = float(amount)
            entry_date = (
                datetime.strptime(date, "%m/%d/%Y") if date else datetime.now()
            )
            entry = {
                "category": category,
                "subcategory": subcategory,
                "description": description,
                "amount": amount,
                "date": entry_date
            }
            self.expenses.append(entry)

            # ✅ Push to Notion with correct date
            create_expense_page(category, subcategory or "Uncategorized", amount, entry["date"], description)
            return True, f"Added {amount} expense: {description}"
        except ValueError:
            return False, "Invalid amount."

    def summary_expense(self):
        """Return a summary of all expense transactions with budget checks"""
        summary = []
        for entry in self.expenses:
            category = entry["category"]
            subcategory = entry["subcategory"]
            spent = entry["amount"]
            budget = self.budgets.get(subcategory or category, 0)
            status = "Over Budget" if spent > budget else "OK"
            summary.append({
                "category": category,
                "subcategory": subcategory,
                "description": entry["description"],
                "spent": spent,
                "budget": budget,
                "status": status,
                "date": entry["date"].strftime("%Y-%m-%d")
            })
        return summary
