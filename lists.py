from re import sub


subjects = ['python','webtech','java']
marks = [99,100,90]

'''
#Removes all the elements from the list
subjects.clear()
print(subjects)'''

#Returns a copy of the list
subjects2 =subjects.copy()
print(subjects2)

#Adds an element at the end of the list
subjects.append("c++")
print(subjects)

#Returns the number of elements with the specified value
count = subjects.count("java")
print(count)

#Add the elements of a list (or any iterable), to the end of the current list
subjects.extend(marks)
print(subjects)


#Returns the index of the first element with the specified value
index = subjects.index("java")
print(index)

#Adds an element at the specified position
marks.insert(0,89)
print(marks)

#Removes the element at the specified position
marks.pop()
print(marks)

#Removes the first item with the specified value
subjects.remove("c++")
print(subjects)

#Reverses the order of the list
subjects2.reverse()
print(subjects2)

#Sorts the list
subjects.sort()
marks.sort()
print(subjects)
print(marks)
