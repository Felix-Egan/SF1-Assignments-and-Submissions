import random as rand
import os

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

deck = [(rank, suit) for rank in ranks for suit in suits]
rand.shuffle(deck)

player1_hand = deck[0:26]
player2_hand = deck[26:]


def card_comparison(p1_card, p2_card):
    return 1 if ranks.index(p1_card[0]) > ranks.index(p2_card[0]) else 2 if ranks.index(p1_card[0]) < ranks.index(p2_card[0]) else 0


def play_round(player1_hand, player2_hand):
	p1_card = player1_hand.pop(0)
	print(f"You play the {p1_card[0]} of {p1_card[1]}")
	p2_card = player2_hand.pop(0)
	print(f"Your opponent plays the {p2_card[0]} of {p2_card[1]}")
	if card_comparison(p1_card, p2_card) == 1:
		print("You win this round! You add both cards to the end of your hand.")
		player1_hand.append(p1_card)
		player1_hand.append(p2_card)
	elif card_comparison(p1_card, p2_card) == 2:
		print("You lost this round! (womp womp) Your opponent adds both cards to the end of their hand")
		player2_hand.append(p2_card)
		player2_hand.append(p1_card)
	elif card_comparison(p1_card, p2_card) == 0: 
		print("WAR! (wait, no no no...) PEACE! You and your opponent play three cards face down.")
		war(player1_hand, player2_hand)


def war(player1_hand, player2_hand, war_pool_reuse=[]):
	if len(player1_hand) < 4:
		print("BUT WAIT! The war has expended all of your cards! You lose! Humongus L.")
		exit("The game has concluded and the script will now stop...")
	elif len(player2_hand) < 4:
		print("BUT WAIT! The war has expended all of your opponent's cards! You win!")
		exit()
	else:
		war_pool = war_pool_reuse
		war_pool.append(player1_hand.pop(0))
		war_pool.append(player1_hand.pop(0))
		war_pool.append(player1_hand.pop(0))
		war_pool.append(player2_hand.pop(0))
		war_pool.append(player2_hand.pop(0))
		war_pool.append(player2_hand.pop(0))

		p1_card = player1_hand.pop(0)
		print(f"You play the {p1_card[0]} of {p1_card[1]}")
		p2_card = player2_hand.pop(0)
		print(f"Your opponent plays the {p2_card[0]} of {p2_card[1]}")

		war_pool.append(p1_card)
		war_pool.append(p2_card)
		if card_comparison(p1_card, p2_card) == 1:
			print("You win this round! You add all these cards to the end of your hand.")
			for card in war_pool:
				player1_hand.append(card)
		elif card_comparison(p1_card, p2_card) == 2:
			print("You lost this round! (womp womp) Your opponent adds all those cards to the end of their hand")
			for card in war_pool:
				player1_hand.append(card)
		elif card_comparison(p1_card, p2_card) == 0: 
			print("WAR! AGAIN! You and your opponent play three more cards face down.")
			war(player1_hand, player2_hand, war_pool)


def play_game():
	clear()
	input("Press Enter to start the game!")
	input("""NOTE: The card game \"War\" is poorly designed and may result in an infinite loop of win/lose/win/lose for what feels like forever. \n
If you encounter this loop, simply send CTRL + C to stop the script, and reinitialize it afterwards, or wait for it to conclude (can go on forever.)""")
	clear()
	while player1_hand and player2_hand:
			play_round(player1_hand, player2_hand)
			if not player1_hand:
				exit("You have lost the game (humongous L). You have no more cards in your hand. Press Enter to exit the script...")
			if not player2_hand:
				exit("You have won the game! Your opponent has no more cards in their hand. Press Enter to exit the script...")
			input("Press Enter to start the next round.")
			clear()
play_game()