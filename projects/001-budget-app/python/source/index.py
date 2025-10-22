from source.class_config.budget import Category
from source.utility.create_spend_chart import create_spend_chart

def menu():
    print("Welcome to Budget App")
    categories = {}
    while True:
        print("What would you like to do?")
        print("1. Create a new category budget")
        print("2. Add founds to your category budget")
        print("3. Get a withdraw")
        print("4. transfer between categories ")
        print("5. Show category balance")
        print("6. Show graphic spent")

        selection = input("What would you like to do? ")
        match selection:
            case "1":
                name = input("Name of category: ")
                categories[name] = Category(name)
                print(f"Category {name} created")
            case "2":
                name = input("Name of category to deposit: ")
                if name in categories:
                    amount = float(input("Amount to deposit: "))
                    description = input("Description: ")
                    categories[name].deposit(amount, description)
                    print(f"Deposited {amount} to {description}")
                else:
                    print("Category not found")

            case "3":
                name = input("Name of category to withdraw: ")
                if name in categories:
                    amount = float(input("Amount to withdraw: "))
                    description = input("Description: ")
                    if categories[name].withdraw(amount, description):
                        print("Withdrawn successfully")
                    else:
                        print("Insufficient funds")
                else:
                    print("Category not found")

            case "4":
                from_category = input(" Transfer from: ")
                to_category = input("Transfer to: ")
                if from_category in categories and to_category in categories:
                    amount = float(input("Amount to transfer: "))
                    if categories[from_category].transfer(amount, categories[to_category]):
                        print(f"Transfer {amount} from {from_category} to {to_category}")
                    else:
                        print("Insufficient funds")
                else:
                    print("One or more category not found")

            case "5":
                name = input("Name of category: ")
                if name in categories:
                    print(categories[name])

            case "6":
                if categories:
                    print(create_spend_chart(list(categories.values())))

            case "7":
                print("Thank you for using Budget App")
                break

            case _:
                print("Invalid selection")