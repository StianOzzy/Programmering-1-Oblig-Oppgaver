# imports
import random
import time

# -----------------------------------------------------------------------------------------------------------------------

# ___ Create deck ___
# assigns card-tuples of format (*rank*, *suit*) to a list called cardbank
def create_new_deck():
    cardbank = []
    suits = ["♠", "♥", "♦", "♣"]
    for i in range(1, 14):
        for suit in suits:
            face = {1: "A", 11: "J", 12: "Q", 13: "K"}
            if i in face:
                i = face[i]
            cardbank.append((i, suit))
    return cardbank

# ___ Shuffle Functionality ___
# Shuffles the order of the card-tuples in cardbank
def shuffle_deck(_cards):
    random.shuffle(_cards)

# ___ Drawing cards ___
# removes a card-tuple from the cardbank, and appends it to player/dealer
def draw_card(to_inv, _cards):
    to_inv.append(_cards.pop())

# ___ Show hands ___
# print hands
def show_player_hands(hand):
    print(hand)

# ___ Check sum ___
# Check the total sum the cards in a hand
def check_sum(hand):
    total_sum = 0
    global ace_amount
    for i in range(len(hand)):
        rank, suit = hand[i]
        invface = {"A": 11, "J": 10, "Q": 10, "K": 10}
        if rank in invface:
            rank = invface[rank]
        if rank == 11:
            ace_amount += 1
        total_sum = total_sum + rank
    if total_sum > 21 and ace_amount >= 1:
        total_sum -= 10
        ace_amount -= 1
    return total_sum

# ___ Placing bet ___
# Player chooses amount to bet
def place_bet():
    global chips
    while True:
        if chips == 1:
            print("You currently have 1 chip.")
        else:
            print(f"You currently have {chips} chips.")

        global bet_amount
        bet_amount = int(input("How many chips do you want to bet?\n\n>"))

        if bet_amount > chips:
            print("You do not have enough chips for that bet. Try again.")
        elif bet_amount <= 0:
            print("Invalid bet amount. Try again.")
        elif bet_amount >= 0 and bet_amount <= chips:
            chips -= bet_amount
            break

    # ___ Game start ___

# ___ Game initializer ___
# All parameters to initialize a new fresh game. Welcome message to player
def initialize_game():
    global player_hand
    global dealer_hand
    global chips
    global cards
    global ace_amount
    player_hand = []
    dealer_hand = []
    cards = create_new_deck()
    shuffle_deck(cards)
    ace_amount = 0
    clear_console()
    print("\n___ Welcome to Blackjack ___\n")

# ___ Deal to player ___
# Deals a card to the player, and shows the new total
def deal_to_player():
    draw_card(player_hand, cards)
    show_player_hands(f"Dealers hand:\n(UNKNOWN)  {dealer_hand[0][0]}{dealer_hand[0][1]}\n")
    playerhandvisual = ""
    for i in range(len(player_hand)):
        cardstring = str(player_hand[i][0])+ "" + str(player_hand[i][1])
        playerhandvisual = playerhandvisual+ "  " +cardstring
    show_player_hands(f"Players Cards:\n{playerhandvisual}")
    print("Player hand total value:", check_sum(player_hand),"\n")

# ___ Hit or Stand ___
# Asks the player if they will choose to hit or stand. Returns a 1 for hit or 0 for stand
def hit_or_stand():
    while True:
        statement = input("Do you wish to hit or stand?\n\n>").lower()
        if statement == "hit" or statement == "h":
            return 1
        elif statement == "stand" or statement == "s":
            return 0
        else:
            print("Invalid choice. Please choose 'hit' or 'stand'.")

# ___ Dealer Show Cards ___
def dealer_show():
    global dealercardstring
    global dealerhandvisual
    dealerhandvisual = ""
    for i in range(len(dealer_hand)):
        dealercardstring = str(dealer_hand[i][0]) + "" + str(dealer_hand[i][1])
        dealerhandvisual = dealerhandvisual + "  " + dealercardstring
    show_player_hands(f"\nDealers Cards ({len(dealer_hand)}):\n{dealerhandvisual}")
    print("Dealer hand total value:", check_sum(dealer_hand), "\n")

# ___ Clear Console ___
def clear_console():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Player is given 10 chips as the program begins
chips = 10

# Run main program
while True:
    # initialize game parameters
    initialize_game()

    # ask for bet
    place_bet()

    # bet message for the player
    print(f"\nYou placed a bet of {bet_amount} chips, you have {chips} chips remaining.")
    print("Shuffling...\n")
    time.sleep(1)

    # Give 2 cards to dealer, and 2 cards to player. Keep the dealers first card hidden.
    draw_card(dealer_hand, cards)   # First card dealt to dealer
    draw_card(dealer_hand, cards)   # Second card dealt to dealer
    draw_card(player_hand, cards)   # First card dealt to Player
    deal_to_player()                # Second card dealt to player, and formatting shown in console

    if check_sum(player_hand) == 21:
        print(f"BlackJack")
        print(f"Player wins {2 * bet_amount} chips.")
        chips = chips + 3 * bet_amount
        betting = 0
    else:
        betting = 1
    while betting == 1:
        if hit_or_stand() == 1:
            print("*** Player will be dealt another card ***")
            time.sleep(1)
            deal_to_player()
            if check_sum(player_hand) > 21:
                print("Player bust.")
                print("Dealer wins.")
                break
        else:
            print("Player hand total value:", check_sum(player_hand))
            while True:
                dealerhandvisual = ""
                dealer_show()
                if check_sum(dealer_hand) >= 17:
                    print("Dealer has to stand at", check_sum(dealer_hand),".")
                    time.sleep(1)
                    if check_sum(player_hand) > check_sum(dealer_hand):
                        print(f"Player wins {bet_amount} chips.")
                        chips = chips + 2*bet_amount
                        betting = 0
                        break
                    elif check_sum(player_hand) < check_sum(dealer_hand):
                        print(f"Dealer wins. Player loses {bet_amount} chips.")
                        betting = 0
                        break
                    elif check_sum(player_hand) == check_sum(dealer_hand):
                        print("It is a draw.")
                        betting = 0
                        chips = chips + bet_amount
                        break
                elif check_sum(dealer_hand) < 17:
                    print("*** Dealer will be dealt another card ***")
                    time.sleep(1)
                    draw_card(dealer_hand, cards)
                    if check_sum(dealer_hand) > 21:
                        dealer_show()
                        print("Dealer bust.")
                        print(f"Player wins {bet_amount} chips.")
                        chips = chips + 2 * bet_amount
                        betting = 0
                        break

                time.sleep(1)

    time.sleep(1)
    if chips < 1:
        print("You are out of chips. Game over.")
        break
    else:
        while True:
            playagain = input("Do you wish to play again? (y/n)\n\n>").lower()
            if playagain == "y" or playagain == "yes":
                betting = 1
                break
            elif playagain == "n" or playagain == "no":
                betting = 0
                break
            else:
                print("Invalid choice. Please choose 'yes' or 'no'.")
                continue