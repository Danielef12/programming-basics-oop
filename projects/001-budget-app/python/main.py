from budget_app.menu import PrintMenu
from budget_app.app_function import AppFunction

class StartApp:
    @staticmethod
    def start():
        PrintMenu.print_initial_message()
        app = AppFunction()
        app.menu_selection()


if __name__ == "__main__":
    StartApp.start()