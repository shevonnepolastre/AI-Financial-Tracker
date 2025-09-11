import os
from notion_client import Client
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()  

NOTION_TOKEN = os.getenv("NOTION_API_KEY")
INCOME_DB_ID = os.getenv("NOTION_INCOME_DB_ID")
EXPENSE_DB_ID = os.getenv("NOTION_EXPENSE_DB_ID")

notion = Client(auth=NOTION_TOKEN)

def create_income_page(category, amount, date_added, description="Income"):
    payload = {
        "parent": {"database_id": INCOME_DB_ID},
        "properties": {
            "Income Name": {
                "title": [
                    {"text": {"content": description or category.title()}}
                ]
            },
            "Category": {
                "select": {"name": category.title()}
            },
            "Amount": {
                "number": float(amount)
            },
            "Date Received": {
                "date": {"start": date_added.strftime("%Y-%m-%d")}
            }
        }
    }

    try:
        return notion.pages.create(**payload)
    except Exception as e:
        print(f"[ERROR] Failed to log income to Notion: {e}")
        return None

def create_expense_page(category, subcategory, amount, date_added, description="Expense"):
    payload = {
        "parent": {"database_id": EXPENSE_DB_ID},
        "properties": {
            "Expense": {
                "title": [
                    {"text": {"content": description or category.title()}}
                ]
            },
            "Category": {
                "select": {"name": category.title()}
            },
            "Subcategory": {
                "select": {"name": subcategory.title()} if subcategory else None
            },
            "Actual": {
                "number": float(amount)
            },
            "Date": {
                "date": {"start": date_added.strftime("%Y-%m-%d")}
            }
        }
    }

    # Remove empty properties (e.g. no subcategory)
    payload["properties"] = {k: v for k, v in payload["properties"].items() if v is not None}

    try:
        return notion.pages.create(**payload)
    except Exception as e:
        print(f"[ERROR] Failed to log expense to Notion: {e}")
        return None
