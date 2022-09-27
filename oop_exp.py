class Car:
    def __init__(self, name, color, mileage):
        self.name = name
        self.color = color
        self.mileage = mileage
    def description(self):
        return f"The colour of the {self.name} is {self.color} and it can attain {self.mileage} in few minute"
toyota = Car("Toyota Camry", "Pink", "30 miles")
print(toyota.description())
venza = Car("Venza 8", "Gold", "20, 000 miles")
print(venza.description())
