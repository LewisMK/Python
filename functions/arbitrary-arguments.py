def my_function(*cars):

    print("The most expensive car is " + cars[2])

my_function("Benz", "Audi", "Volvo")

#the * symbol is used when we do not know how many args will be passed into the function.
# the function is instantiated with a tuple of args and they can be accessed inside the function using indexes
