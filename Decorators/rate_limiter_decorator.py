import time

def rate_limiter(limit_per_second):     # Decorator function and logic
    
    min_interval = 1 / limit_per_second
    last_called = 0
    
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            
            nonlocal last_called
            
            elapsed = time.time() - last_called
            
            if elapsed < min_interval:
                
                sleep_time = min_interval - elapsed
                
                time.sleep(sleep_time)
            
            last_called = time.time()
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

            
# Wrapping our main function with the decorator
@rate_limiter(limit_per_second=1)       # the value of limit_per_second can be changed based on needs.
def limited_function():
    
    sum = 10 + 50
    
    print(sum)
    

# Testing the rate limit for the function   
for i in range(5):
    
    limited_function()
