x = 5
try:
    print(yo)
except NameError:
    print("Variable X is not defined")
except:
    print("Something else is wrong")

try:
    print("Hello")
except:
    print("Something is wrong")
else:
    print("Nothing is wrong")

try:
    print(u)
except:
    print("Something is wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("volinfo.txt")
    try:
        f.write("We are money launderers")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong while opening the file")
