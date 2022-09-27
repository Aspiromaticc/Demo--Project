#Animal is-a object
class Animal(object):
    pass
#Dog is-a Animal
class Dog(animal):
    def __init__(self, name):
#Function __init__ has-a parameters self, name
        self.name = name
#Cat is-a Animal
class Cat(animal):
    def __init__(self, name):
#Function __init__ has-a parameters self, name
        self.name = name
#Person is-a object
class Person(object):
    def __init__(self, name):
#Function __init__ has-a parameters self, name
        self.name = name
        self.pet = None
#Employee is-a person
class Employee(person):
    def __init__(self, name, salary):
#Function __init__ has-a parameters self, name, salary
        super(Employee, self).__init__(name)
        #Employee has-a salary
        self.salary = salary
#Fish is-a object
class Fish(object):
    pass
#Salmon is-a Fish
class Salmon(fish):
    pass
#HAlibut is-a fish
class Halibut(fish):
    pass
#rover is-a Dog
rover = Dog("Rover")
#Satan is-a Cat
satan = Cat("Satan")
#Mary is-a Person
mary = Person("Mary")
#Mary has-a pet named satan
mary.pet = satan
#Frank is-a employee
frank = Employee("Frank", 12000)
#Frank has-a pet named rover
frank.pet = rover
#Fish has-a flipper
flipper = Fish()
#Salmon has-a crouse
crouse = Salmon()
#Halibut has-a harry
