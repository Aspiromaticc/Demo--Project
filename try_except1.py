file = input("Enter file:")
handle = open(file, 'r')
form = dict()
for word in handle:
    words = word.split('')
    
