#lambda functions are useful when we use them as anonymous functions inside another function
#for example, we have a function that takes one argument, and that arg will be multiplied by an unknown number.
#we can use lambda to make the function always double the number we send in (argument)

def my_function(n):

    return lambda a: a * n

my_doubler = my_function(2) #holds the value lambda a: a * 2

my_times_five = my_function(5)

print(my_doubler(11)) #11 will now become the 'a' to complete the maths

print(my_times_five(11))

#lambda functions are good when an anonymous function is needed for a short period of time
