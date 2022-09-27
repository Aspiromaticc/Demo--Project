from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if '0' in choice or '1'in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")
    if how_much < 50:
        print("Nice you are greedy")

    else:
        dead("You greedy bastard")
def bear_room():
    print("""
    There is a bear here \nThe bear has a bunch of honey
    \nThe fat bear is in front of the door \nHow are you going to move
    the bear
    """)
    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "Take honey":
            dead("The bear looked at you and slapped you")
        elif choice == "Taunt bear" or "taunt bear" and not bear_moved:
            print("The bear has moved from the door \nYou can go through it now")
            bear_moved = True
        elif choice == 'Taunt bear' and bear_moved:
            dead("The bear get pissed off and chew your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")
def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("Print, he, it whatever stare at you and you go insane")
    print("Do you flee for your life or eat your head")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print(why, "Good job!")
    exit(0)
def start():
    print("You are in a dark room")
    print("There is a door to your left and right")
    print("Which one do you take?")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you serve")
start()
