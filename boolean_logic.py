""" 
Python has two Boolean values, True and False
Always capitalized

EQUALITY OPERATORS

== - equal to
!= - not equal to

"""

print(7 == 7)
# prints: True
# 7 is equal to 7

print(7 == "7")
# prints: False 
# 7 is an integer, and "7" is a string

print(7 != 7)
# prints: False
# 7 is equal to 7

print(7 != "7")
# prints: True 
# 7 is an integer, and "7" is a string; therefore, they cannot be equal

""" COMPARISON OPERATORS
< - less than
> - greater than
<= - less than or equal
>= - greater than or equal
"""

print(8 > 8)
# prints: False 
# 8 is not greater than 8

print(8 >= 8)
# prints: True 
# 8 is greater than or equal to 8 (equal)

print(8 < 8)
# prints: False 
# 8 is not less than 8

""" LOGICAL OPERATORS

Logical operators we used in JavaScript work the same way in Python, except Python uses English words instead of symbols:

or is the same as ||
and is the same as &&

or - Returns the first truthy operand, or the last operand.
and - Returns the first falsy operand, or the last operand.
"""

# or

print(True or False)
# prints: True

print(False or True)
# prints: True

print(False or False)
# prints: False

print('hello' or 0)
# prints: 'hello'

print(0 or 'hello')
# prints: 'hello'

print('hello' or 'tacos')
# prints: 'hello'

# and

print(True and False)
# prints: False

print(False and True)
# prints: False

print('hello' and 0)
# prints: 0

print(0 and 'hello')
# prints: 0

print('hello' and 'tacos')
# prints: 'tacos'

# More than two conditions can be evaluated at the same time, like so

# or

print(True or True or True)
# prints: True

print(True or True or False)
# prints: True

# and

print(True and True and True)
# prints: True

print(True and True and False)
# prints: False

# And you can mix OR and AND

print(False or True and True)
# prints: True

""" The 'not' operator

Just like the not operator in JavaScript (!), the not operator in Python flips a 
truthy expression to a boolean value of False, 
and a falsy expression to a boolean value of True.
"""

print(not False)
# prints: True

print(not 'hello')
# prints: False
