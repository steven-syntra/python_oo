from pprint import pprint


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x},{self.y})'


point = Point2D(0, 0)

# Gives an error because not dict exists:
# print(point.__dict__)

# No error:
# print(point.__slots__)

# Error because z is not in slots:
# point.z = 0

# No error: class attributes CAN be added, even if not in slots
Point2D.color = "Black"
pprint(Point2D.__dict__)
