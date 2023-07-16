#Imagine you have many random numbers that have to be converted to int or float for storage/display.
#we can convert these numbers or display their types using the code below

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
