#show how lambda functions work and reduce()

func = lambda : print("Hello world!")
func()
#Hello world!

addnums = lambda x, y : x + y
print(addnums(2,3))
#5

from functools import reduce

ourlist = [1,2,3]
print(reduce(lambda a, b : a+b, ourlist))
#6 (sum)
print(reduce(lambda a, b : a if a>b else b, ourlist))
#3 (max)