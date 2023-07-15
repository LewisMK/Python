#used when we do not the number of keyword args that will be passed to my_function
#we add two ** before the param name in function definition
#this way, the function will receive a dictionary of args

def my_function(**cars):

    print("The last car in the list is " + cars["lcar"])

my_function(fcar = "Benz", lcar = "Volvo", mcar = "Audi")

#here, instead of using the index like in arb arguments, we use the name (key) of the target value
