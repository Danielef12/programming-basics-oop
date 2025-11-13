class Input:
    """Class responsible for handling all user input operations."""

    def create_rectangle() -> tuple[int, int]:
        """Prompt the user to input the dimensions of a rectangle.

        Returns:
            tuple[int, int]: A tuple containing the width and height of the rectangle.
        """
        while True:
            width: int = Input.validate_positive_number("Insert width: ")
            height: int = Input.validate_positive_number("Insert height: ")
            if width != height:
                return width, height
            else:
                print("Width and height must be greater than or equal to two.")

    def create_square() -> int:
        """Prompt the user to input the side length of a square.

        Returns:
            int: The side length of the square.
        """
        width: int = Input.validate_positive_number("Insert side length: ")
        return width

    def get_intro_menu_selection() -> int | None:
        """Display the main menu and get the user's choice of shape.

        Returns:
            int | None: The user's menu selection (1, 2, or 3), or None if invalid input is entered.
        """
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

    def validate_positive_number(prompt: str) -> int:
        """Validate that the user input is a positive integer.

        Args:
            prompt (str): The text prompt displayed to the user.

        Returns:
            int: A positive integer input by the user.
        """
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number

                print("Please enter a positive number")
            except ValueError:
                print("Please enter a positive number")

    def if_not_square() -> str:
        """Ask the user if they want to create a square when one does not exist.

        Returns:
            str: 'y' if the user wants to create a square, 'n' otherwise.
        """

        print("For use this function, you must create a square shape.")
        while (choose := (input("Do you want create it?(y/n) "))) not in ("y", "n"):
            print("Please enter y or n")
        return choose

    def if_not_rectangle() -> str:
        """Ask the user if they want to create a rectangle when one does not exist.

        Returns:
            str: 'y' if the user wants to create a rectangle, 'n' otherwise.
        """
        print("For use this function, you must create a rectangle shape.")
        while (choose := (input("Do you want create it?(y/n) "))) not in ("y", "n"):
            print("Please enter y or n")
        return choose

    def get_shape() -> int:
        """Ask the user which shape they want to view.

        Returns:
            int | None: 1 for rectangle, 2 for square, or None if invalid input is entered.
        """
        print("Which shape do you want to view?")
        print("1. Rectangle")
        print("2. Square")
        try:
            while (choice := (int(input("Choose shape: ")))) not in (1, 2):
                print("Invalid input. Try again.")
            return choice
        except ValueError:
            print("Please enter a number.")

    def menu_after_shape() -> int:
        """Display the post-creation menu and get the user's choice.

        Returns:
            int | None: The user's menu selection (1–4), or None if invalid input is entered.
        """
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

    def modify_measures() -> tuple[str, int, int] | tuple[str, int] | None:
        """Allow the user to modify the dimensions of a shape.

        Returns:
            tuple[str, int, int] | tuple[str, int] | None:
                A tuple containing the shape type and its new dimensions,
                or None if invalid input is entered.
                - ("rectangle", width, height)
                - ("square", side)
        """
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
