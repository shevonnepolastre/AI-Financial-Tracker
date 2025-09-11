from budget_categories import Categories
from transactions import Transactions
# from webpage import app

from datetime import date
from dotenv import load_dotenv

from notion_trans import create_income_page, create_expense_page


load_dotenv()

def main():
    categories = Categories()
    transactions = Transactions()

    while True:
        action = input("Do you want to add income or expense? (type 'exit' to stop): ").strip().lower()

        if action == 'income':
            cat = input("Enter income category: ").strip().lower()
            if categories.is_income_category(cat):
                result = transactions.add_income(cat)
                if result:
                    print("Logging to Notion...")
                    create_income_page(cat, "", result[1], date.today(), entry_type="income")

        elif action == 'expense':
            cat = input("Enter expense category: ").strip().lower()
            sub = input("Enter subcategory (or press Enter to skip): ").strip().lower()
            if categories.is_expense_category(cat, sub):
                result = transactions.add_expense(cat)
                if result:
                    print("Logging to Notion...")
                    create_expense_page(cat, sub, result[1], date.today(), entry_type="expense")

        elif action == "exit":
            break

        else:
            print("Not an option. Try again.")
            continue

    print("Current transactions:")
    print("Income:", transactions.income)
    print("Expenses:", transactions.expenses)

if __name__ == "__main__":
    main()
