# TUPLES IN PYTHON

# A tuple is a immutable data type in python

a = () # empty tuple
a = (1,) #tuple with only one element needs to have a comma in it.
a = (1,7,2) #tuple with more than one elements
print(type(a))

# Now we will look for some tuple methods.

# 1. count(value) = returns the number of times a specified value appears in the tuple

a = (1,2,3,4,5,6,7,8,9)
count_of_tuple = a.count(1)
print(count_of_tuple)

# 2. index(value) = Returns the index of the first occurence of the specified value.
a = (9,3,6,1,4,7,8,5)
index_of_tuple = a.index(5)
print(index_of_tuple)

#Operations with tuples
# 3. Concatenation = you can combine two or more tuples using the + operator

tuple1 = (1,2)
tuple2 = (3,4)
tuple3 = tuple1 + tuple2
print(tuple3)

# 4. Repetition = We can repeat a tuple using multiple(*) sign and multiply it.

new_tuple = (1,2,3)
multiple_tuple = new_tuple * 5
print(multiple_tuple)

# 5. Slicing = You can access a subset of the tuple using slicing

my_tuple = (1,2,3,4,5,6,7,8,9)
slicing_tuple = my_tuple[1:4]
print(slicing_tuple)

# 6. Length = you can get the number of elements in a tuple using len()

new_tuple1 = (1,2,3,4,5,6,7,8,9,0)
length_tuple = len(new_tuple1)
print(length_tuple)

# 7. Packing and Unpacking = Creating a tuple by assigning multiple values to a single variable

#packing
my_tuple = (1,2,3)
#unpacking
a,b,c = my_tuple

print(a,b,c)

# 8. Nested Loops = tuples can contain other tuples, allowing for complex data strucures.

nested_tuple = (1, (1,2), (3,4))

# 9. Type checking = you can check if a variable is a tuple using isinstance()

my_tuple = (1,2,3)
is_tuple = isinstance(my_tuple, tuple)
print(is_tuple)


# Imp notes on Tuple
# - tuples are generally faster than lists for iteration  due to their mobility 
# - they can be used as key as dictionaries because they are hashable(as long as they contain only hashable types)
