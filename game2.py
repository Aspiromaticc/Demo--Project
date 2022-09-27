from sys import exit

def volunteers():
    print("How many volunteers do you have already?")
    choice = int(input("> "))
    if choice > 1:
        print("How many volunteers do you need?")
        free = int(input("> "))
        if free > 20:
            print("I can only get you 20 free volunteers")
            print("Do you want to continue?")
            choice = input("> ")
            if choice == "Yes":
                print("What are the names of the volunteers?")
                choice = input("> ")
                vol_names = f'"{choice}"'
                stuff = vol_names.split(' ')
                more_names = ["Jason", "Akolawole", "Deborah", "Felix", "Frederick", "Benedict", "Emmanuel", "Bukola", "Oyintola", "Kemisola"]
                while len(stuff) != free:
                    screw = more_names.pop()
                    print("Adding volunteers:", screw)
                    stuff.append(screw)
                    print(f"The number of volunteers is now {len(stuff)}")
                print("There we go:", stuff)
            elif choice == "No":
                dead("You can check out other features on our app")
            else:
                dead("You can checkout others features on our apps")
        elif free < 21:
                print("What are the names of the volunteers?")
                choice = input("> ")
                vol_names = f'"{choice}"'
                stuff = vol_names.split(' ')
                more_names = ["Jason", "Akolawole", "Deborah", "Felix", "Frederick", "Benedict", "Emmanuel", "Bukola", "Oyintola", "Kemisola"]
                while len(stuff) != free:
                    screw = more_names.pop()
                    print("Adding volunteers:", screw)
                    stuff.append(screw)
                    print(f"The number of volunteers is now {len(stuff)}")
                print("There we go:", stuff)
def start():
    print("Yup. Welcome to the adventure of Truth or Dare")
    print("There are 20 Truth or Dare questions in this game")
    print("And you need to answer all the questions, else the demon will kill you")
    print("You need to choose between Truth or Dare")
    print("Truth or Dare")

    while True:
        choice = input("> ")
        if choice == "Truth":
            print("What is the secret that you can't share with nobody?")
            end = input()
        elif choice == "Dare":
            print("I dare you to laugh and drink 2 sachets of water. Type 'done' when you're done.")
            choice = input("> ")
            if choice == "done":
                print("Weldone man. You can fucking continue to the next stage")
            else:
                dead("You are done man.  The demon will kill you soon")
        else:
            dead("You need to choose between Truth or Dare")
        print("Do you want to advance to the next stage?")
        choice = input("> ")
        if choice == "Yes":
            print("This is the second question. Truth or Dare?")
            end = input("> ")
            if end == "Truth":
                print("What is the name of your sister? and is she in OAU?")
                end = input()
            elif end == "Dare":
                print("I dare you to share your sister's number with Remi")
                end =int(input())
                if end > 50:
                    home = end
                else:
                    dead("Learn to type number man")
            else:
                dead("Learn to read instruction bro.")
        else:
            print("Super man")
        print("Do you want to advance to the next stage")
        choice = input("> ")
        if choice == "Yes":
            print("This is the third question. Truth or Dare?")
            choice = input("> ")
            if choice == "Truth":
                print("Have you had sex before?", end = '')
                end = input()
                if end == "Yes":
                    print("With who?", end = '')
                    end = input("> ")
                    exit(0)
                else:
                    dead("Good boy")
            elif choice == "Dare":
                print("Type 'done when you're done")
                print("I dare you to cook 8 cups of rice")
                end = input()
                if end == 'done':
                    dead("Good job. You're doing well")
                else:
                    dead("You are a bitch man. You'll be killed soon")
            else:
                dead("Learn to read instruction man")
def interface():
    print("""
    In 1958, a game was invented by Ryan Hurdinson.
    The game is a terrifying game because a demon called Cthulhu used to
    possess the game. And anybody that plays it must not reject the game.
    The person must answer. The game name is Truth and Dear
    """)
    print("Do you want to play the game?")

    choice = input("> ")
    if choice == 'Yes':
        start()
    elif 'No' in choice:
        dead("You are a bitch, man. Why did you quit?")
    else:
        print("Reply with \"Yes\" or \"No\"")

def dead(win):
    print(win, ".Thank you!")
    exit(0)
def call():
    print("Hello. This is All-doing. An app that allows you to get volunteers and play game.")
    print("How may I help you. Do you want to play game or get volunteers?")
    choice = input("> ")
    if choice == "Play game":
        interface()
        start()
    elif choice == "Get volunteers":
        volunteers()
    else:
        print("You need to read the instruction")
call()
