# PYTHON LOOPS
# 1. Finding the height  from a list of student heights.
total = 0
students_height = input("Input a list of student heights: ").split()
for n in range(0, len(students_height)):
    students_height[n]  = int(students_height[n])
#print(students_height)

    #for loop to get length of list
total_students = 0
for student in students_height:
    total_students+=1


    #for loop to sum up the individual heights of the students in the list
total_height = 0
for height in students_height:
    total_height += height

average_height = total_height/total_students
rounded_average = (round(average_height))
print(f"the average height of all the students is {rounded_average}cm")


# 2. find the biggest number in the list
biggest_num = 0
for num in students_height:
    if num > biggest_num:
        biggest_num = num
print(f"The tallest persson is {biggest_num}cm")


# 3. Adding all the even numbers from 1 - 100

total = 0
for x in range(2, 101, 2):
    total += x
print(f"Total sum of all the even numbers from 1 - 100 is {total}")

# 4. Fizz buzz game.
number = 0
for x in range(1, 101):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz!!")
    elif x % 3 == 0:
         print("Fizz!")
    elif x % 5 == 0:
        print("Buzz!")
    else:
        print(x)

# 5. Python password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input(f"How many symbols would you like?\n"))
no_of_numbers = int(input(f"How many numbers would you like?\n"))

    #Easy solution. Arranged sequentially
# password = ""

# for letter in range(1, no_of_letters + 1):
#     password += random.choice(letters)

# for symbol in range(1, no_of_symbols + 1):
#     password += random.choice(symbols)

# for number in range(1, no_of_numbers + 1):
#     password += random.choice(numbers)
    
# print(f"Your password is {password} ")


    #Hard solution - Order randomized
password = []

for letter in range(1, no_of_letters + 1):
    password.append(random.choice(letters)) 

for symbol in range(1, no_of_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, no_of_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password) 
password = "".join(password)
print(f"Your password is {password} ")

    
#         #Solution alternate - not so good, but nice attempt without looping, lol
# random_letters = random.sample(letters, no_of_letters)
# random_letters_str = "".join(random_letters)
# # print(random_letters_str)

# random_numbers = random.sample(numbers, no_of_numbers)
# random_numbers_str = "".join(random_numbers)
# # print(random_numbers_str)

# random_symbols = random.sample(symbols, no_of_symbols)
# random_symbols_str = "".join(random_symbols)
# # print(random_symbols_str)

# print(f"Your password is {random_letters_str}{random_symbols_str}{random_numbers_str} ")




    

  
        




