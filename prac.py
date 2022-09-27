from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take")
    choice = int(input("> "))
    if choice < 50:
        print("You are greedy")
    else:
        dead("You are fucking greedy. Bastard!")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of the door")
    print("How are you going to move?")
    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "Take honey":
            dead("The bear looked at you and slapped you")
        elif choice == "Taunt bear" and not bear_moved :
            print("The bear has moved from the door \nYou can go through it now")
            bear_moved = True
        elif choice == 'Taunt bear'and bear_moved:
            dead("The bear get pissed off and chew your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")
def cthulhu_room():
    print("Here you see the great Cthulhu")
    print("If he stares at you, you go insane")
    print("Do you flee for your life or eat your head?")
    choice = input("> ")
    if choice == "flee":
        start()
    elif choice == "head":
        print("You stumbled around your room until you serve")
def dead(why):
    print(why, "Good job!")
    exit(0)
def start():
    print("You are in a dark room")
    print("There is a door to your left and right")
    print("Which one do you take")
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("I got no idea what that means")
start()
