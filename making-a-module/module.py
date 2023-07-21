#when you run a file directly, its __name__ variable is set to __main__
#when a file is imported as a module, its __name__ variable is set to the file's name (without .py)

#we can use this to know the context in which the code is being activated

'''if __name__ == "__main__":

    print(__name__)
    print("This module is running directly.")

    else:
    print(__name__)
    print("This module is imported in another file.")
'''

#we can use this variable to test whether functions in the module are working properly.

#if you modify the functions, you can run the module to make sure it's okay

#when you import the module for another purpose, these tests will not be included in the code

#NOW A REAL MODULE

#!/usr/bin/env python3

# module.py - an example of a Python module

__counter = 0 #the dashes tell module users to not change the value

def suml(the_list):

    global __counter
    __counter += 1
    the_sum = 0

    for element in the_list:
        the_sum += element

    return the_sum

def prodl(the_list):

    global __counter
    __counter += 1
    prod = 1

    for element in the_list:
        prod *= element

    return prod

if __name__ == "__main__":

    print("I prefer to be a module, but I can run some tests for you.")

    my_list = [i+1 for i in range(5)]

    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
