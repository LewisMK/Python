#range() function specifies how many times to loop through the code
#it has a default value of 0 but one can specify other values

for x in range(2,6):
    print(x)
print("\n")

#the above function prints x four times because we don't reach to 6

#we can also increment the step by more than one by adding the step param

for x in range(2, 30, 3):
    print(x)
