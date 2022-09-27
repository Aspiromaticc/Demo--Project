from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file).read()
print(f"The input is {len(in_file)} bytes long")
print(f"Does the output exists? {exists(to_file)}")
input()
out_file = open(to_file, 'r+')
out_file.write(to_file)
