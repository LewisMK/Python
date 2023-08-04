# this program logs a function's parameters and the output using a decorator
# logging helps to debug and understand program logic

import logging

def function_logger(func):
    
    logging.basicConfig(level= logging.INFO, filename= "addition.log")    # open the addition.log file to see the log output
    
    def wrapper(*args, **kwargs):       # *args and **kwargs means that the function takes any number of args and kwargs. 
        
        result = func(*args, **kwargs)
        
        logging.info(f"{func.__name__}' ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}")
        
        return result
    
    return wrapper



@function_logger                        # calling the logging function before executing the real function
def add_one(value):
    
    return value + 1

print(add_one(1))                       # output is 2


    
