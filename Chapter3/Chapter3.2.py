#STRING FUNCTIONS

# 1. len() function - This function returns us the length of the string

a = "Tejas"
b = "Tejas is a good boy"

print(len(a))
print(len(b))

# 2. string.endswith() -this funciton tells whether the variable string ends with the given string in it or not. if the string is "Tejas" and "as" is given in the funtion. it will return true. 

a = "Tejas"
print(a.endswith("as")) 

# 3. string.count() - It counts the total number of occurrences of any character. This function tells us how many times the number of strings are available that are given in it. 

string = "Tejas is a good boy"
print(string.count("o"))

# 4. string.capitalize() - This function capitalizes the first character of the string

string = "hello world!"
print(string.capitalize())

# 5. string.find(word) - This function friends a word and returns the index of first occurence of that word in the string.

string = "hello world"
print(string.find("world"))

# 6. string.replace(old word, new word) - This function replace the old word with new word in the entire string.
string = "Tejas is learning C++"
print(string.replace("C++", "Python"))