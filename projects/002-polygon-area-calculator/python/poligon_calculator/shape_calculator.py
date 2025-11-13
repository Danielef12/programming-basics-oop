from poligon_calculator.rectangle import Rectangle
from poligon_calculator.square import Square

class ShapeCalculator:
    def __init__(self):
        self.rectangle = None
        self.square = None

    def create_rectangle(self, width, height):
        self.rectangle = Rectangle(width, height)

    def create_square(self, side):
        self.square = Square(side)


    def set_height(self, height):
        if self.rectangle:
            self.rectangle.set_height(height)

    def set_width(self, width):
        if self.rectangle:
            self.rectangle.set_width(width)
    def set_side(self, side):
        if self.square:
            self.square.set_side(side)

    def square_in_rectangle(self):
        if self.rectangle is not None and self.square is not None:
            amount = self.rectangle.get_amount_inside(self.square)
            return amount
        return None