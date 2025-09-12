import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_hand(hand):
    value = 0
    aces = 0
    for card in hand:
        rank, _ = card
        if rank == 'A':
            aces += 1
        value += values[rank]
    
    while value > 21 and aces > 0:
        value -= 10  
        aces -= 1
    
    return value

def show_hand(hand, name):
    print(f"{name}'s hand: {', '.join([f'{rank} of {suit}' for rank, suit in hand])} (Value: {calculate_hand(hand)})")

def decide_ace():
    while True:
        choice = input("You got an Ace! Do you want it to be 1 or 11? (1/11): ")
        if choice in ['1', '11']:
            return int(choice)
        print("Invalid input. Please choose 1 or 11.")

def game():
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    for i, (rank, suit) in enumerate(player_hand):
        if rank == 'A':
            values['A'] = decide_ace()
            break
    
    while True:
        show_hand(player_hand, "Player")
        show_hand(dealer_hand[:1], "Dealer")  

        if calculate_hand(player_hand) == 21:
            print("Blackjack! Player wins!")
            return

        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
            if calculate_hand(player_hand) > 21:
                show_hand(player_hand, "Player")
                print("Player busts! Dealer wins!")
                return
        else:
            break

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    
    show_hand(dealer_hand, "Dealer")

    if calculate_hand(dealer_hand) > 21:
        print("Dealer busts! Player wins!")
    elif calculate_hand(dealer_hand) > calculate_hand(player_hand):
        print("Dealer wins!")
    elif calculate_hand(dealer_hand) < calculate_hand(player_hand):
        print("Player wins!")
    else:
        print("It's a tie!")
    print("----------x----------")

if __name__ == "__main__":
    while True:
        print("----------x----------")
        game()
        print("----------x----------")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for participating!")
            break
