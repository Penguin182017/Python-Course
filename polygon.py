class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        if shape.width == 0 or shape.height == 0:
            return 0
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect)
    print("Area:", rect.get_area())
    print("Perimeter:", rect.get_perimeter())
    print("Diagonal:", rect.get_diagonal())
    print(rect.get_picture())

    rect.set_height(3)
    rect.set_width(7)
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq)
    print("Area:", sq.get_area())
    print("Perimeter:", sq.get_perimeter())
    print("Diagonal:", sq.get_diagonal())
    print(sq.get_picture())

    sq.set_side(4)
    print(sq)
    sq.set_width(2)
    print(sq)

    rect = Rectangle(16, 8)
    print(rect)
    print("Squares of side 3 inside:", rect.get_amount_inside(Square(3)))

    rect2 = Rectangle(4, 8)
    print("Rectangles 4x8 inside:", rect.get_amount_inside(rect2))