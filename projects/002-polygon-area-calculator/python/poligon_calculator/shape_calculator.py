from typing import Optional

from poligon_calculator.rectangle import Rectangle
from poligon_calculator.square import Square


class ShapeCalculator:
    """Class responsible for managing and performing operations on geometric shapes.

    This class acts as a bridge between user input and geometric computations.
    It supports creating, modifying, and calculating relationships between
    rectangles and squares.
    """

    def __init__(self) -> None:
        """Initialize the ShapeCalculator with no shapes created."""
        self.rectangle = None
        self.square = None

    def create_rectangle(self, width: int, height: int) -> None:
        """Create and store a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.rectangle = Rectangle(width, height)

    def create_square(self, side: int) -> None:
        """Create and store a new Square object.

        Args:
            side (int): The side length of the square.
        """
        self.square = Square(side)

    def set_height(self, height: int) -> None:
        """Set the height of the current rectangle, if one exists.

        Args:
            height (int): The new height value.
        """
        if self.rectangle:
            self.rectangle.set_height(height)

    def set_width(self, width: int) -> None:
        """Set the width of the current rectangle, if one exists.

        Args:
            width (int): The new width value.
        """
        if self.rectangle:
            self.rectangle.set_width(width)

    def set_side(self, side: int) -> None:
        """Set the side length of the current square, if one exists.

        Args:
            side (int): The new side length.
        """
        if self.square:
            self.square.set_side(side)

    def square_in_rectangle(self) -> Optional[int]:
        """Calculate how many squares can fit inside the current rectangle.

        Returns:
            Optional[int]: The number of squares that fit inside the rectangle,
            or None if either shape has not been created yet.
        """
        if self.rectangle is not None and self.square is not None:
            amount: int = self.rectangle.get_amount_inside(self.square)
            return amount
        return None
