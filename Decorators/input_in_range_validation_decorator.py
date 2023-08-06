def validate_input_range(min, max):
    
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            
            for arg in args:
                
                if not isinstance (arg, (int, float)) or arg < min or arg > max:
                   
                   raise ValueError(f"The value must be between {min} and {max}.")
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

 
@validate_input_range(min = 10, max = 100)
def calculate_percentage(value, total):
    
    return (value / total) * 100

try: 
    
    value = float(input("Enter a value between 10 and 100: "))
    total = float(input("Enter the total value: "))
    
    result = calculate_percentage(value, total)
    
    print(f"Result: {result} percent")
    
except ValueError as e:
    
    print("Error: ", e) 
    
    