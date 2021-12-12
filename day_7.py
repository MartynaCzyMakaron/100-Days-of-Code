import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo


chosen_word = word_list[random.randint(0, 2)]
lives = 6

display = []
for i in range(0, len(chosen_word)):
    display.append("_")
print(chosen_word + " is the chosen word")
past_guesses = []

print(logo)

while list(chosen_word) != display and lives > 0:
    print(display)
    guess = str(input("Guess a letter")).lower()
    if guess not in past_guesses:
        i = 0
        if guess in chosen_word:
            for letter in chosen_word:
                if guess == letter:
                    display[i] = guess
                i += 1
        else:
            lives -= 1

        print(stages[lives])
        past_guesses.append(guess)
    else:
        print("You've already guessed this letter")


if lives > 0:
    print("You guessed correctly! You won!")
else:
    print("You dead! xx")
