from budget_app.budget import Category


class Controller:
    def __init__(self):
        self.categories = {}

    def add_category(self, name: str) -> Category:
        if name not in self.categories:
            category = Category(name)
            self.categories[name] = category
            return category
        else:
            raise ValueError(f"Category {name} already exists")

    def get_category(self, name: str) -> Category:
        if name in self.categories:
            return self.categories[name]
        else:
            raise ValueError(f"Category {name} does not exist")

    def create_spend_chart(self):
        categories = list(self.categories.values())
        spending = []
        for category in categories:
            total_spent = 0
            for entry in category.ledger:
                amount = entry["amount"]
                if amount < 0:
                    total_spent += abs(amount)
            spending.append(total_spent)

        total = sum(spending)
        percentages = [int((sp / total) * 10) * 10 for sp in spending]

        chart = "Percentage spent by category\n"

        for i in range(100, -1, -10):
            chart += f"{i:>3}| "
            for p in percentages:
                if p >= i:
                    chart += "o  "
                else:
                    chart += "   "
            chart += "\n"

        chart += "    -" + "---" * len(categories) + "\n"

        max_len = max(len(c.name) for c in categories)
        for i in range(max_len):
            chart += "     "
            for c in categories:
                if i < len(c.name):
                    chart += c.name[i] + "  "
                else:
                    chart += "   "
            if i < max_len - 1:
                chart += "\n"

        return chart