# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(-1,99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print("\nlength of x after all this manipulation:",len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
xX1000 = [1000 * x_i for x_i in x]
print("\nMultiplying x by 1000 changes the values to:\n", xX1000, sep='')