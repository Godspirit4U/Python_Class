class Person:
    def __init__(self, name, age, height):
        self.age = age
        self.name = name
        self.height = height

    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nHeight: {self.height}"

    def update(self, height=None, age=None):
        if age is not None:
            self.age = age
        if height is not None:
            self.height = height


class Employee(Person):
    def __init__(self, name, age, height, role):
        super().__init__(name, age, height)
        self.role = role

    def get_details(self):
        print(self)
        print(e1.role)


e1 = Employee("Elon Musk", 44, 170, "Sweeper")

                                                                              
                                                                              
# print(e1)
e1.get_details()

# p1 = Person("Sivaharsha", 18, 180)
# p2 = Person("Dhruva", 32, 220)

# print(p1)
# print(p2)

# p1.update(age=20)
# print(p1)
