class Output:
    """Class responsible for displaying information to the user."""

    def welcome() -> None:
        """Display a welcome message at the start of the program."""
        print("WELCOME TO THE SHAPE CALCULATOR\n")

    def print_shape_specs(shape) -> None:
        """Print the specifications of a given shape, including dimensions,
        area, perimeter, diagonal, and a visual representation.

        Args:
            shape: The shape object containing geometric data.
        """
        specs = f"{shape}:\n"
        specs += f"Width: {shape.width} Height: {shape.height}\n"
        specs += f"Area: {shape.get_area()}\n"
        specs += f"Perimeter: {shape.get_perimeter()}\n"
        specs += f"Diagonal: {shape.get_diagonal():.2f}\n"
        specs += f"Pic:\n{shape.get_picture()}"
        print(specs)

    def print_how_square_in_rect(amount: int) -> None:
        """Print the number of squares that can fit inside a rectangle.

        Args:
            amount (int): The number of squares that fit within the rectangle.
        """
        print(f"In rectangle area can stay {amount} square units")
