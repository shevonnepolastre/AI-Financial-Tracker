import json
import os

CATEGORIES_FILE = "categories.json"
BUDGETS_FILE = "budgets.json"

# ---------------- Categories ---------------- #
def load_categories():
    if os.path.exists(CATEGORIES_FILE):
        with open(CATEGORIES_FILE, "r") as f:
            return json.load(f)
    return {
        "income_cat": [
            "salary", "bonus", "investment", "rental income", "side hustle", "transfer", "other income"
        ],
        "expense_cat": {
            "house": ["mortgage", "property tax", "repairs"],
            "utilities": ["electric", "water", "gas", "internet", "streaming service", "mobile"],
            "food": ["groceries", "dining out"],
            "auto": ["gas", "maintenance", "insurance"],
            "entertainment": [],
            "health": [],
            "shopping": [],
            "education": [],
            "insurance": [],
            "taxes": [],
            "credit card repayment": [],
            "loan repayment": [],
            "child expenses": ["tuition", "activities", "childcare", "clothing", "health"],
            "personal care": [],
            "vacation": [],
            "savings": [],
            "miscellaneous": []
        }
    }

def save_categories(cats):
    with open(CATEGORIES_FILE, "w") as f:
        json.dump(cats, f, indent=2)

class Categories:
    def __init__(self):
        cats = load_categories()
        self.income_cat = cats["income_cat"]
        self.expense_cat = cats["expense_cat"]
        self.budgets = load_budgets()  # ✅ initialize budgets

    def add_income_category(self, category):
        if category not in self.income_cat:
            self.income_cat.append(category)
            save_categories({"income_cat": self.income_cat, "expense_cat": self.expense_cat})

    def add_expense_category(self, category, subcategory=None):
        if category not in self.expense_cat:
            self.expense_cat[category] = []

        if subcategory and subcategory not in self.expense_cat[category]:
            self.expense_cat[category].append(subcategory)

        save_categories({"income_cat": self.income_cat, "expense_cat": self.expense_cat})

# ---------------- Budgets ---------------- #
def load_budgets():
    if os.path.exists(BUDGETS_FILE):
        with open(BUDGETS_FILE, "r") as f:
            return json.load(f)
    return {}  # start empty if no budgets.json exists

def save_budgets(budgets):
    with open(BUDGETS_FILE, "w") as f:
        json.dump(budgets, f, indent=2)
