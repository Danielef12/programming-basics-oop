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







