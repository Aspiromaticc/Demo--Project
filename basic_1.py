
from sys import argv
script, user = argv
print(f"{user}, I would like to ask you a few questions. I am the {script}")
print("Do you like me?")
print(f"Where do you live {user}?")
a = input()
print(f"{user}, What's your age?")
b = input()
print(f"What kind of computer do you have {user}?")
c = input()
print(f"""
Alright, you said you live in Ife {a}, and you age is {b}. And you use
a {c} laptop
""")
