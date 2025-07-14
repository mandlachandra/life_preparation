class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("dog barks")

d = Dog()
d.speak()