import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def sum_score(list):
    score = sum(list)
    if 11 in list:
        if score > 21:
            score -= 10
    return score


def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score > 21 :
        return "You went over. You lose :<"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You loose!"



to_continue = True

while to_continue:
    your_cards = []
    computer_cards = []
    continue_round = True
    decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if decision == 'n':
        to_continue = False
    your_cards.append(deal_cards())
    your_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    while continue_round:
        user_score = sum_score(your_cards)
        computer_score = sum_score(computer_cards)
        print(f"Your cards : {your_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score > 21:
            continue_round = False
        next_round = input("Type 'y' to get another card or 'n' to pass: ")
        if next_round == 'y':
            your_cards.append(deal_cards())
        else:
            continue_round = False
    if computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = sum_score(computer_cards)
    print(f"Your final hand: {your_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))