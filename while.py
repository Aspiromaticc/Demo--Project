number = []
i = 0
x = 6
while i < x:
    print(f"We are running through {i}")
    number.append(i)
    i += 1
    print("The number is", number)
    print(f"They told you to show {i}")
    i += 2
    print("The number is", number)
    print(f"They told you to show {i}")
print("The numbers:")
for num in number:
    print(num)                                                                                                                                                                                                                                       
