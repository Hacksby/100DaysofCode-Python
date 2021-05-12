from art import logo


def find_winner(dictionary):
    # Variables for winner name and value of the winner bet
    highest_bidder = ""
    highest_bid = 0
    # Dictionary iteration
    for bidder in dictionary:
        if dictionary[bidder] > highest_bid:
            highest_bid = dictionary[bidder]
            highest_bidder = bidder
    # Result
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


# Starting Point
print(logo)
print("Welcome to this blind auction!")
finish_program = False
bidder_dictionary = {}

while not finish_program:
    # Inputs
    bidderName = input("What's your name?:\n")
    bidderMoney = int(input("How much do you want to bet?:\n$"))
    # Keep data in dictionary
    bidder_dictionary[bidderName] = bidderMoney
    # Loop condition to keep running the program
    auctionContinues = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if auctionContinues == 'no':
        finishProgram = True
        find_winner(bidder_dictionary)  # Trigger function to finding and print the highest bidder
    else:
        print(logo)
