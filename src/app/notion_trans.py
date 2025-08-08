from dotenv import load_dotenv
import os
from datetime import date

from budget_categories import Categories
from transactions import Transactions


def main():
    load_dotenv("config/.env")
    categories = Categories()
    transactions = Transactions()

    while True:
        trans_selec = input("Do you want to add income or expense? (or type 'exit' to quit): ").strip().lower()

        if trans_selec == 'exit':
            break

        if trans_selec == 'income':
            inc_cat = input("What is your income category? :").strip().lower()
            if categories.is_income_category(inc_cat):
                result = transactions.add_income(inc_cat)
                if result:
                    add_to_notion(inc_cat, "", result[1], date.today(), entry_type="income")
        
        elif trans_selec == 'expense':
            exp_cat = input("What is your expense category? :").strip().lower()
            subcat = input(f"Enter subcategory for '{exp_cat}' (or press Enter to skip): ").strip().lower()
            if categories.is_expense_category(exp_cat, subcat):
                result = transactions.add_expense(exp_cat)
                if result:
                    add_to_notion(exp_cat, subcat, result[1], date.today(), entry_type="expense")

        else:
            print("Please enter 'income', 'expense', or 'exit'.")


if __name__ == "__main__":
    main()
