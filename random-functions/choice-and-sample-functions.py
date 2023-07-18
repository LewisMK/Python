# the randrange and randint functions can have repetitions
# we want to eliminate this outcome and improve randomness

# syntax choice(sequence)
# syntax sample(sequence, elements_to_choose)

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list)) #returns one int

print(sample(my_list, 5)) #returns five unique ints (non-repeating) in array

print(sample(my_list, 10)) # returns an array of unique ints, but all appear since elements_to_choose == input selection i.e. 10 is the number of list items
