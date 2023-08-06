def validate_positive_integers(func):
    
    def wrapper(*args, **kwargs):
        
        for arg in args:
            
            if not isinstance(arg, int) or arg <= 0:
                
                raise ValueError("All values must be positive integers")
            
        return func(*args, **kwargs)
    
    return wrapper

@validate_positive_integers
def multiply(a, b):
    
    return a * b

try:
    
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    result = multiply(a, b)
    
    print("Result: ", result)
    
except ValueError as e:
    
    print("Error: ", e)
    
    