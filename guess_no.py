from random import randint
def func():
    random_number = f"{randint(1, 5), (1,5)}"
    guess = input("GUESS NUMBER: ")
    guesses = 0
    while guess != random_number and guesses < 10:
        print("Oh! Shucks. Wrong")
        if guess > random_number:
            print("You are so close. Too high")
        if guess < random_number:
            print("You are so close. Too low")
        guesses += 1
        guess = input("GUESS NUMBER: ")
    if guess == random_number:
        print(f"The number is {random_number}")
        print(guess)
func()
