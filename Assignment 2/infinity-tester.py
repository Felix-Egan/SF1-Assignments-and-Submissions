import random as rand
import time
import os

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

deck = [(rank, suit) for rank in ranks for suit in suits]
rand.shuffle(deck)

player1_hand = deck[0:26]
player2_hand = deck[26:]
combinations_tracker = {}
comparison_count = 0
pair_tracker = {}

def card_comparison(p1_card, p2_card):
    global comparison_count
    comparison_count += 1
    return 1 if ranks.index(p1_card[0]) > ranks.index(p2_card[0]) else 2 if ranks.index(p1_card[0]) < ranks.index(p2_card[0]) else 0

def update_tracker_and_check(p1_card, p2_card):
    pair = (p1_card[0], p1_card[1], p2_card[0], p2_card[1])
    if pair in pair_tracker:
        pair_tracker[pair] += 1
    else:
        pair_tracker[pair] = 1
    if pair_tracker[pair] >= compare_count-1:
        end_game(f"INFINITE LOOP DETECTED DUE TO REPEATING CARD PAIR {compare_count} TIMES: {pair}")

def end_game(message):
    end_time = time.time()
    print(message)
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print(f"Total card comparisons: {comparison_count}")
    exit()

def play_round(player1_hand, player2_hand):
    p1_card = player1_hand.pop(0)
    print(f"You play the {p1_card[0]} of {p1_card[1]}")
    p2_card = player2_hand.pop(0)
    print(f"Your opponent plays the {p2_card[0]} of {p2_card[1]}")
    update_tracker_and_check(p1_card, p2_card)
    result = card_comparison(p1_card, p2_card)
    if result == 1:
        print("You win this round! You add both cards to the end of your hand.")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)
    elif result == 2:
        print("You lost this round! (womp womp) Your opponent adds both cards to the end of their hand")
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)
    else: 
        print("WAR! (wait, no no no...) PEACE! You and your opponent play three cards face down.")
        war(player1_hand, player2_hand)

def war(player1_hand, player2_hand, war_pool_reuse=[]):
    if len(player1_hand) < 4:
        end_game("BUT WAIT! The war has expended all of your cards! You lose! Humongous L.")
    elif len(player2_hand) < 4:
        end_game("BUT WAIT! The war has expended all of your opponent's cards! You win!")
    else:
        war_pool = war_pool_reuse
        war_pool.extend([player1_hand.pop(0) for _ in range(3)])
        war_pool.extend([player2_hand.pop(0) for _ in range(3)])
        p1_card = player1_hand.pop(0)
        print(f"You play the {p1_card[0]} of {p1_card[1]}")
        p2_card = player2_hand.pop(0)
        print(f"Your opponent plays the {p2_card[0]} of {p2_card[1]}")
        war_pool.append(p1_card)
        war_pool.append(p2_card)
        update_tracker_and_check(p1_card, p2_card)
        result = card_comparison(p1_card, p2_card)
        if result == 1:
            print("You win this round! You add all these cards to the end of your hand.")
            player1_hand.extend(war_pool)
        elif result == 2:
            print("You lost this round! (womp womp) Your opponent adds all those cards to the end of their hand")
            player2_hand.extend(war_pool)
        else:
            print("WAR! AGAIN! You and your opponent play three more cards face down.")
            war(player1_hand, player2_hand, war_pool)

def play_game():
    global start_time
    start_time = time.time()
    clear()
    input("Press Enter to start the game!")
    input("""NOTE: The card game \"War\" is poorly designed and often results in an infinite loop of win/lose/win/lose for what feels like forever. \n
If you encounter this loop, simply send CTRL + C to stop the script, and reinitialize it afterwards, or wait for it to conclude (can go on forever.)""")
    global compare_count
    compare_count = int(input("\n Enter Comparison Cap: "))
    clear()
    while player1_hand and player2_hand:
        play_round(player1_hand, player2_hand)
        most_compared = max(pair_tracker, key=pair_tracker.get)
        print(f'                                                                   MOST REPEATED COMPARISON: {most_compared}: {pair_tracker[most_compared]} times')
    end_game("The game has ended...")

play_game()