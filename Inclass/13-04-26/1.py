class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_details(self):
        return f"{self.x} + i{self.y}"
    
    def add(self, other_obj):
        self.x += other_obj.x
        self.y += other_obj.y
        # return self
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1)
print(c1.get_details())
c1.add(c2)
print(c1.get_details())