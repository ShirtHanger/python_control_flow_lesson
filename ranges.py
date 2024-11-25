""" 
Purpose of ranges

Python ranges are a sequence type, similar to a list.

An immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.

"""

# Ranges can only be created by invoking the range() class:

for num in range(5):
    print(num)
    # prints the integers: 0, 1, 2, 3, 4
    # Oddly, does not include the number 5
    
# You can pass a start and step to get more complex

# range(start, input, step)

# Start: The starting integer
# Step: The amount added to current value for each step

for even in range(4, 12, 2):
    print(even)
    # prints the integers: 4, 6, 8, 10

# You can create a list with ranges!

nums = list(range(10))
print(nums)
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# And count downward!

for num in range(5, 0, -1):
    print(num)
    # prints the integers: 5, 4, 3, 2, 1

# Learn more https://docs.python.org/3/tutorial/controlflow.html#the-range-function