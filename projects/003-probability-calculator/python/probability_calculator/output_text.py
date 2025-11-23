class OutputText:
    def show_welcome_message():
        print("=" * 80)
        print("|| Welcome to Probability Calculator! ||")
        print("=" * 80)
        print("\nThis software is use to determine the approximate probability of drawing\n"
              "certain balls randomly from a hat.\n")

    def show_main_menu():
        print("=" * 80)
        print("Main Menu\n")

        print("1. Create new hat.")
        print("2. Show current hat.")
        print("3. Start Experiment.")
        print("0. Exit")

    def exit_message():
        print("=" * 80)
        print("Thank you for using this software.")
        print("=" * 80)