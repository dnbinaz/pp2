import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

distance = point1.dist(point2)
print("Distance between the points:", distance)

point1.move(3, 5)
point1.show()
