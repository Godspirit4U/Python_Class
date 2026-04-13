class person:
    def __init__(self, name, age, gender, height):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__height = height

    def __str__(self):
        return f"Name:{self.__name}\nAge:{self.__age}\nGender:{self.__gender}\nHeight:{self.__height}\n"

    def update(self,age=None, height=None):
        if age is not None:
            self.__age = age
        if height is not None:
            self.__height = height


s1 = person("Abc", 19, "male", 170)
print(s1)  # <__main__.person object at 0x00000272FD866A50>

s1.update(height=183)
s1.update(age=20)

print(s1)

s2 = person("Xyz", 17, "female", 160)
print(s2)
s2.update(age=18, height=168)
print(s2)

s2.age = 22
print(s2)
'''  I dont want the details of attributes to be changed in main or outside the class   '''
