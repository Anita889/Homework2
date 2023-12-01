from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def area(self):
        pass  # To be implemented by subclasses

    def volume(self):
        pass  # To be implemented by subclasses


class Square(Shape):
    def __init__(self, side_length):
        super().__init__("Square")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Cuboid(Shape):
    def __init__(self, length, width, height):
        super().__init__("Cuboid")
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


class Cone(Shape):
    def __init__(self, radius, height):
        super().__init__("Cone")
        self.radius = radius
        self.height = height

    def volume(self):
        return (1 / 3) * pi * self.radius ** 2 * self.height


# Example usage:
square = Square(4)
triangle = Triangle(3, 5)
cuboid = Cuboid(2, 3, 4)
cone = Cone(3, 6)

print(f"{square} Area: {square.area()}")
print(f"{triangle} Area: {triangle.area()}")
print(f"{cuboid} Volume: {cuboid.volume()}")
print(f"{cone} Volume: {cone.volume()}")
