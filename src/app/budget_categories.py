class Categories:
    default_income_cat = [
        "salary", "bonus", "investment", "rental income", "side hustle", "transfer", "other income"
    ]

    default_expense_cat = {
        "house": ["mortgage", "property tax", "repairs"],
        "utilities": ["electric", "water", "gas", "internet", "streaming service", "mobile"],
        "food": ["groceries", "dining out"],
        "auto": ["gas", "maintenance", "insurance"],
        "entertainment": [],
        "health": [],
        "shopping": [],
        "education": [],
        "insurance": [],
        "taxes": [],
        "credit card repayment": [],
        "loan repayment": [],
        "child expenses": ["tuition", "activities", "childcare", "clothing", "health"],
        "personal care": [],
        "vacation": [],
        "savings": [],
        "miscellaneous": []
    }

    def __init__(self, income_cat=None, expense_cat=None):
        self.income_cat = income_cat if income_cat is not None else Categories.default_income_cat.copy()
        self.expense_cat = (
            expense_cat if expense_cat is not None
            else {k: v.copy() for k, v in Categories.default_expense_cat.items()}
        )

    def is_income_category(self, category):
        category = category.lower().strip()
        if category in self.income_cat:
            return True
        add = input(f"'{category}' is not an income category. Add it? (y/n): ").strip().lower()
        if add == 'y':
            self.income_cat.append(category)
            print(f"'{category}' added to income categories.")
            return True
        return False

    def is_expense_category(self, category, subcategory=None):
        category = category.lower().strip()
        if category not in self.expense_cat:
            add = input(f"'{category}' is not an expense category. Add it? (y/n): ").strip().lower()
            if add == 'y':
                self.expense_cat[category] = []
                print(f"'{category}' added to expense categories.")
            else:
                return False

        if subcategory:
            subcategory = subcategory.lower().strip()
            if subcategory not in self.expense_cat[category]:
                add_sub = input(f"'{subcategory}' is not in '{category}'. Add it? (y/n): ").strip().lower()
                if add_sub == 'y':
                    self.expense_cat[category].append(subcategory)
                    print(f"'{subcategory}' added in '{category}'.")
                else:
                    return False
        return True
