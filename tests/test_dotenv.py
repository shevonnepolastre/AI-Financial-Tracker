from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("PLAID_CLIENT_ID"))
print(os.getenv("NOTION_TOKEN"))
