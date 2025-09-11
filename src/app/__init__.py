import csv, io
from flask import Flask, render_template, request, redirect, url_for, flash
from .transactions import Transactions
from .budget_categories import Categories, save_budgets

def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret"

    # global objects
    tx = Transactions()
    cats = Categories()

    # ---------------- Dashboard ---------------- #
    @app.route("/")
    def dashboard():
        expense_summary = tx.summary_expense()
        income_summary = tx.summary_income()
        return render_template(
            "index.html",
            expense_summary=expense_summary,
            income_summary=income_summary,
            income_categories=cats.income_cat,
            expense_categories=cats.expense_cat
        )

    # ---------------- Add Expense ---------------- #
    @app.route("/add_expense", methods=["POST"])
    def add_expense():
        category = request.form.get("category")
        subcategory = request.form.get("subcategory")
        amount = request.form.get("amount")
        tx.add_expense(category, amount, subcategory=subcategory, description=subcategory or category)
        flash(f"Added expense: {subcategory or category} - ${amount}")
        return redirect(url_for("dashboard"))

    # ---------------- Add Income ---------------- #
    @app.route("/add_income", methods=["POST"])
    def add_income():
        category = request.form.get("category")
        amount = request.form.get("amount")
        tx.add_income(category, amount, description=category)
        flash(f"Added income: {category} - ${amount}")
        return redirect(url_for("dashboard"))

    # ---------------- Upload CSV ---------------- #
    @app.route("/upload_csv", methods=["POST"])
    def upload_csv():
        if "file" not in request.files:
            flash("No file uploaded.")
            return redirect(url_for("dashboard"))

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected.")
            return redirect(url_for("dashboard"))

        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.DictReader(stream)

        for row in csv_input:
            try:
                amount = float(row.get("Amount", "0").replace(",", "").strip())
                category = row.get("Category", "").strip()
                description = row.get("Simple Description", "").strip()
                date_str = row.get("Date", "").strip()

                if amount > 0:
                    tx.add_income(category, amount, description=description, date=date_str)
                else:
                    tx.add_expense(category, abs(amount), description=description, date=date_str)
            except Exception as e:
                print("[ERROR] Failed to parse row:", row, "Error:", e)

        flash("Bank CSV uploaded successfully!")
        return redirect(url_for("dashboard"))

    # ---------------- Update Budget ---------------- #
    @app.route("/update_budget", methods=["POST"])
    def update_budget():
        category = request.form.get("category")
        amount = request.form.get("amount")
        try:
            amount = float(amount)
            cats.budgets[category] = amount
            save_budgets(cats.budgets)
            flash(f"Updated budget for {category.title()} to ${amount}")
        except ValueError:
            flash("Invalid budget amount")
        return redirect(url_for("manage"))

    # ---------------- Add Category ---------------- #
    @app.route("/add_category", methods=["POST"])
    def add_category():
        cat_type = request.form.get("type")
        category = request.form.get("category")
        subcategory = request.form.get("subcategory")

        if cat_type == "income":
            if category not in cats.income_cat:
                cats.income_cat.append(category)
                flash(f"Added new income category: {category}")
        elif cat_type == "expense":
            if category not in cats.expense_cat:
                cats.expense_cat[category] = []
                flash(f"Added new expense category: {category}")
            if subcategory:
                cats.expense_cat[category].append(subcategory)
                flash(f"Added subcategory {subcategory} under {category}")

        return redirect(url_for("manage"))

    # ---------------- Manage Page ---------------- #
    @app.route("/manage")
    def manage():
        return render_template(
            "manage.html",
            income_categories=cats.income_cat,
            expense_categories=cats.expense_cat
        )

    return app
