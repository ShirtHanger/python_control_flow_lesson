""" FOR LOOP """

# Much simpler and more rational in python

names = ["Emily", "Jack", "Sophia", "Ethan"]

for name in names:
    print(name)

""" WHILE LOOP """

num = 1

while num <= 10:
    print(num)
    # prints the numbers 1 through 10
    num += 1

# while loops are great for when you don’t know how many times you will need to iterate - 
# for example if you want to continue getting input from a user until a specific condition is met.
# Beware of infinite loops!

""" The break and continue statements

Like in JavaScript, the 'break' statement in Python is used to exit for and while loops immediately.

the 'continue' statement will end the current iteration of a loop and continue to the next iteration as long as 
* the condition of the loop is still truthy
* there are still items to iterate through.
"""

things = ["computer", "g-g-ghost", "chair", "spider", "desk"]

for thing in things:
    if thing == "g-g-ghost":
        print("Oh, that's just my ghost friend, carry on.")
        continue
    elif thing == "spider":
        print("Nope. Burn it down, no more.")
        break
    print(f"There is a {thing} in the room.")
    
# Prints:
# There is a computer in the room.
# Oh, that's just my ghost friend, carry on.
# There is a chair in the room.
# Nope. Burn it down, no more.

input_message = 'Enter "green", "yellow", "red": '
color = input(input_message).lower()
print(f'{color} light!')
while color != 'quit':
    if color == 'green':
        print('Go!')
        color = input(input_message).lower()
    elif color == 'yellow':
        print('Slow down!')
        color = input(input_message).lower()
    elif color == 'red':
        print('Stop!')
        color = input(input_message).lower()
    else:
        print(f'...')
        print(f'Bogus! What the hell is {color}??')
        color = input(input_message).lower()
print(f"... wait {color} isn't a color")
print('Aight man, goodbye')