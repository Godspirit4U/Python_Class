class person:
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    def show_details(self):
        print(f'--------------------\nName : {self.name}\nID : {self.id}\nCGPA : {self.cgpa}\n')

    def cgpa_checker(self):
        if self.cgpa < 8:
            print("You need to work hard\n\n")
        else:
            print('You worked hard enough\n\n')

    def update_gpa(self, new_gpa):
        self.new_gpa = new_gpa
        self.cgpa = (self.cgpa + self.new_gpa) / 2
        print("Congrats! you improved")


p1 = person('Spirit', 1245, 9.6)
p1.show_details()
p1.cgpa_checker()

p2 = person('Dhruva', 1698, 9.8)
p2.show_details()
p2.cgpa_checker()

p3 = person('Dollar', 8554, 7.4)
p3.update_gpa(9.2)
p3.show_details()
