# the else keyword specifies a block of code to be executed when the loop is finished

for x in range(6): # we don't have to include the zero
    print(x)
else:
    print("Finished successfully")
print("\n")

#the else block is not executed if the loop is stopped by a break statement

for x in range(6):
    if x == 3: break
    print(x)

# the above code will only print values 1 and 2. 
else:
    print("I will not be printed.")
