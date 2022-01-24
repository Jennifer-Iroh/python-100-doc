# PYTHON FUNCTIONS OR NOT? LOL
from ctypes.wintypes import CHAR
from distutils.command import check
from email.utils import format_datetime
import random
from telnetlib import CHARSET

# simple program to mask a person's password

# username = input('Enter a username: ')
# password = input('Enter your password: ')

# password_length = len(password)
# # mask password
# secret = '*' * password_length

# print(f' {username} Your password {secret} is {password_length} letters long ')


# 2.  Function for a self driving car
# def check_driver_age(age = 0):
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")

# check_driver_age(100)


# 3. Function that returns the highest even number from a list of numbers.
# def highest_even(li):
#     li.sort()
#     li.reverse()
#     for i in li:
#         if i % 2 == 0:
#             return i

# print(highest_even([10,2,3,4,8,11,14, 18]) )

# Alternateviley
# def highest_even(li):
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)


# print(highest_even([10, 2, 3, 4, 8, 11, 14, 18]))


# HANGMAN GAME

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
print(chosen_word)

# a. create a list of underscores to represent the number of letters the word should have
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

# print(chosen_word == display)

# b. replace the underscores with the correct letter at the correct position.
def check_letter():
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

#loop through till the user fills all the blanks
# iteration = 0
while chosen_word != display:
    # iteration += 1
    guess = input("Guess any letter of your chioce: ").lower()
    check_letter()
    
if chosen_word == display:
    print("You win")
else:
    print("You lose")
    
    
