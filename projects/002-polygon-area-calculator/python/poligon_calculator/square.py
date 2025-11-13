from poligon_calculator.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square, a special type of rectangle
    where all sides have equal length.
    """

    def __init__(self, side: int) -> None:
        """Initialize a Square instance.

        Args:
            side (int): The length of each side of the square.
        """
        super().__init__(height=side, width=side)

        self.width = side
        self.height = side
        self.side = side

    def set_side(self, side: int) -> None:
        """Set a new side length for the square.

        Updates both width and height to maintain equality.

        Args:
            side (int): The new side length of the square.
        """
        self.height = side
        self.width = side

    def __str__(self) -> str:
        """Return a human-readable string representation of the square.

        Returns:
            str: A formatted description of the square.
        """
        return f"Square(side={self.width}"
