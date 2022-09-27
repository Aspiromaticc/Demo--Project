ten_things = "Ryan Brymo Wizkid Fireboy Joeboy Rema"
print("The list is not up to 10. Let's add to it")
stuff = ten_things.split(' ')
more_stuff = ["Burnaboy", "Cheque", "Blaqbonez", "Tekno", "Skales", "Ruger", "Drille", "Psquare")
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    next_one.append(ten_things)
