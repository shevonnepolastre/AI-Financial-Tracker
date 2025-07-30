class Categories:
    def __init__(self):
        self.income_categories = ["salary", "bonus", "investment", "rental income", "side hustle", "transfer", "other income"]
        self.expense_categories = {
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

    def is_income_category(self, category):
        if category.lower() in self.income_categories:
            return True
        else:
            add = input(f"'{category}' is not an income category. Add it? (y/n): ").strip().lower()
            if add == 'y':
                self.income_categories.append(category.lower())
                print(f"'{category}' added to income categories.")
                return True
            return False

    def is_expense_category(self, category, subcategory=None):
        category = category.lower()
        if category not in self.expense_categories:
            add = input(f"'{category}' is not an expense category. Add it? (y/n): ").strip().lower()
            if add == 'y':
                self.expense_categories[category] = []
                print(f"'{category}' added to expense categories.")
            else:
                return False

        if subcategory:
            subcategory = subcategory.lower()
            if subcategory not in self.expense_categories[category]:
                add_sub = input(f"'{subcategory}' is not in '{category}'. Add it? (y/n): ").strip().lower()
                if add_sub == 'y':
                    self.expense_categories[category].append(subcategory)
                    print(f"'{subcategory}' added in '{category}'.")
                else:
                    return False
        return True
