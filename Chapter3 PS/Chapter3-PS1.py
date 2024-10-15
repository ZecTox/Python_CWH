# Write a python program to display a user entered name followed by good afternoon using input() funtion.

name = input("Please enter your name: ")
print("Hello {}, Good Afternoon!".format(name))

#or we can also use fstring

print(f"Hello {name}, Good Afternoon!")