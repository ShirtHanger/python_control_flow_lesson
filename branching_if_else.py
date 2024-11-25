""" Indentation

Indentation is MANDATORY in python."""

""" BRANCHING """

""" If-Else """

# Single path if statement

floor = "sticky"
walls = "clean"

# notice the colon ':' after the conditional expression
# it indicates the start of the if block
if floor == "sticky":
    print("Clean the floor! It's sticky!")
    # this is where you would add more lines of code related to the condition
    # each line must be indented to be part of the 'if' block

# unindented code indicates that we have returned to normal code execution
print("This will always print, it's not inside of an if block!")

# parentheses are not required around the conditional expression
if walls == "sticky":
    print("Clean the walls! They're sticky!")

# Dual path if...else statement:

val = 3

# if path
if val == 1:
    print('val is one')
# else path
else:
    print('val is not one')
    # prints: val is not one
    # since val is not 1, the else path is taken

# Multi-path if...elif...else statement:

val = 3

if val == 1:
    print('val is one')
elif val == 2:
    print('val is two')
elif val == 3:
    print('val is three')
    # prints: val is three
    # since val is 3, this elif path is taken
else:
    print('not one, two, or three')

# else is always optional, just like it is in JavaScript


color = input('Enter "green", "yellow", "red": ').lower()
print(f'{color} light!')
if color == 'green':
    print('Go!')
elif color == 'yellow':
    print('Slow down!')
elif color == 'red':
    print('Stop!')
else:
    print(f'...')
    print(f'Bogus! What the hell is {color}??')