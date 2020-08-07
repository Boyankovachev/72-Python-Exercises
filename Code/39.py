# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Square:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2


a = Square(10,20)
b = Square(5,100)
print(a.area(), b.area())