#do list, set, dictionary comprehensions

ourlist = ["byu","uvu","weber","usu"]
newlist = [x for x in ourlist if "u" in x]
print(newlist)
#['byu', 'uvu', 'usu']

ourdict = {x: x*2 for x in [1,2,3,4,5]}
print(ourdict)
#{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}