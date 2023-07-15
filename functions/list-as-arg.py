#arguments can have many data types
#when we send a list to a function, it is treated as a list inside the function

def my_function(food):

    for x in food:
        print(x)

    print("\n")

fruits = ["apple", "banana", "cherry"]

drinks = ["milk", "juice", "water"]

my_function(fruits)
my_function(drinks)
