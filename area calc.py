import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def diagonal(self):
        return self.width * math.sqrt(2)


rect = Rectangle(8, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print("Diagonal:", round(rect.diagonal(), 2))

sq = Square(6)
print("\nArea:", sq.area())
print("Perimeter:", sq.perimeter())
print("Diagonal:", round(sq.diagonal(), 2))