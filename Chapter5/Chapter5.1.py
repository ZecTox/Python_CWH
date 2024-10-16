# Chapter 5 - Sets and Dictionaries

# DICTIONARY - collection of key value pairs

a = { "key" : "value",
     "tejas" :"code",
     "marks" : "100",
      "list" : [1,2,3]
    }

print(a["list"]) #this will prin the value that is paired with list in the dictionary

## PROPERTIES of Dictionary

    # 1. It is unordered
    # 2. It is mutable
    # 3. It is indexed
    # 4. Cannot contain duplicate keys
    
# Dictionary Methods..

# Comsider the following dictionary:

a = {"name" : "tejas",
     "from" : "India",
     "marks" : [92,98,96]
    }

# 1. a.items() = returns the list of (key, value) tuples.

print(a.items())

# 2. a.keys() = returns a list containing dictionaries keys

print(a.keys())

# 3. a.values() = returns a list containing dicitonaries values

print(a.values())

# 4. a.update({"friends" : }) = updates the dicitionary with supplied key-value pairs

a.update({"from" : "Japan"}) # as we know dictionary is mutable, hence changes or updates can be done.
#also if we gave a new value to it. then it adds it in the dictionary
print(a)

# 5. a.get(key) = returns the value of the specified keys (if key is given "name" then value is returned as "Tejas")

print(a.get("name"))
print(a.get("college")) #there is no key by name "college" so it will return none as output

# SOME MORE METHODS

# 6. a.pop(key, default = none ) = removes the specified key and returns its value, if the key is not in dictionary it will return whatever was given in default or if default is also empty then KeyError is returned.

print(a.pop("marks"))

# 7. a.popitem() = removes and returns the last inserted key-value pair as tuple. Raises a keyerror if the dictionary is empty

hehe = a.popitem()
print(hehe) #it will print the from key as we have popped the marks key before it.

# 8. a.clear() = removes all the items from dictionary

# a.clear()
# print(a)

# 9. a.copy() = returns a shallow copy of the dictionary

copy_dict = a.copy()
print(copy_dict)

# 10. a.fromkeys(iterable, value=none) = creates a new dictionary with keys from the given table iterable and values set to the specified value (default is none)

new_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print(new_dict)


