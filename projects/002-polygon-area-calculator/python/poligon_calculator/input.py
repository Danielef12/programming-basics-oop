class Input:

    def create_rectangle():
        while True:
            width = Input.validate_positive_number("Insert width: ")
            height = Input.validate_positive_number("Insert height: ")
            if width != height:
                return width, height
            else:
                print("Width and height must be greater than or equal to two.")

    def create_square():
        width = Input.validate_positive_number("Insert side length: ")
        return width


    def get_intro_menu_selection():
        print("What shape do you want to work on?")
        print("1. Rectangle")
        print("2. Square")
        print("3. Rectangle / Square\n")
        try:
            while (choice := (int(input("Enter your choice: ")))) not in (1, 2, 3):
                print("Invalid input. Try again.")
            return choice
        except ValueError:
            print("Please enter a number.")


    def validate_positive_number(prompt):
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number

                print("Please enter a positive number")
            except ValueError:
                print("Please enter a positive number")

    def if_not_square():
        print("For use this function, you must create a square shape.")
        while (choose := (input("Do you want create it?(y/n) "))) not in ("y", "n"):
            print("Please enter y or n")
        return choose

    def if_not_rectangle():
        print("For use this function, you must create a rectangle shape.")
        while (choose := (input("Do you want create it?(y/n) "))) not in ("y", "n"):
            print("Please enter y or n")
        return choose

    def get_shape():
        print("Which shape do you want to view?")
        print("1. Rectangle")
        print("2. Square")
        try:
            while (choice := (int(input("Choose shape: ")))) not in (1, 2):
                print("Invalid input. Try again.")
            return choice
        except ValueError:
            print("Please enter a number.")

    def menu_after_shape():
        print("1. Calculate shape specs (Area, Perimeter, Diagonal)")
        print("2. Calculate amount square inside rectangle")
        print("3. Modify measures")
        print("4. Exit")
        try:
            while (choice := (int(input("Enter your choice: ")))) not in (1, 2, 3, 4):
                print("Invalid input. Try again.")
            return choice
        except ValueError:
            print("Please enter a number.")

    def modify_measures():
        print("\nWhich shape do you want to modify?")
        print("1. Rectangle")
        print("2. Square")

        try:
            while (choice := int(input("Choose shape: "))) not in (1, 2):
                print("Please enter 1 or 2")
            if choice == 1:
                width = Input.validate_positive_number("Enter new width: ")
                height = Input.validate_positive_number("Enter new height: ")
                return "rectangle", width, height
            elif choice == 2:
                side = Input.validate_positive_number("Enter new side: ")
                return "square", side
        except ValueError:
            print("Please enter a valid number")
