from math import e, exp, log

print(pow(e, 1) == exp(log(e)))

print(pow(2, 2) == exp(2 * log(2)))

print(log(e, e) == exp(0))

# e = value close to Euler's number
#exp(x) is e power x
# log(x)
# log(x, b) = log x to base b
# log10(x) = decimal log of x (more precise than log(x, 10))
# log2(x) = binary log of x (more precise tahn log(x, 2))

# pow(x, y) = x power y. this is a built-in function (no import)
