# SETS FROM w3school
#Captain each part of code needs to run seperately by removing the " comments " because the methods are conflicting. 
setA = {"agent1", "agent2", "agent3", "agent4", "agent5"}
setB = {"agent1", "agent2", "agent8", "agent7", "agent6"}
setC = {"agent3","agent4","agent5"}


# The add() method adds an element to the set.
'''setA.add("agent6")
print(setA)'''

# The copy() method copies the set.
'''setcopy = setA.copy()
print(setcopy)'''

# The difference() method returns a set that contains the difference between two sets.
'''setdiff = setA.difference(setB)
print(setdiff)'''

# The difference_update() method removes the items that exist in both sets. The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
'''diffup = setA.difference_update(setB)
print(setA)'''

#The discard() method removes the specified item from the set.
'''setA.discard("agent5")
print( setA)'''

#The intersection() method returns a set that contains the similarity between two or more sets.
'''inter = setA.intersection(setB)
print(inter)'''

#The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
'''setA.intersection_update(setB)
print(setA)'''

#The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
'''disjoint = setA.isdisjoint(setB)
print(disjoint)'''


#The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
'''subset = setC.issubset(setA)
print(subset)'''

#The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
'''superset = setA.issuperset(setC)
print(superset)'''

#The pop() method removes a random item from the set.
'''setC.pop()
print(setC)'''

#The remove() method removes the specified element from the set.
'''setB.remove("agent2")
print(setB)'''

#The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
'''symmetric_diff = setA.symmetric_difference(setB)
print(symmetric_diff)'''

#The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
'''setA.symmetric_difference_update(setB)
print(setA)'''

#The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
'''union = setA.union(setC)
print(union)'''

#The update() method updates the current set, by adding items from another set (or any other iterable).
'''setA.update(setB)
print(setA)'''