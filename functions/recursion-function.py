#recursion means that a defined function can call itself

#take care not to write a function that never terminates or uses too much memory and processing power

def tri_recursion(k):

    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")

tri_recursion(6)

#read more on recursion
