class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x},{self.y})'


class Point3D(Point2D):

    # Point3D DOES NOT INHERIT __slots__ AUTOMATICALLY from parent (Point2D)
    # and has a __dict__ if not __slots__ are defined

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


point = Point3D(10, 20, 30)
print(point.__dict__)   # works!

