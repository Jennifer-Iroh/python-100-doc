print("Hello and welcome to my first python program!!")
name = input("What's your name? \n")
print(f"Hello {name}, glad to have you here.")
food = input("Have you eaten in the last three hours? Yes or No? \n")
if food.lower() == "no":
    print(f"Please {name} find time to take care of yourself, life isn't that long you know, You're gonna look sickly if you don't eat right!!")
elif food.lower() == "yes":
    print(f"Good job {name}, I am glad you are taking care of yourself. Keep up the good work.")
else:
    print("I don't understand that command, please re run program")
    exit()
feeling = input("How do you feel today? Good Or Meh? \n")
if feeling.lower() == "good":
    print(f"I am super excited you are happy boo!")
elif feeling.lower() == "meh":
    print(f"It's okay, we all have our bad days. Take a walk, call a friend or take a nap, it should make you feel better. \n if It's any consolation, today has also been a weird day for me. But hey, I get to watch Gintama after. Lol")
else:
    print("I don't understand that command, please re run program")
    exit()

print("Thank you for using my program, if you ever need a friend to talk to or need help in anyway, I'm one DM away.  \n Love, \n Jenny")
exit()