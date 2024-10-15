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


#------- some extra string functions -------#

# 7. string.lower() = Coverts all the characters in the string to lowercase

string = "HELLO World"
print(string.lower())

# 8. string.upper() = Converts all the characters in the string to uppercase

string = "hello world"
print(string.upper())

# 9. string.strip() = Removes leading and trailing whitespaces from a string.

string = "      Tejas       "
print(string.strip())

# 10. string.split() = Splits a string into a list based on a specific delimiter (space by default)

string = "Tejas is a good boy"
print(string.split())

# 11. " ".join(string) = Join elements of a list into a single string with a specified seperator.

array_of_strings = ['Tejas', 'is', 'a', 'good', 'boy']
print(" ".join(array_of_strings))

# 12. string.startswith() = Checks if a string starts with a specified substring

text = "Tejas"
print(text.startswith("Te"))

# 13. string.format() = Formats string using placeholders.

name = "Tejas"
greeting = "Hello, {}".format(name)
print(greeting)

# 14. string.title() = Capitalizes the first character of every word in the string

text = "hello world"
print(text.title())

# 15. string.isdigit() = Checks if all the character in the string are digits  or not 

string = "19735382"
print(string.isdigit()) #if true, outputs as true and if not then prints false

# 16. string.isalpha() = Checks if all the characters in the string are alphabets or not

string = "helloworld"
print(string.isalpha())

# 17. string.isalnum() = Checks if the string is alphanumeric or not

string = "Tejas123"
print(string.isalnum())

# 18. string.swapcase() = Swaps the case of all characters in the string

string = "Hello World"
print(string.swapcase()) #output - hELLO wORLD