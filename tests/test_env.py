import os
from dotenv import load_dotenv

load_dotenv()
print("NOTION_API_KEY:", os.getenv("NOTION_API_KEY"))
print("NOTION_INCOME_DB_ID:", os.getenv("NOTION_INCOME_DB_ID"))
print("NOTION_EXPENSE_DB_ID:", os.getenv("NOTION_EXPENSE_DB_ID"))
print("NOTION_PAGE_ID:", os.getenv("NOTION_PAGE_ID"))
print("PLAID_CLIENT_ID:", os.getenv("PLAID_CLIENT_ID"))
print("PLAID_SECRET:", os.getenv("PLAID_SECRET"))
print("PLAID_ENV:", os.getenv("PLAID_ENV"))