from random import random, seed

seed()

# seed(2) doing this will set the seed to 2. Therefore, we will remove all randomness
# seed() only uses the current time. Hence, all values will be random even when program is run twice.

for i in range(5):
    print(random())
