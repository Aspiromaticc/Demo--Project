class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def description(self):
        return f"{self.name} is {self.age} and his color is {self.color}"
    def speak(self, sound):
        return f"{self.name} speaks {sound}"
class Jackinson(Dog):
    pass


jack = Jackinson("Jack", 10, "Black")
robbin = Dog("Robbin", 8, "Pink")
craig = Dog("Craig", 12, "White")
print(jack.description())
print(robbin.description())
print(craig.description())
print(jack.speak("Gbo Gbo"))
print(jack.name)
print(robbin.name)
print(craig.name)
