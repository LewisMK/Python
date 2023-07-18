#we can also have random integers
#we use randrange and randint functions

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 10), end =' ')
print(randrange(0, 100, 5), end=' ') #increments of 5
print(randint(0, 100))

# however, these methods are weak in that they can repeat a number even if the number of repetitions is not larger than the width range. i.e.
# if we repeat the function 9 or 10 times in the range (0, 10) we will likely have similar numbers
