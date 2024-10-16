# Chapter 4 - Lists and Tuples
# We will study Lists now

# Python lists are containers to store a set of values of any data type.
friends = ["apple", "akash", "rohan", 7, "false"]

# It can store values of any datatype.

# LIST INDEXING
# A list can be indexed just like a string.
print(friends[0])  # Output: apple
friends[0] = "Grapes"  # Lists are mutable; we can change their contents.
print(friends[0])  # Output: Grapes
print(friends[1:4])  # Output: ['akash', 'rohan', 7]

listname = [1, 8, 7, 2, 21, 15]

# LIST Methods
# 1. listname.sort() - sorts the list in ascending order.
listname.sort()  # This modifies listname in place.
print(listname)  # Output: [1, 2, 7, 8, 15, 21]

# 2. listname.reverse() - reverses the list.
listname.reverse()  # This modifies listname in place.
print(listname)  # Output: [21, 15, 8, 7, 2, 1]

# 3. listname.append() - adds the given item to the end of the list.
listname.append(7)  # This modifies listname in place.
print(listname)  # Output: [21, 15, 8, 7, 2, 1, 7]

# 4. listname.insert(a, b) - inserts b at index a.
listname.insert(2, 99)  # This modifies listname in place.
print(listname)  # Output: [21, 15, 99, 8, 7, 2, 1, 7]

# 5. listname.pop() - removes and returns the last indexed element.
popped_item1 = listname.pop()  # Removes and returns the last item.
print(popped_item1)  # Output: 7 (the last item)
print(listname)  # Output: [21, 15, 99, 8, 7, 2, 1]

popped_item2 = listname.pop(2)  # Removes and returns the item at index 2.
print(popped_item2)  # Output: 99
print(listname)  # Output: [21, 15, 8, 7, 2, 1]

# 6. listname.remove(21) - removes the first occurrence of the specified value.
listname.remove(21)  # This modifies listname in place.
print(listname)  # Output: [15, 8, 7, 2, 1]