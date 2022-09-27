from sys import argv
script, filename, filename_2 = argv
abb = open(filename)
print(abb.read())
ddd = open(filename_2)
print(ddd.read())
