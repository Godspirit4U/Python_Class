# list

class my_list:
    def __init__(self):
        self.l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.count = 0

    def my_append(self, value):
        self.l[self.count] = value
        self.count = self.count + 1

    def print_list(self):
        print("[", end = "")
        for i in range(self.count):
            if i != (self.count - 1):
                print(self.l[i], end = ", ")
            else:
                print(self.l[i], end = "")
        print("]\n")

    def update(self, value, index):
        self.l[index] = value
    
    def insert(self, value, index):
        count = self.count
        while count > index:
            self.l[count] = self.l[count - 1]
            count -= 1

        self.count += 1
        self.l[index] = value

    
    def __str__(self):

        # return self.l.print_list()


        print("[", end = "")
        for i in range(self.count):
            if i != (self.count - 1):
                print(self.l[i], end = ", ")
            else:
                print(self.l[i], end = "")
        print("]", end = "")
        return ""

    def delete_by_value(self, value):

        for i in range(self.count):
            if self.l[i] == value:
                index = i

        for i in range(index, self.count - 1):
            self.l[i] = self.l[i + 1]

        self.count -= 1

    def deletye_by_index(self, index):

        for i in range(index, self.count):
            self.l[i] = self.l[i + 1]
        
        self.count -= 1

l1 = my_list()
l1.my_append(7)
l1.my_append(5)
l1.my_append(4)
l1.my_append(5)
l1.my_append(4)
l1.print_list()
# print(l1)
# l1.update(100, 2)
# l1.print_list()

l1.insert(200, 2)
# l1.print_list()
print(l1)

print(l1)
l1.delete_by_value(200)
print(l1)
l1.deletye_by_index(0)
print(l1)