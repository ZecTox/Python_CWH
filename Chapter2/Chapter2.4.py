#Learning about inputs in python

a = input("enter number 1: ")
b = input("enter number 2: ")

print("Number a is: ", a)
print("Number b is: ", b)
print(a+b)

#currently the outputs we are getting are in strings, if we want them to give us outputs in integers, we have to do this..

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
print("Number a is: ", a)
print("Number b is: ", b)
print(a+b)