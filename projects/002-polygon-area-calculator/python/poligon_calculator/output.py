class Output:

    def welcome():
        print("WELCOME TO THE SHAPE CALCULATOR\n")


    def print_shape_specs(shape):
        specs = f"{shape}:\n"
        specs += f"Width: {shape.width} Height: {shape.height}\n"
        specs += f"Area: {shape.get_area()}\n"
        specs += f"Perimeter: {shape.get_perimeter()}\n"
        specs += f"Diagonal: {shape.get_diagonal():.2f}\n"
        specs += f"Pic:\n{shape.get_picture()}"
        print(specs)



    def print_how_square_in_rect(amount):
        print(f"In rectangle area can stay {amount} square units")
