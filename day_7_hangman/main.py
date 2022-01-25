# HANGMAN GAME

# Import modules from various folders
import random
from word_list import word_list
from ascii import stages, logo

print(logo)
# Create a word list and generate random words from the list everytime the game runs.
chosen_word = random.choice(word_list)


# create variable to keep track of availabe lives and a variable to set the status of the game and to find the length of the chosen word.
lives = 6
game_over = False
word_length = len(chosen_word)

# create a list of underscores to represent the number of letters the word should have
display = []
for _ in range(word_length):
    display += "_"
print(display)

# Loop to enable user enter multiple letters till the game is over
while not game_over:
    # take user input and check if tthere is any correct letter and replace the underscores with themm.
    guess = input("Guess any letter of your chioce: ").lower()

    if guess in display:
        print(f"{guess}, You have already guessed this letter")
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Reduce the lives available in the game if a user choses a wrong option and set a condition to end the while loop.
    if guess not in chosen_word:
        print(f"{guess} is not a part of the word ")
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lose.')
    # Print word as a string not list
    print(f' '.join(display))

    # Check if a user gets all the letters right and make them win.
    if '_' not in display:
        game_over = True
        print('You win')

    print(stages[lives])

    # Print corresponding ascii art for each iteration
print(f"The word was {chosen_word}")
