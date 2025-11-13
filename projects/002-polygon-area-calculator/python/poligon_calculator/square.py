from poligon_calculator.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(height= side, width= side)
        self.width = side
        self.height = side
        self.side = side

    def set_side(self, side):
        self.height = side
        self.width = side



    def __str__(self):
        return f"Square(side={self.width}"
