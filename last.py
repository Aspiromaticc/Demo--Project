def Brymo(a, b):
    print(f"I usually sing \"{a}\" but \"{b}\" is my favourite")
    return a, b
def Wizkid(a, b):
    print(f"I love Wizkid when he released \"{a}\" but I still like his new release-{b}")
    return a, b
def Olamide(a, b):
    print(f"Olamide cane into limelight when he released {a} and {b}")
    return a, b
Brymo = Brymo("There's a place", "A billion naira dream")
Wizkid = Wizkid("Holla at your boy", "Essence")
Olamide = Olamide("Eni duro", "Yahoo Boy No Laptop")
print(f"""
I like these Brymo's song: {Brymo} \nThese two songs- {Wizkid}- are
among Wizzy greatest songs. \nOlamide is a legend. These songs - {Olamide}- brought him
into the industry
""")
