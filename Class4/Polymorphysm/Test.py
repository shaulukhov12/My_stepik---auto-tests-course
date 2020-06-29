from poly import Square, Circle, Rectangle
rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

sq1 = Square(5)
sq2 = Square(7)

cir1 = Circle(3)
cir2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure, figure.get_area())
