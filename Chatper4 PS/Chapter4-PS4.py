# write a program to sum a list with 4 numbers

#we make a random array

a = [1,2,4,5,6,7,8,77,8,8,22,2,5,6]

print(sum(a))

# or we can just use for loop,

sum = 0  # we have to initialize a variable to keep the count of sum
for i in range(len(a)):
    sum += a[i]
print(sum)