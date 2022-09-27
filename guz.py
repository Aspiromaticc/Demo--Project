from sys import argv
script = argv
def print_one(f):
    print(f.read())
def rewind(f):
    print(f.seek(0))
def print_a_file(line_count, f):
    print(line_count, f.readline())
current_file = open(input())
print_one(current_file)
rewind(current_file)
current_line = 1
print_a_file(current_line, current_file)
current_line = current_line + 1
print_a_file(current_line, current_file)
current_line = current_line + 1
print_a_file(current_line, current_file)
current_line = current_line + 1
print_a_file(current_line, current_file)
