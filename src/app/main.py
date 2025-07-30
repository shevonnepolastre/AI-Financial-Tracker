import pandas as pd
import numpy as np
from flask import Flask
import plaid
from plaid.api import plaid_api
import os
from dotenv import load_dotenv

from src.app.budget_categories import Categories

# Load environment variables from .env file
load_dotenv()

# Access the variables
client_id = os.getenv("PLAID_CLIENT_ID") 
secret = os.getenv("PLAID_SECRET")

# Available environments are
# 'Production'
# 'Sandbox'

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

app = Flask(__name__)
@app.route("/")

# user input for income or expense
def main():
    cat = Categories()
    while True:
        finance_item = input("Is it an income or expense? ").strip().lower()
        if finance_item == "income":
            income(cat)
        elif finance_item == "expense":
            expense(cat)
        else:
            ValueError("This is not a valid input. Please enter an income or expense.")
            continue 

# Function to handle income input
def income(cat):
    income = float(input("How much did you make? "))
    income_source = input("What is the source of your income? ")
    if income_source in cat.income_categories:
        income_categories[income_source] += income
    else:
        print("This income source is not recognized. Please add it to your budget categories.")
    print(f"Your total income from {income_source} is now {cat.income_categories[income_source]}.")
    return cat.income_categories

def expense(categories):
    expense = float(input("How much did you spend? "))
    expense_category = input("What is the category of your expense? ")
    if expense_category in categories:
        categories[expense_category] -= expense
    else:
        print("This expense category is not recognized. Please add it to your budget categories.")
    print(f"Your total expenses in {expense_category} is now {categories[expense_category]}.")
    return categories

if __name__ == "__main__":
    main()