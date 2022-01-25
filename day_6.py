# PYTHON FUNCTIONS OR NOT? LOL
import random

# simple program to mask a person's password

username = input('Enter a username: ')
password = input('Enter your password: ')

password_length = len(password)
# mask password
secret = '*' * password_length

print(f' {username} Your password {secret} is {password_length} letters long ')


# 2.  Function for a self driving car


def check_driver_age(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


check_driver_age(100)


# 3. Function that returns the highest even number from a list of numbers.
def highest_even(li):
    li.sort()
    li.reverse()
    for i in li:
        if i % 2 == 0:
            return i


print(highest_even([10, 2, 3, 4, 8, 11, 14, 18]))

# Alternateviley


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11, 14, 18]))
