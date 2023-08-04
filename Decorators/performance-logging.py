import logging

def function_logger(func):
    
    logging.basicConfig(level= logging.INFO, filename= "addition.log")
    
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        
        logging.info(f"{func.__name__}' ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}")
        
        return result
    
    return wrapper



@function_logger
def add_one(value):
    
    return value + 1

print(add_one(1))


    