#we can have a default param to be used when nothing is passed in the function call

def my_function(name = "Lewis"):

    print("My name is " + name)

my_function("John")
my_function("Doe")
my_function()
my_function("JD")

#line 9 will return My name is Lewis. 
