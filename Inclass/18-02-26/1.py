# cylinder
class cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 3.14 * 2 * self.radius * self.height

    def volume(self):
        return 3.14 * self.radius * self.radius * self.height


c1 = cylinder(1, 1)
print(c1.surface_area(), c1.volume())

c2 = cylinder(2, 3)
print(c2.surface_area(), c2.volume())
