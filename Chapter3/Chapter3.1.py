#Chapter 3 - Strings

# String is a data type in Python, it is a sequence of characters enclosed in quotes.
# We can primarily write a string in three ways

a = 'tejas' #single quoted string
b = "tejas" #double quoted string 
c = '''tejas''' #triple quoted string, used for multiple lines of string


# String Slicing
## A string in python can be sliced for getting a part of the strings 
## Strings are immutable, if any changes are needed, need to create new string

#The index of a string starts from 0 to (length-1) in python. In order to slice a string. We use the following syntax.

name = "Tejas"
    # sl = name[index_start:index_end]
    #                /           \
    #        first index       last index
    #         included          included   
    
#  sl[0:3] returns "tej" -----> Characters from 0 to 3 (3 is not included)
#  sl[1:3] returns "ej"  -----> Characters from 1 to 3 (again 3 is not included)

print(name[0:3]) #it will print the letters from thestring from 0 to 2 (as we know 3 will not be included)

print(name[-4:-1]) #this thing will work same as print(name[1:4])

# print(name[-1:-4])  # this wont work as it doesnt define the rules of slicing. 

print(name[:4])
print(name[2:])
print(name[2:3])

# SLICING WITH SKIP VALUE
## we can provide the skip value as a part ofour slice like this

word = "amazing"
word[1:6:2]

a = "0123456789"
print(a[1:6:3])

b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:9:4])
print(b[0:10:1])