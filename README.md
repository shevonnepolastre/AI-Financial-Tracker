# Personal Financial Tracker

#### Video Demo of the MVP: [https://youtu.be/Ba6VCnjLngU](https://youtu.be/Ba6VCnjLngU)

## Description

I started this project as my final project for Harvard CS50 Python. I built the MVP to meet the course requirements: log income and expenses, categorize them, and sync with Notion.

Since then, I've expanded it into a day-to-day financial management tool. My Notion dashboard now connects directly to the tracker, so I don't have to juggle spreadsheets and manually type transactions.

As I went along, I added a Flask web interface for entering data more easily and even uploading CSVs from my bank.

I'm still learning, but it works - and I've got a solid foundation for expanding later, both for personal finance management and for preparing for the Azure AI-102 exam.

## Current Features

* Easily add income and expense transactions.
* Use subcategories to categorize expenses (like house + lawn care).
* Synchronize all transactions to Notion (separate expense and income databases).
* Automatically log transactions from CSV exports from my bank.
* Track your progress against budgets for each category.
* An income and expense dashboard powered by Flask.

## Approach

I broke the project into smaller pieces:

1. **Budget Categories** – A class that stores income and expense categories, plus subcategories. Keeps everything consistent.
2. **Transactions** – Handles adding income and expenses, stores details (amount, category, description, date), and connects to Notion.
3. **Notion Integration** – Used the Notion API to send data into my existing Income and Expense Tracker databases. This was tricky — I had to carefully map fields so everything landed in the right place.
4. **CSV Import** – Added the ability to upload a bank CSV. It reads the “Simple Description” field as the transaction name and uses the correct amount, category, and date.
5. **Web Dashboard** – Built a Flask app with a clean UI where I can add transactions, upload CSVs, and view summaries.

## Project Structure

```
AI-Financial-Tracker/
│
├── run.py                  # Entry point for running the Flask app
│
├── src/
│   └── app/
│       ├── __init__.py      # Flask app factory and route definitions
│       ├── transactions.py  # Handles income and expense logic
│       ├── budget_categories.py  # Defines categories, subcategories, budgets
│       ├── notion_trans.py  # Functions for sending data to Notion
│       ├── templates/
│       │   ├── index.html   # Main dashboard UI
│       │   └── manage.html  # Page for managing categories/budgets
│       └── static/
│           └── css/
│               └── style.css  # Styling for the dashboard
│
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables file
└── README.md               # Project documentation
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shevonnepolastre/AI-Financial-Tracker
cd AI-Financial-Tracker
```

### 2. Create and activate a virtual environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the project root and add the following values:

```
NOTION_API_KEY=your_notion_integration_token
NOTION_INCOME_DB_ID=your_income_database_id
NOTION_EXPENSE_DB_ID=your_expense_database_id
FLASK_ENV=development
```

### 5. Run the app

Using Flask’s built-in server:

```bash
flask --app run.py run
```

For Production, I used Waitress because it's only for my personal use:

```bash
waitress-serve --host=127.0.0.1 --port=8000 run:create_app
```

### 6. Open in browser

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) (or port `8000` if using Waitress).

## Next Steps

* Improve the UI design
* Add more visuals 
* Add credit card payment tracking in a separate Notion table.
* Explore AI mainly to use chatbot 
