# Define a Rectangle class
class Rectangle:

    def __init__(self, h, w):
        self.h = h
        self.w = w


# Define a Square class
class Square(Rectangle):

    def __init__(self, w):
        self.z = w


r = Rectangle(10,20)
print(r.__dict__)

s = Square(4)
print(s.__dict__)
