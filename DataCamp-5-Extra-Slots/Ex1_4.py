class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x},{self.y})'


class Point3D(Point2D):

    # Point3D DOES NOT INHERIT __slots__ AUTOMATICALLY from parent (Point2D)

    # BUT IT DOES if you define it like this
    __slots__ = ('z',)      # komma is there to make it a tuple
                            # x and y inherited from Point2D

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f'Point3D({self.x},{self.y},{self.z})'


if __name__ == '__main__':

    point = Point3D(10, 20, 30)
    print(point)
    # print(point.__dict__)
    # point.b = 10
    # print(point.b)
