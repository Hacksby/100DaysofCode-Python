from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def blackjack():
    run_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if run_input == "y":
        print(logo)
        user_cards = []
        computer_cards = []
        while len(user_cards) < 2 and len(computer_cards) < 2:
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Your cards: {computer_cards}, current score: {computer_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_cards[-1] == 11 and user_score > 21:
            user_cards[-1] = 1

        if user_score == 21:
            print("BLACKJACK, You Win!")

        blackjack()


blackjack()
