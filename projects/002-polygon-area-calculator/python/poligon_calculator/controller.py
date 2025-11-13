from poligon_calculator.input import Input
from poligon_calculator.output import Output
from poligon_calculator.shape_calculator import ShapeCalculator


class Controller:
    """Main controller class responsible for managing user interactions
    and delegating shape-related operations to the ShapeCalculator.
    """

    def __init__(self):
        """Initialize the Controller instance and create a ShapeCalculator object."""
        self.shape_calculator = ShapeCalculator()

    def start(self) -> None:
        """Start the program by displaying the intro menu and handling user choices."""
        Output.welcome()
        choice = Input.get_intro_menu_selection()

        match choice:
            case 1:
                self.handle_rect()
            case 2:
                self.handle_square()
            case 3:
                self.handle_square_and_rect()
            case _:
                print("You didn't enter a valid choice")
                return
        self.second_menu()

    def handle_rect(self) -> None:
        """Handle the creation of a rectangle by collecting user input and storing it."""

        width, height = Input.create_rectangle()
        self.shape_calculator.create_rectangle(width, height)
        print("Rectangle create successfully")

    def handle_square(self) -> None:
        """Handle the creation of a square by collecting user input and storing it."""

        side = Input.create_square()
        self.shape_calculator.create_square(side)
        print("Square create successfully")

    def handle_square_and_rect(self) -> None:
        """Handle the creation of both a rectangle and a square."""

        self.handle_rect()
        self.handle_square()

    def second_menu(self) -> None:
        """Display the secondary menu and handle subsequent user interactions."""

        while True:
            choice = Input.menu_after_shape()

            match choice:
                case 1:
                    self.show_specs()
                case 2:
                    self.calculate_square_in_rect()

                case 3:
                    self.modify_shapes()
                case 4:
                    print("Thank you for using this program")
                    break
                case _:
                    print("You didn't enter a valid choice")

    def show_specs(self) -> None:
        """Display the specifications (area, perimeter, etc.) of the chosen shape."""

        shape_choice = Input.get_shape()

        if shape_choice == 1:
            if self.shape_calculator.rectangle:
                Output.print_shape_specs(self.shape_calculator.rectangle)
            else:
                print("You didn't enter a valid shape")
        elif shape_choice == 2:
            if self.shape_calculator.square:
                Output.print_shape_specs(self.shape_calculator.square)
            else:
                print("You didn't enter a valid shape")

    def calculate_square_in_rect(self) -> None:
        """Calculate how many squares fit inside the rectangle.

        This method ensures that both shapes exist. If not, it prompts
        the user to create them first. It then calls the calculator
        to determine how many squares can fit within the rectangle.
        """
        try:
            if not self.shape_calculator.rectangle:
                choice = Input.if_not_rectangle()
                if choice == "y":
                    self.handle_rect()
                else:
                    return

            if not self.shape_calculator.square:
                choice = Input.if_not_square()
                if choice == "y":
                    self.handle_square()
                else:
                    return

            amount = self.shape_calculator.square_in_rectangle()
            if amount is not None:
                Output.print_how_square_in_rect(amount)
        except Exception as e:
            print(f"Error calculating square in rectangle: {e}")

    def modify_shapes(self) -> None:
        """Allow the user to modify the measures of existing shapes.

        Raises:
            Exception: If an unexpected error occurs during modification.
        """
        try:
            if not self.shape_calculator.rectangle and not self.shape_calculator.square:
                print("No shape has been created.")
                return

            result = Input.modify_measures()

            if result is None:
                return

            if result[0] == "rectangle":
                if self.shape_calculator.rectangle:
                    _, width, height = result
                    self.shape_calculator.set_width(width)
                    self.shape_calculator.set_height(height)
                    print("Rectangle modify successfully")
                else:
                    print("You didn't enter a valid shape")

            elif result[0] == "square":
                if self.shape_calculator.square:
                    _, side = result
                    self.shape_calculator.set_side(side)
                    print("Square modify successfully")
                else:
                    print("You didn't enter a valid shape")
        except Exception as e:
            print(f"Error modifying shape: {e}")
