from random import randint
se1 = ["Software Engineer", "Name" "Age", "Salary"]
class Employee:

    def __init__(self, name, age, salary, level):
        self.name = name
        self.age = age
        self.salary = salary
        self.level = level
    def work(self):
        return f"{self.name} is working"
class Designer(Employee):
    def __init__(self, name, age, salary, level, company ):
        super().__init__(name, age, salary, level)
        self.company = company
    def Company(self):
        return f"{self.name} works in {self.company}"
    def Salary(self):
        return self.salary * 0.8
class Product_Designer(Designer):
    def __init__(self, name, age, salary, level, company, product):
        super().__init__(name, age, salary, level, company)
        self.product = product
class SoftwareEngineer(Employee):
    #class attribute
    alias = "Computer savant"
    def code(self):
        return f"{self.name} is writing code"
    def code_in_a_language(self, language):
        return f"{self.name} is writing code in {language}"
    @staticmethod
    def entry_level(age):
        if age < 25:
            return 5000
        if age > 25:
            return 7000
        return 9000
    #def __eq__(self, other):
        #return self.name == other.name and self.age == other.age
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, salary = {self.salary}"
        return information
    def enter(self):
        print(SoftwareEngineer.se1[randint(0, len(self.se1)-1)])
employees = [
SoftwareEngineer("Jane", 20, 5000, "Junior"),
SoftwareEngineer("Jim", 27, 9000, "Senior"),
Designer("Karl", 23, 9000, "Senior", "Apple")
]
for employee in employees:
    print(employee.work())
se1 = SoftwareEngineer("Jane", 20, 5000, "Junior")
se2 = SoftwareEngineer("Nate", 25, 7000, "Senior")
se3 = SoftwareEngineer("Jim", 27, 9000, "Senior")
des1 = Designer("Karl", 23, 9000, "Senior", "Apple")
des2 = Designer("Ryan", 25, 4000, "Junior", "Facebook")
des3 = Designer("Michael", 27, 11000, "Senior", "Twitter")
print(se1.code())
print(se2.code())
print(se3.code())
print(des1.Company())
print(des2.Company())
print(des3.Company())
print(se1.code_in_a_language("Python"))
print(se2.code_in_a_language("C++"))
print(se3.code_in_a_language("Java"))
print(se1 == se2)
print(se3.entry_level(27))
print(se1)
print(des1.Salary())
