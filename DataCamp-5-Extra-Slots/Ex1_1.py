class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x},{self.y})'


point = Point2D(0, 0)
print(point.__dict__)
