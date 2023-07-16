#we want to create a list using lambda and for loop

list = [lambda arg=x: arg * 10 for x in range(1,5)]

#this function will iterate with x becoming the current item in the iteration

for item in list:
    print(item()) #here we call function with the default value already given before.
