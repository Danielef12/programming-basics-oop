class GetUserInput:
    """Utility class that handles and validates user input."""
    def validate_positive_number(prompt: str) -> int:
        """Ask the user for a positive integer number.

                Args:
                    prompt (str): Message shown to the user.

                Returns:
                    int: A validated positive integer.
                """
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a positive number")

    def get_user_choice() -> str:
        """Request the user's menu choice (0–3).

                Returns:
                    str: The chosen option ("0", "1", "2", "3").
                """
        while (choice := input("Enter your choice: ").strip()) not in ("1", "2", "3", "0"):
            print("Invalid choice. Please try again.")
        else:
            return choice


