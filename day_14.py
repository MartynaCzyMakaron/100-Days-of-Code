from game_data import data
import random


def who_winner(first, second):
    if second["follower_count"] > first["follower_count"]:
        return second
    else:
        return first



alive = True
score = 0
A = random.choice(data)

while alive:
    B = random.choice(data)
    print("Compare A: " + A["name"] + ", a " + A["description"] + ", from " + A["country"])
    print("VS")
    print("Compare B: " + B["name"] + ", a " + B["description"] + ", from " + B["country"])
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == 'A':
        guess = A
    else:
        guess = B
    if guess == who_winner(A, B):
        score += 1
        A = B
        print(f"That's right! Current score: {score}")
    else:
        alive = False

print(f"It's not a correct answer. Your score : {score}")


