#Python Randomizations and lists
import random

#1. Heads or tails?
random_int = random.randint(0, 1)
if random_int == 1:
    print("Heads")
else:
    print("Tails.")


#2a Pick a ramdom person to pay from a bunch of names
names_string = input("Give me everybody's names seperated by a comma and a space: \n")

    #The split method converts a bunch of string to a list and seperates them by teh specified oarameters in the bracket hence a space and a comma makes sense in this case
names = names_string.split(", ") 
list_length = len(names)

    #I used the term list_length-1 because unlike the index, a list length counts from 1 and not 0
random_int = random.randint(0, (list_length-1))
person_paying = names[random_int]

print(f"{person_paying.title()} is the person paying today")

#2b. Alterantively, the .choice() function could be used like so;

names_string = input("Give me everybody's names seperated by a comma and a space: \n")
names = names_string.split(", ") 
list_length = len(names)
person_paying = random.choice(names)
print(f"{person_paying.title()} is the person paying today")


#3 Rock, paper , scissors
print("Welcome to jenny's rock, paper and scissors game, Choose an option to begin.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]

player_choice = int(input("Type 0 for Rock, 1 for paper and 2 for scissors. \n"))

computer_choice = random.randint(0, 2)
print(f"Computer Chose: \n {images[computer_choice]}")

print(f"You chose: \n {images[player_choice]}")



if computer_choice == player_choice:
    print(f"It's a draw.")
elif computer_choice == 0 and player_choice == 1:
    print(f"You win! ")
elif computer_choice == 0 and player_choice == 2:
    print(f"You lose!")
elif computer_choice == 1 and player_choice == 0:
    print(f"You lose!")
elif computer_choice == 1 and player_choice == 2:
    print(f"You win!")
elif computer_choice == 2 and player_choice == 0:
    print(f"You win!")
elif computer_choice == 2 and player_choice == 1:
    print(f"You lose!")
elif computer_choice > len(images) and player_choice > len(images):
    print("Please enter a valid option")


