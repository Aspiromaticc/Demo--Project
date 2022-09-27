from sys import exit
def gold_room():
    print("The room is full of gold. How many do you take?")
    choice = input("> ")
    if '0' in choice and '1' in choice:
        home = int(choice)
    else:
        dead("Man, learn to type number")
    if home < 50:
        print("Nice, you are greedy")
        exit(0)
    else:
        dead("You are fucking greedy bastard")
def bear_room():
    print("""
    There is a bear here\nThe bear has a bunch of honey\nThe fat bear is in front of the door\nHow are you going to move the bear
    """)
    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "Take honey":
            dead("The bear looked at you and slapped you")
        elif choice == 'Taunt bear' and not bear_moved:
            print("The bear has moved from the door. You can go through it")
            bear_moved = True
        elif choice == "Toss bear" and bear_moved:
            dead("Sorry, try to keep your cool bro")
        elif choice == "open door" or "Open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")
def cthulhu_room():
    print("Here you see the great Cthulhu")
    print("You'll go insane, if he stares at you")
    print("Do you flee for your life or eat your head")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty")
    else:
        cthulhu_room()
def dead(win):
    print(win, ".That's good!")
    exit(0)
def start():
    print("You are in a dark room")
    print("There's a door to you left and right")
    print("Which one do you take")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("I got no idea what that means")
start()
