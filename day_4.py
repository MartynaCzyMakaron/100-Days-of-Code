import random
rock = '''
    _____
---'   __)
      (___)
      (___)
      (__)
---.__(_)
'''

paper = '''
    _____
---'   __)____
          ____)
          _____)
         _____)
---.__________)
'''

scissors = '''
    _____
---'   __)____
          ____)
       ________)
      (__)
---.__(_)
'''
moves = [rock, paper, scissors]
person_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choice = random.randint(0, 2)

print(moves[person_choice])
print("Computer's choice:\n")
print(moves[computer_choice])

if person_choice == computer_choice:
    print("It's a tie")
elif person_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You win")
elif person_choice == 1:
    if computer_choice == 0:
        print("You win")
    else:
        print("You lose")
else:
    if computer_choice == 0:
        print("You lose")
    else:
        print("You win")
