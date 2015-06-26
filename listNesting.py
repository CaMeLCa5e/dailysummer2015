lists = [[]]*10
print lists
 
lists[0].append(3)
print lists

lists[0].pop()
print lists

list2 = [[] for i in range(3)]
list2[0].append(3)
list2[1].append(5)
list2[2].append(7)
print list2