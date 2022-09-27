from sys import argv
def print_one(f):
    print(f.read())
def rewind(f):
    print(f.seek(0))
def print_in_line(line_count, f):
    print(line_count, f.readline())
current_file = open(input("> "))
print_one(current_file)
rewind(current_file)
current_line = 1
print_in_line(current_line, current_file)
current_line += 1
print_in_line(current_line, current_file)
current_line += 2
print_in_line(current_line, current_file)
