from functools import reduce
l = [3,4,1,5]
x = list(map(lambda x:str(x), l))
c = reduce(lambda x,y:x+y,x)
print(c)

