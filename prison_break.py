from sys import exit
from random import randint
from textwrap import dedent
def Scene1():
    print("PRISON BREAK: The facet of loyalty")
    print("Your brother is wrongly accused of a felony. And his sentence is death by hanging. However, he will be executed  in the next few days. ")
    print("But only you could save him with the great ability you possess. ")
    print("You need to get through some tasks before you can break into the prison. This mission is extremely difficult and you could lose your life in the process.")
    print("Are you willing to go far for your brother? Are you willing to take the risk?")
    choice = input("> ")
    if choice == "Yes":
        Scene_2()
    else:
        dead("You are a bitch. So you'll let your brother's ass get kicked")

def Scene_2():
    print("Welcome to the first level to the first challenge of your pursuit")
    print("The plan you devised on a blueprint was stolen by some gangs. As you get to those gang's house, they didn't allow you pass through them. And you are still holding your gun. ")
    choice = input("> ")
    if choice == "Shoot":
        print("Oh! Good of you boy! Didn't know you are good at getting ass kicked")
        print("All the boys are dead but you are really hurt. You need to go to hospital after recovering your blueprint.")
        print("The blueprint is locked in a big box, and unfortunately, there's no way you can access the box without one of their members telling you, or guessing the number")
        print("One of their members is alive, but he is in a state of coma. You can save him in order to get the pin of the box, but he might report you to the force after getting healed")
        print("Do you want to save him or guess the number")
        choice = input("> ")
        if choice == "Guess the number":
            print("You have 5 attempts to guess the number. You are dead, if you don't guess the number correctly")
            code = f"{randint(1, 3), randint(1, 3), randint(1, 3)}"
            guess = input("[keypad]> ")
            guesses = 0
            while code != guess and guesses < 4:
                print("OH! SUCKS")
                guesses += 1
                guess = input("[keypad]> ")
                if guess == code:
                    print("Good")
        elif  choice == "Save him":
            print("The guy is saved now. And the key is 345. But the has hit the force on. And the forces have surrounded the hospital, waiting for you to get out")
            print("You need to find a way to get out of the prison")


Scene_2()
