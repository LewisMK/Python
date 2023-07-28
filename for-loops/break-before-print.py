#putting the break statememt before the print statement

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print (x)

# this code will print apple only. It will not continue after seeing banana
