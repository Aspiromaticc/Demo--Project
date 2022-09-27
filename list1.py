star = ["Joseph", "Samuel", "Deji", "Olatoke", "Charles"]
print(len(star))
print(star)
print(star[2])
for x in star:
    print(x)
print(star[-2])
print(star[-4])
print(star[2:5])
if "Joseph" not in star:
    print("Yes, it is")
try:
    print("We are money launderers")
except:
    if "Joseph" not in star:
        print("And heartbreakers, right?")
star[1] = "Aderemi"
print(star)
star.append("Oyebola")
list = ["Jason", "Richard", "Deborah", "Akinsola"]
print(star)
star[1:2] = "David", "Chinoso", "Jimmy"
print(star)
star.insert(2, "Wench")
print(star)
star.insert(-1, "Ronaldo")
print(star)
print(star[-1])
star.extend(list)
print(star)
star.append(list)
print(star)
stuple = ("Kane", "Jason")
star.extend(stuple)
print(star)
star.remove(list)
print(star)
star.remove("Jason")
print(star)
star.remove("Kane")
print(star)
star.pop(-1)
print(star)
star.pop()
print(star)
del star[0]
print(star)
del star[1]
print(star)
latecomers2 = [x for x in star if x != "Oyebola"]
print(latecomers2)
latecomers  = []
for x in star:
    if x != "Oyebola" "Olatoke":
        latecomers.append(x)
print(latecomers)
for i in range(len(star)):
    print(i)
i = 0
while i < len(star):
    print(star[i])
    i += 1
[print(x) for x in star]
latecomers = []
for x in star:
    if "b" in x:
        latecomers.append(x)
print(latecomers)
latecomers2 = [x for x in star if "b" in x]
print(latecomers2)
j = [x for x in star]
print(j)
j = [x for x in range(len(star))]
print(j)
j = [x for x in range(len(star)) if x < 5]
print(j)
j = []
for x in range(len(star)):
    if x < 5:
        j.append(x)
print(j)
j = [x.lower() for x in star]
print(j)
j = [free if free != "Oyebola" else "Jughead" for free in star]
print(j)
star.sort()
print(star)
star.sort(reverse = True)
print(star)
def my_key(n):
    return n + "Winner"
star.sort(key = my_key)
print(star)
j = [x.lower() for x in star if 'a' in x]
star.extend(j)
star.sort()
print(star)
star.sort(key = str.upper)
print(star)
j = star.copy()
print(j)
j = list(star)
print(j)
