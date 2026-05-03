class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat Meows")


class Animal(Dog, Cat):
    def sound(self):
        print("animal makes sound")


animal_1 = Animal()
animal_1.sound()
