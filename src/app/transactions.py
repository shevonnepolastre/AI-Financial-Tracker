from budget_categories import Categories

from collections import defaultdict

class Transactions:
    def __init__(self):
        self.store_income = defaultdict(float)
        self.store_expense = defaultdict(float)

    def add_income(self, category):
        add_inc = input(f"What is the amount for '{category}'? :").strip()
        try:
            amount = float(add_inc)
            self.store_income[category] += amount
            print(f"Added {amount} to '{category}'. Total now: {self.store_income[category]}")
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return False
        return (category, amount)

    def add_expense(self, category):
        add_exp = input(f"What is the amount for '{category}'? :").strip()
        try:
            amount = float(add_exp)
            self.store_expense[category] += amount
            print(f"Added {amount} to '{category}'. Total now: {self.store_expense[category]}")
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return False
        return (category, amount)
