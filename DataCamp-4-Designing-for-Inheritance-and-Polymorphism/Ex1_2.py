# Define a Rectangle class
class Rectangle:

    def __init__(self, h, w):
        self.h = h
        self.w = w


# Define a Square class
class Square(Rectangle):

    def __init__(self, w):
        self.h = w
        self.w = w
