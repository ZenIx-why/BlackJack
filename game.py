import random

suits = ['♥️', '♦️', '♣️', '♠️']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        value += values[rank]
        if rank == 'Ace':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_cards(player_hand, dealer_hand, show_all_dealer_cards):
    print("\nDealer's Hand:")
    if show_all_dealer_cards:
        for card in dealer_hand:
            print(card)
        print(f"Value: {calculate_hand_value(dealer_hand)}")
    else:
        print(" <card hidden>")
        print(dealer_hand[1])
    print("\nPlayer's Hand:")
    for card in player_hand:
        print(card)
    print(f"Value: {calculate_hand_value(player_hand)}")

def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        display_cards(player_hand, dealer_hand, False)
        if calculate_hand_value(player_hand) == 21:
            print("Blackjack! Player wins!")
            return "win"
        move = input("Would you like to Hit or Stand? Enter 'h' or 's': ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                display_cards(player_hand, dealer_hand, True)
                print("Player busts! Dealer wins!")
                return "lose"
        elif move == 's':
            break

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    display_cards(player_hand, dealer_hand, True)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! Player wins!")
        return "win"
    elif dealer_value > player_value:
        print("Dealer wins!")
        return "lose"
    elif dealer_value < player_value:
        print("Player wins!")
        return "win"
    else:
        print("It's a tie!")
        return "draw"

wins = 0
draws = 0
loses = 0

def p():
    global wins, draws, loses
    result = play_blackjack()
    if result == "win":
        wins += 1
    elif result == "lose":
        loses += 1
    else:
        draws += 1
    print("Game is ended!")

def s():
    print(f"Wins: {wins}")
    print(f"Draws: {draws}")
    print(f"Loses: {loses}")

def l():
    print("*---*---*---*---*---*---*---*---*")
    print("Lobby:")
    print("--------------------")
    print("Choose one of the functions:")
    print("Play(p)")
    print("Stats(s)")
    print("Exit(e)")
    return input("Your choice: ")

def after_game():
    while True:
        print("What do you want to do?")
        print("Play again(a)")
        print("Return to lobby(l)")
        after_game_answer = input("Your answer: ")
        if after_game_answer == "a":
            print("> starting game...")
            p()
            continue
        elif after_game_answer == "l":
            return
        else:
            print("No such an answer! Please enter valid one.")

while True:
    choice = l()
    if choice == "p":
        print("> starting game...")
        p()
        after_game()
    elif choice == "s":
        s()
    elif choice == "e":
        print("> exiting...")
        break
    else:
        print("No such an answer! Please enter valid one.")