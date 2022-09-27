import string
fhand = open('volinfo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    print(words)
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts[word])
lst = list()
for key, val in list(counts.items()):
    lst.append(val, key)
lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)
