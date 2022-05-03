#Implement methods for dictionary data structures
info = {
    "name":"divyansh",
    "age":19,
    "course":"PYTHON"
}

#Print dictionary
print(info)

#Returns a copy of the dictionary
copied = info.copy()
print(copied)

#Returns a dictionary with the specified keys and value
keyss = ('key1', 'key2', 'key3')
common_values = "value"
thisdict = dict.fromkeys(keyss, common_values)
print(thisdict)

#Returns the value of the specified key
age = info.get("age")
print(age)

#Returns a list containing a tuple for each key value pair
items = info.items()
print(items)

#Returns a list containing the dictionary's keys
keys = info.keys()
print(keys)

#Removes the element with the specified key
info.pop("age")
print(info)

#Removes the last inserted key-value pair
info.popitem()
print(info)

#Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
x = info.setdefault("age",19)
print(x)


#Updates the dictionary with the specified key-value pairs
info.update({"course":"web development"})
print(info)

#Returns a list of all the values in the dictionary
vals = info.values()
print(vals)

#Removes all the elements from the dictionary
info.clear()
print(info)