from functools import lru_cache


@lru_cache(maxsize=None) 
def fib(n):
    
    if n <= 1:
        
        return n
    else:
        
        return fib(n-1) + fib(n-2)
    
print(fib(10))
print(fib(50))
print(fib(100))
print(fib(500))



