#the break statement stops the for loop before it is done

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

    if x == "banana":
        break
        
# the output will be apple and banana. Cherry will not be printed.
