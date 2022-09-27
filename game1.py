from sys import exit
def dead(why):
    print(why, "Good job!")
    exit(0)
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
        print("Respond with \"Yes\" or \"No\"")
        return interface()
interface()
