from budget_app.controller import Controller
from budget_app.menu import PrintMenu

class AppFunction:
    def __init__(self):
        self.controller = Controller()
        self.menu = PrintMenu

    def menu_selection(self):
        while True:
            self.menu.print_menu()
            try:
                if (selection := int(input("Select an option: "))) not in [1,2,3,4,5,6,7]:
                    print("Invalid selection. Try again.")
                    continue

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

            except ValueError:
                print("Invalid selection. Try again.")

    def create_category(self):
        name = input("Enter category name: ")
        try:
            self.controller.add_category(name)
            print("Successfully added category '{}'".format(name))
            while (response := input("Category have budget 0, want to add funds?(y,n): ").lower()) not in ["n","no"]:
                if response in ["y", "yes"]:
                    category = self.controller.get_category(name)
                    self.add_funds(category, "Initial deposit")
                    break
                else:
                    print("Invalid input. Try again.")
        except ValueError as e:
            print(f"Error: {e}")

    def add_funds(self, name_category=None, description=None):
        try:
            if name_category is None:
                name_category = self.controller.get_category(input("Enter category name: "))

            if (amount := int(input("Enter amount of funds: "))) < 0:
                print("Amount must be positive.")
                return

            if description is None:
                description = input("Enter description of funds: ")
            name_category.deposit(amount, description)
            print(f"Deposited: {amount}, Description: {description}")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


    def get_withdraw(self):
        try:
            name_category = self.controller.get_category(input("Enter category name: "))



            if name_category.withdraw(
                    (amount:=int(input("Enter amount of withdrawals: "))),
                    (description :=input("Enter description of withdrawals: "))
            ):

                print(f"Withdrawal: {amount}, Description: {description}")
            else:
                print("Not enough funds.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def transfer(self):
        try:
            from_category = self.controller.get_category(input("Transfer from category: "))
            to_category = self.controller.get_category(input("To category: "))


            if from_category.transfer(amount :=int(input("Enter amount of transfers: ")), to_category):
                print(f"Transferred: {amount} from {from_category.name} to {to_category.name}")
            else:
                print("Not enough funds to transfer!")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

    def show_category_detail(self):
        if category_name := self.controller.get_category(input("Enter category name: ")):
            print(category_name)
        else:
            print("Not found")

    def show_graphic_spent(self):
        print(self.controller.create_spend_chart())

