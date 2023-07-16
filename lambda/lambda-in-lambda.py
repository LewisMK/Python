#lambda functions cannot have multiple statements
#However, we can create two functions and call one from the other


list = [[2,3,4], [1,10,4,16], [3,8,4,18]]

#sort each sublist

sortList = lambda x: (sorted(i) for i in x)

#get the second largest element

secondLargest = lambda x, f: [y[len(y) -2] for y in f(x)]

res = secondLargest(list, sortList)

print(res)
