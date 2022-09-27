class Parent:
    def implicit(self):
        print("We are money")
#Explicit inheritance: CHild making its own element
class Child(Parent):
    def implicit(self):
        print("Fucking awesome")
boy = Parent()
girl = Child()
boy.implicit()
girl.implicit()

class Father(object):
    def altered(self):
        print("This is the father")
    def willy(self):
        print("I fit dey kolomenta")
class Son(Father):
    def altered(self):
        print("This is the son")
        super(Son, self).altered()
        print("This is son 2")
x = Father()
y = Son()
x.altered()
y.altered()
x.willy()
y.willy()
#Composition
class Adetunji(object):
    def override(self):
        print("This is the 1")
    def implicit(self):
        print("Jane the willy")
    def altered(self):
        print("I can't reason")
class Aderemi(object):
    def __init__(self):
        self.other = Adetunji()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("EverytimeI ball")
    def altered(self):
        print("We are money launderers")
        self.other.altered()
        print("We're goin' to do this bro")
son = Aderemi()
son.implicit()
son.altered()
son.override()
