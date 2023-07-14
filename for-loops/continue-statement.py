#continue statement stops the current loop iteration and continues with the next one

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)

#this program will print apple and cherry and leave out banana
