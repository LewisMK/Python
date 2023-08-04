# this program logs a function's parameters and the output using a decorator
# logging helps to debug and understand program logic

import logging
import time

def function_logger(func):
    
    logging.basicConfig(level= logging.INFO, filename= "addition.log")    # open the addition.log file to see the log output
    
    def wrapper(*args, **kwargs):       # *args and **kwargs means that the function takes any number of args and kwargs. 
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        logging.info(f"{func.__name__} ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}. Total execution time: {execution_time: .6f} seconds")
        
        return result
    
    return wrapper



@function_logger                        # calling the logging function before executing the real function
def add_one(value):
    
    return value + 1

<<<<<<< HEAD
print(add_one(10))
=======
print(add_one(1))                       # output is 2
>>>>>>> 8c4f09c58d1c26c72ae8df6fc883effbad37cdc3


    
