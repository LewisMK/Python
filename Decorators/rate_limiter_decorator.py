import time

def rate_limiter(limit_per_second):
    
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

            

@rate_limiter(limit_per_second=1)
def limited_function():
    
    sum = 10 + 50
    
    print(sum)
    

    
for i in range(5):
    
    limited_function()
