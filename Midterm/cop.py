#show the difference between shallow and deep copies, and show how the empty slice works

from copy import deepcopy

#shallow
original_list = [[1,2,3],["a","b","c"]]
shallow_list = list(original_list)
shallow_list[0][0] = -1
#print(original_list)
#[[-1, 2, 3], ['a', 'b', 'c']]
#print(shallow_list)
#[[-1, 2, 3], ['a', 'b', 'c']]

#deep
original_list = [[1,2,3],["a","b","c"]]
deep_list = deepcopy(original_list)
deep_list[0][0] = -1
#print(original_list)
#[[1, 2, 3], ['a', 'b', 'c']]
#print(deep_list)
#[[-1, 2, 3], ['a', 'b', 'c']]