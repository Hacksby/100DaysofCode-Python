from art import logo
import random


# Function for dealing random a card to the user or the computer
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Just for the sum function, returns scores adding the values of the cards in the hand
def calculate_scores(card_list):
    return sum(card_list)


# If a wild ace appears, gets its value in regard of the total value of the hand
def ace_controller(card_list):
    if sum(card_list) > 21:
        for card in range(len(card_list)):
            if card_list[card] == 11:
                card_list[card] = 1
    return card_list


# The computer will draw until its hand gets a value >= 17
# Check each hand values and print the corresponding message
def print_final_score(u_cards, c_cards):
    while sum(c_cards) < 17:
        c_cards.append(deal_card())
        ace_controller(c_cards)
    c_score = calculate_scores(c_cards)
    u_score = calculate_scores(u_cards)
    print(f"\n\tYour cards: {u_cards}, current score: {u_score}")
    print(f"\tComputer cards: {c_cards}, computer score:{c_score}\n")

    if u_score > 21:
        print("\tYou went over... You Lose 😭\n")
    elif u_score == c_score:
        print("\tDRAW!! 🙀 \n")
    elif u_score == 21 and len(u_cards) == 2:
        print("\tBLACKJACK, You Win! 🙀 🎉🎉\n")
    elif c_score == 21 and len(c_cards) == 2:
        print("\tComputer BLACKJACK, You Lose 😭\n")
    elif c_score > 21:
        print("\tComputer went over, You Win! 🎉🎉\n")
    elif u_score > c_score:
        print("\tNice! You Win! 🎉🎉\n")
    else:
        print("\tYou Lose, oldsport 😭\n")
    blackjack()


# BlackJack as a function in order to call it if the condition is met
def blackjack():
    run_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if run_input == "y":
        print(logo)
        user_cards = []
        computer_cards = []
        # Day1, Starting table
        while len(user_cards) < 2 and len(computer_cards) < 2:
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        # Day2
        card_dealer_controller = True
        while card_dealer_controller:
            user_cards = ace_controller(user_cards)
            user_score = calculate_scores(user_cards)
            print(f"\n\tYour cards: {user_cards}, current score: {user_score}")
            print(f"\tComputer's first card: {computer_cards[0]}\n")
            if sum(user_cards) < 22:
                get_card_answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if get_card_answer != "y":
                    card_dealer_controller = False
                    print_final_score(user_cards, computer_cards)
                else:
                    user_cards.append(deal_card())
            else:
                card_dealer_controller = False
                print_final_score(user_cards, computer_cards)


# STARTING POINT
blackjack()
