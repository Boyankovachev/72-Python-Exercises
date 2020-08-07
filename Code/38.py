# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * self.radius * self.radius


krug4e = Circle(10)
krug4e2 = Circle(375)
print(krug4e.area(), krug4e2.area())