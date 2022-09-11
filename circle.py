class Circle():
    def __init__(self, ra):
        self.radius = ra

    def get_area(self):
        return self.radius ** 2 * 3.14

    def get_perimeter(self):
        return 2 * self.radius * 3.14


circle_one = Circle(11)
print(circle_one.get_area())
print(circle_one.get_perimeter())
