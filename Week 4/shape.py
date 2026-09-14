"""Week 4 assignment: Shape class and advanced Python concepts."""

class Shape:
    """Represent a rectangle using length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Shape(length={self.length}, width={self.width})"


if __name__ == "__main__":
    shape = Shape(10, 5)
    print(shape)
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
