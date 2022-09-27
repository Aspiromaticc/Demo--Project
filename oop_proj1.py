from random import randint
print("This is an app that contains the information of Facebook employees")
class Male:
    def __init__(self, name, job, address, level, company="Inspiron", gender="Male"):
        self.name = name
        self.job = job
        self.address = address
        self.level = level
        self.company = company
        self.__salary = None
    def persona(self):
        return  f"""
        {self.name} joined {self.company} as a {self.job} but he specialises in Edu.
        He is very hardworing and his grit for his work is of no equal. He lives in {self.address}.
        And He is currently a {self.level}.
        """
    def  bio(self):
        return f"""
        This is {self.name} details:
        Name: {self.name}
        WOrkplace: {self.company}
        Job: {self.job}
        Level: {self.level}
        Home Address: {self.address}
        """
class Bank:
    def __init__(self, name, deposit):
        self.name = name
        self.__deposit = deposit
        self.__actual_money = None
    def set_deposit(self, actual_money):
        self.__actual_money = actual_money
    def get_deposit():
        return self.__deposit * 2

class Female:
    def __init__(self, name, job, address, level, company="Inspiron", gender="Male"):
        self.name = name
        self.job = job
        self.address = address
        self.level = level
        self.company = company
        self.__salary = None
    def persona(self):
        return  f"""
        {self.name} joined {self.company} as a {self.job}.
        She is very hardworing and her grit for her work is of no equal. She lives in {self.address}.
        And she is currently a {self.level}.
        """
    def  bio(self):
        return f"""
        This is {self.name} details:
        Name: {self.name}
        WOrkplace: {self.company}
        Job: {self.job}
        Level: {self.level}
        Home Address: {self.address}
        """
class Employee(Male):
    pass
class Employee2(Female):
    pass
class SoftwareEngineer(Employee):
    pass
class Designer(Employee):
    pass
class Web_Developer(Employee):
    pass
class Marketer(Employee):
    pass

employees = [
Employee("Sean", "Software Engineer", "Seattle", "Junior"),
Employee("Hurd", "Software Engineer", "Brooklyn", "Senior"),
Employee2("Lola", "Software Engineer", "Los Angeles", "Junior"),
Employee("Nate", "Designer", "Washington", "Junior"),
Employee2("Lisa", "Designer", "Seattle", "Junior"),
Employee("Jason", "Designer", "West Virgina", "Senior"),
Employee("Lewin", "Sales representative", "Illinois", "Senior"),
Employee("Wyatt", "Sales representative", "Brooklyn", "Senior"),
Employee("Lewin", "Sales representative", "Illinois", "Senior")
]
dep1 = Bank("Jane", 10000)
dep1.set_deposit()
print(dep1.get_deposit(2))
print()
def dead(win):
    print(win, "oops")
    exit(0)
def interface():
    true = False
    while True:
        choice = input()
        if choice == employees[0].name and not true:
            print(employees[0].bio())
            print(employees[1].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                print("Reply with \"Yes\" or \"No\".")
        if choice == employees[1].name and not true:
            print(employees[1].bio())
            print(employees[1].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                print("Reply with \"Yes\" or \"No\".")
        if choice == employees[2].name and not true:
            print(employees[2].bio())
            print(employees[2].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        false = True
        if choice == employees[3].name and false:
            print(employees[3].bio())
            print(employees[3].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        if choice == employees[4].name and false:
            print(employees[4].bio())
            print(employees[4].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        if choice == employees[5].name and True:
            print(employees[5].bio())
            print(employees[5].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        if choice == employees[6].name and True:
            print(employees[6].bio())
            print(employees[6].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        if choice == employees[7].name and True:
            print(employees[7].bio())
            print(employees[7].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        if choice == employees[8].name and True:
            print(employees[8].bio())
            print(employees[8].persona())
            choice = input("DO YOU WANT TO CONTINUE? >")
            if choice == "yes":
                interface()
            elif choice == "no":
                dead("Thanks.")
            else:
                dead("Reply with \"Yes\" or \"No\".")
        elif choice is False:
            print("Type the name")
        else:
            print("Not in the database. Type another name")

#def Bank():
    #print("This is Bank A. How much do you want to deposit?")
    #choice = input("> ")
    #for x in choice:
        #choice = choice.set_deposit()
        #print(choice.get_deposit())

interface()
