import logging
import time

def function_logger(func):
    
    logging.basicConfig(level= logging.INFO, filename= "addition.log")
    
    def wrapper(*args, **kwargs):
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        logging.info(f"{func.__name__} ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}. Total execution time: {execution_time: .6f} seconds")
        
        return result
    
    return wrapper



@function_logger
def add_one(value):
    
    return value + 1

print(add_one(10))


    