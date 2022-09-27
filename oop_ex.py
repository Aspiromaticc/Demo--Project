class Roommates:
    def __init__(self, name, age, town, food, course, song):
        self.name = name
        self.age = age
        self.town = town
        self.food = food
        self.course = course
        self.song = song
    def __repr__(self):
        return f"{self.name} was a bad boy in the room. He is studying {self.course}"
    def description(self):
        return f"{self.name}'s favourite food is {self.food}"
    def sound(self):
        return f"Whenever {self.name} is in distress he usually sings {self.song}"
class Adetunji(Roommates):
    def desc(self):
        return f"{self.name} is a great man"
Aderemi = Roommates("Aderemi", 6, "Apomu", "Cheese Omellet", "Demography and Social Statistics", "\"Don't be scared to get lost and be found\"")
Isaac = Adetunji("Isaac", 20, "Akure", "Rice and Beans", "Microbiology", "\"Let's get high and fall from the sky\"")
Nelson = Roommates("Nelson", 21, "Akure", "Spagnoodles", "Chemical engineering", "\"We are here, we are breathing is suffice for everyone of us\"")


print(Aderemi)
print(Nelson)
print(Isaac)
print(Aderemi.description())
print(Aderemi.sound())
print(Nelson.sound())
print(Isaac.sound())
print(Isaac.desc())
