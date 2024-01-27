#!/usr/bin/python3

class Square:
    def __init__(self, side=0):
        self.side = side

    def area(self):
        """Calculate and return the area of the square."""
        return self.side * self.side

    def perimeter(self):
        """Calculate and return the perimeter of the square."""
        return 4 * self.side

    def __str__(self):
        """Return a string representation of the square."""
        return "Square with side length {}".format(self.side)

if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print(s.area())
    print(s.perimeter())

