from sys import exit
def dead(win):
    print(win)
    exit(0)
def agile():
    print("Do you want to check out the details of the programmer")
    choice = input("> ")
    if choice == "Yes" or "yes":
        print("type name or age or height or town or school to check out his details")
        stuff = {'Name': 'Aderemi', 'Age': '20', 'Town': 'Apomu', 'School': 'Obafemi Awolowo University'}
        while True:
            choice = input("> ")
            if choice == "Name":
                print(stuff['Name'])
            if choice == "Age":
                print(stuff['Age'])
            if choice == "Town":
                print(stuff['Town'])
            if choice == "School":
                dead(stuff['School'])
    else:
        print("Please read instruction")
def dict():
    print("This is Aspiro's dictionary. It contains 10 words. You can checkout the words")
    print("Type the word")
    stuff = {'curtail': 'To reduce the duration of something', 'disparage': 'To discredit, undermine or ridicule someone or something',
    'consign': 'To dispose someone or something', 'homogeneous': 'Something of the same kind', 'disintegrate': 'To break something into pieces'}
    while True:
        choice = input("> ")
        if choice == "curtail":
            print(stuff['curtail'])
            print("Do you want to type another word")
            choice = input("> ")
            if choice == 'Yes':
                continue
            else:
                dead("You can checkout other words later")
        else:
            print("Type another word")
        if choice ==  "disparage":
            print(stuff['disparage'])
            print("Do you want to type another word?")
            choice = input("> ")
            if choice == 'Yes':
                continue
            else:
                dead("You can checkout other words later")
        else:
            print("Type another word")
        if choice == "consign":
            print(stuff['consign'])
            print("Do you want to type another word?")
            choice = input("> ")
            if choice == 'Yes':
                continue
            else:
                dead("You can checkout other words later")
        else:
            print("Type another word")
        if choice == "homogeneous":
            print(stuff['homogeneous'])
            print("Do you want to type another word?")
            choice = input("> ")
            if choice == 'Yes':
                continue
            else:
                dead("You can checkout other words later")
        else:
            print("Type another word")
        if choice == "disintegrate":
            dead(stuff['disintegrate'])
            print("Do you want to type another word?")
            choice = input("> ")
            if choice == 'Yes':
                continue
            else:
                dead("You can checkout other words later")
        else:
            print("Type another word")
dict()
