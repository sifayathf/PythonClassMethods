class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side


class Cube(Square):
    def area(self):
        face_area = self.side * self.side
        return super().area() * 6
    def volume(self):
        vol=super().area() * self.side
square = Square(5)
cube = Cube(6)
print(square.area())
print(cube.area())
print(cube.volume())
