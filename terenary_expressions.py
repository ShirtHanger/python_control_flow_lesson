""" Ternary expressions

Python does not have a dedicated ternary operator. 
Instead, Python uses a modified syntax of if/else, which results in a ternary
expression instead of a control flow construct.

The Python ternary expression equivalent to the JavaScript example above is:"""

time_of_day = 9
morning = True if time_of_day < 12 else False
print(morning)
# prints: True
