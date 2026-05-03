class employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def __str__(self):
        return f"\nName: {self.name} \nId: {self.id} \nSalary: {self.salary}"

    def update_salary(self, value):
        self.salary = value
        print(f"Your salary has been updated to {self.salary}")


class sde(employee):
    def __init__(self, name, id, salary, role):
        super().__init__(name, id, salary)
        self.role = role

    def __str__(self):
        return super().__str__() + f"\nrole :{self.role}"


class senior_sde(sde):
    def __init__(self, name, id, salary, role, level):
        super().__init__(name, id, salary, role)
        self.level = level

    def __str__(self):
        return super().__str__() + f"\nLevel: {self.level}\n"


sn1 = senior_sde("Dhruva", 12, 100000, "sde", "1")
print(sn1)
