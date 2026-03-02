# i = -1 ** (1/2)
# x = 3 + (4 * i)
# print(type(x))


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def details(self):
        return f"x: {self.x} and y: {self.y}"

    def scale(self, value):
        self.x = value * self.x
        self.y = value * self.y

    def magnitude(self):
        return ((self.x ** 2) + (self.y ** 2)) ** (1/2)

    def sum_complex(self, other_complex_num):
        c = complex(0, 0)
        c.x = self.x + other_complex_num.x
        c.y = self.y + other_complex_num.y
        return c

    def sub_complex(self, other_complex_num):
        c = complex(0, 0)
        c.x = self.x - other_complex_num.x
        c.y = self.y - other_complex_num.y
        return c
    
    def multiply(self, other_complex_num):
        c = complex(0, 0)

        c.x = (self.x * other_complex_num.x) - (self.y * other_complex_num.y)
        c.y = (self.x * other_complex_num.y) + (self.y * other_complex_num.x)
        return c

c1 = complex(2, 3)
c2 = complex(4, 5)

c3 = c1.sum_complex(c2)
print(c3.details())

c4 = c1.sub_complex(c2)
print(c4.details())

c5 = c1.multiply(c2)
print(c5.details())