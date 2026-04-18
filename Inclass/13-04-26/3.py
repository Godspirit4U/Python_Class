class Animal:
    def sound(self):
        return "Some kind of sound"

    def move(self):
        return "Animal Moves"


class Dog(Animal):
    def dog_sound(self):
        return "Dog Barks"

    def dog_move(self):
        return "dog moves"
    




d1 = Dog()

print(d1.sound())
print(d1.dog_sound())
print(d1.move())
print(d1.dog_move())