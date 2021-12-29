import random


def check_guess(num):
    if num == correct:
        return True
    else:
        return False


def give_clue(num):
    if num > correct:
        print("Too high.")
    else:
        print("Too low.")


attempts = 10
correct = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of number between 1 and 100.")
dif_lvl = input("Choose a difficulty. Type 'easy or 'hard': ")

if dif_lvl == 'hard':
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if check_guess(guess):
        print("You guessed correctly. You win!")
        attempts = 0
    else:
        give_clue(guess)
    attempts -= 1
