# this program demonstrates the use of decorators for caching
# the fib sequence can take a lot of time when using large numbers as args
# thus, the lru_cache decorator is used to improve processing speed dramatically

from functools import lru_cache      # import lru_cache from in-built functools


@lru_cache(maxsize=None)             # use the lru_cache function as a decorator. The maxsize specifies the number of saved(cached) instances before deletion
def fib(n):
    
    if n <= 1:
        
        return n
    else:
        
        return fib(n-1) + fib(n-2)
    
print(fib(10))
print(fib(50))
print(fib(100))
print(fib(500))       

# all functions take less than one second to complete
# without lru_cache, it would take forever


