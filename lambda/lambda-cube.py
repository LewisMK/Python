def cube(y):

    return y*y*y

lambda_cube = lambda y: y*y*y

#using defined function

print("Using function with 'def' keyword, cube:", cube(5))

#using the lambda function

print("Using lambda function, cube:", lambda_cube(5))


# here we are using two different functions for same result. Note how the lambda function is short and ideal for simple functions which return one value.
