class Category:

    def __init__(self, name: str):
        self.name = name
        self.ledger = []
        self.budget = 0

    def check_funds(self, amount: float) -> bool:
        return self.budget >= amount

    def deposit(self, amount: float, description: str ="") -> None:
        self.ledger.append({"amount": amount, "description": description})
        self.budget += amount


    def withdraw(self, amount: float, description: str ="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.budget -= amount
            return True
        return False


    def get_balance(self) -> float:
        return self.budget

    def transfer(self, amount: float, category:"Category") -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:>7.2f}"
            items += f"{description:<23}{amount}\n"
        total= f"Total: {self.budget:.2f}"
        return title + items + total




def create_spend_chart(categories):
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
            if i<len(c.name):
                chart += c.name[i] + "  "
            else:
                chart += "   "
        if i < max_len -1:
            chart += "\n"

    return chart



