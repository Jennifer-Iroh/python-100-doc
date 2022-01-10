#1. Odd or even?
number = int(input("Which number do you want to check? "))

if number % 2 == 1:
    print("That is an odd number")
else:
    print("That is an even number")


#2. Update BMI with conditions
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round((weight / (height ** 2)), 2) 

if bmi < 18.5: 
    print(f"Your bmi is {bmi}. You are underweight ")
elif bmi < 25:
    print(f"your bmi is {bmi}. You have a normal weight ")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {bmi}. You are overweight ")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}. You are obese ")
else:
    print(f"Your bmi is {bmi}. You are clinically obese")


#3. Check if year is a leap year.
year = int(input("Enter the year you want to check: "))

if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#4. Python Pizza?

print("Welcome to Pthon Pizza Deliveries!!")
size = input("What size do you want? S, M, L: ")
add_ppepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

    #Logic for pizza pricing
if size.upper() == "S":
    bill = 15
    if add_ppepperoni.upper() == "Y":
        bill+=2
    if extra_cheese.upper() == "Y":
        bill+=1
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is {bill}")
elif size.upper() == "M":
    bill = 20
    if add_ppepperoni.upper() == "Y":
        bill+=3
    if extra_cheese.upper() == "Y":
        bill+=1
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is {bill}")
elif size.upper() == "L":
    bill = 25
    if add_ppepperoni.upper() == "Y":
        bill+=3
    if extra_cheese.upper() == "Y":
        bill+=1
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is {bill}")
else:
    print("That is not a valid option, please re-start the program. ")


#5. Love calculator.
print("Welcome to Jenny's love calculator!!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_join = name1 + name2
name_join = name_join.lower()

# Conunt the letters and add
true = name_join.count('t') + name_join.count('r') + name_join.count('u') + name_join.count('e')
love = name_join.count('l')  + name_join.count('o') + name_join.count('v') + name_join.count('e')

#Cinvert to a string so we can concatenete the results
result = str(true) + str(love)

#Convert back to an int so that we can use them in the conditionals.
result = int(result)

#Write the logic for the code. 
if (result < 10) or (result > 90):
    print(f"Your score is {result}%, you go together like coke and menthos")
elif (result >= 40) and (result <= 50):
    print(f"Your Score is {result}%, you are alright together")
else:
    print(f"Your score is {result}%")


#6. Treasure island N/b: The 3 single quotes before and after  the brackets in the print statement tell python to print
#the ascii characters as multiple lines of code
print('''
_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Which way do you want to go? Left or Right? \n")


if direction.lower() == "left":
    action = input("Do you want to swim or wait? \n")
    if action.lower() == "wait":
        door_colour = input("Which door do you choose? Red, Blue or Yellow? \n")
        if door_colour.lower() == "red":
            print("Oh, you've been burned by fire game over")
        elif door_colour.lower() == "blue":
            print("You've been eaten by beasts, game over")
        elif door_colour.lower() == "yellow":
            print("Congratulations, you have discovered the treasure, you win")
        else:
            print("You chose a door that does not exist, game over")
    else:
        print("You have been attacked by a trout, game over")
else:
    print("You fell into a hole, game over")
    




























