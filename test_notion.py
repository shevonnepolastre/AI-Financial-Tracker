from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()
print("NOTION_API_KEY:", os.getenv("NOTION_API_KEY"))
notion = Client(auth=os.getenv("NOTION_API_KEY"))
try:
    print("Notion API Test:", notion.users.list())  # Should return a list of users if the token is valid
except Exception as e:
    print("Error:", e)
