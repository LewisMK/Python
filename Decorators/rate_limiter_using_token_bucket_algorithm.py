import time


def token_bucket_rate_limited(tokens_per_second):
    
    interval = 1 / tokens_per_second
    max_tokens = tokens_per_second
    tokens = max_tokens
    last_refill = time.time()
    
    
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            
            nonlocal tokens, last_refill
            now = time.time()
            
            tokens_to_add = (now - last_refill) * tokens_per_second
            tokens = min(tokens + tokens_to_add, max_tokens)
            last_refill = now
            
            if tokens >= 1:
                
                tokens -= 1
                
                return func(*args, **kwargs)
            
            else:
                
                print("Rate limit exceeded. Try again later.")
                
        return wrapper
    
    return decorator

@token_bucket_rate_limited(tokens_per_second=1)
def limited_function():
    
    sum = 10 + 50
    
    print(sum)
  
for i in range(10):
    
    limited_function()
    time.sleep(0.5)
    
          