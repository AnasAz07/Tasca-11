from functools import reduce
l = [3,4,1,5]
x = reduce(lambda a,b: a.join(b),l)
print(x)

