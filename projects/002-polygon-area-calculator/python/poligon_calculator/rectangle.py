class Rectangle:
    """Class representing a rectangle shape with width and height.

    Provides methods for computing geometric properties such as area,
    perimeter, diagonal length, and ASCII visualization.
    """

    def __init__(self, width: int, height: int) -> None:
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width: int = width
        self.height: int = height

    def set_width(self, width: int) -> None:
        """Set a new width for the rectangle.

        Args:
            width (int): The new width value.
        """
        self.width = width

    def set_height(self, height: int) -> None:
        """Set a new height for the rectangle.

        Args:
            height (int): The new height value.
        """
        self.height = height

    def get_area(self) -> int:
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        """Calculate the diagonal length of the rectangle.

        Returns:
            float: The diagonal length, calculated using the Pythagorean theorem.
        """
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        """Return a string representation (ASCII art) of the rectangle.

        If the rectangle is too large (width or height > 50),
        a warning message is returned instead.

        Returns:
            str: A multi-line string made of '*' representing the rectangle,
                or a warning message if too large.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        design = ""
        for i in range(self.height):
            design += ("*" * self.width) + "\n"
        return design

    def get_amount_inside(self, shape) -> int:
        """Determine how many times another shape fits inside this rectangle.

        Args:
            shape (Rectangle): Another shape (typically a Square)
                to fit inside this one.

        Returns:
            int: The total number of times the given shape can fit inside.
        """
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self) -> str:
        """Return a human-readable string representation of the rectangle.

        Returns:
            str: A formatted description of the rectangle.
        """
        return f"Rectangle (width={self.width}, height={self.height}"
