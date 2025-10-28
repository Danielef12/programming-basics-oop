from source.controller import Controller
from source.menu import PrintMenu

class AppFunction:
    def __init__(self):
        self.controller = Controller()
        self.menu = PrintMenu

    def menu_selection(self):
        while True:
            self.menu.print_menu()
            selection = int(input("Select an option: "))
            match selection:
                case 1:
                    self.create_category()
                case 2:
                    self.add_funds()
                case 3:
                    self.get_withdraw()
                case 4:
                    self.transfer()
                case 5:
                    self.show_category_detail()
                case 6:
                    self.show_graphic_spent()
                case 7:
                    print("Thank you for using this program")
                    break
                case _:
                    print("Invalid selection")

    def create_category(self):
        name = input("Enter category name: ")
        try:
            self.controller.add_category(name)
        except ValueError as e:
            print(f"Error: {e}")

    def add_funds(self):
        name_category = self.controller.get_category(input("Enter category name: "))
        amount = int(input("Enter amount of funds: "))
        if amount < 0:
            print("Amount must be positive")
        description = input("Enter description of funds: ")
        try:
            name_category.deposit(amount, description)
            print(f"Deposited: {amount}, Description: {description}")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def get_withdraw(self):
        name_category = self.controller.get_category(input("Enter category name: "))
        amount = int(input("Enter amount of withdrawals: "))
        description = input("Enter description of withdrawals: ")
        try:
            name_category.withdraw(amount, description)
            print(f"Withdrawal: {amount}, Description: {description}")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def transfer(self):
        try:
            from_category = self.controller.get_category(input("Enter category name: "))
            to_category = self.controller.get_category(input("Enter category name: "))
            amount = int(input("Enter amount of transfers: "))
            if from_category.transfer(amount, to_category):
                print(f"Transferred: {amount} from {from_category.name} to {to_category.name}")
            else:
                print("Not enough funds to transfer!")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def show_category_detail(self):
        category_name = self.controller.get_category(input("Enter category name: "))
        if category_name:
            print(category_name)
        else:
            print("Not found")

    def show_graphic_spent(self):
        print(self.controller.create_spend_chart())

