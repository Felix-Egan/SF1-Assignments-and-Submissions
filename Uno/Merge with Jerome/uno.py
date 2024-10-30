# Made by Jerome and Felix
# Intro to Programming - Section 00002

import random
from time import sleep
import os


# clear the screen
def clear_screen(): os.system("cls" if os.name == "nt" else "clear")


# make the player pick a specific card from their hand
def pick_card(deck, first_pick):
    # display tip only when pick_card is used for the first time
    if first_pick:
        print("Tip: Type 'exit' to go back to the action menu.")
        first_pick = False

    try:
        chosen_card_num = input("Card number: ")

        if chosen_card_num == "exit":
            return

        chosen_card_num = int(chosen_card_num)

        # check if chosen_card_num is in deck's range
        if chosen_card_num < 1 or chosen_card_num > len(deck) + 1:
            raise Exception
        
        chosen_card = deck[chosen_card_num - 1]

        return chosen_card

    except Exception:
        print("This card is not in your deck!")
        return


# make sure the selected card can be played according to Uno rules (same color or same number)
def play_valid(card, face_up): return card[0] == face_up[0] or card[1] == face_up[1]


# play a card selected by the player from their hand
def play_card(hand, discard_pile, first_play, ai_turn):
    if ai_turn:
        for card_temp in hand:
            if play_valid(card_temp, discard_pile[-1]):
                card = card_temp
    else:
        card = pick_card(hand, first_play)

    # handle pick_card exit case
    if card == None:               # play aborted
        return hand, discard_pile, True
    
    elif not play_valid(card, discard_pile[-1]):
        print("Make sure your card has either the same color or the same number as the face up card.")
        return hand, discard_pile, True

    discard_pile.append(hand.pop(hand.index(card)))
    print(f"{'AI plays' if ai_turn else 'You play'} the {print_card(card, ai_turn, public_card=True)}.")

    return hand, discard_pile, False


# draw a card from the center deck
def draw_card(center_deck, discard_pile, hand, ai_turn):
    if len(center_deck) == 0:
        print("The deck is empty. Reusing discard pile...")
        sleep(1)
        
        if (len(discard_pile)) == 1:
            print("The face up card is the only card left on the table!")
                                                   
                                                    # draw aborted
            return center_deck, discard_pile, hand, True
        
        # use discarded cards to 'rebuild' the center deck
        random.shuffle(discard_pile)
        center_deck = discard_pile
        discard_pile = [center_deck.pop()]

    card = center_deck.pop()

    hand.append(card)
    print(f"{'You' if not ai_turn else 'AI'} drew {print_card(card, ai_turn, public_card=False)}.")

    return center_deck, discard_pile, hand, False


# display a card in the [<Color> <Number>] format
def print_card(card, ai_turn, public_card): return f"[{card[0]} {card[1]}]" if public_card or not ai_turn else "<Hidden>"
                                                             # Printing the AI's hand would give the player an unfair advantage
    


# handle all the game's rounds
def main(num_players, player_hands, face_up, deck, ai_active=False):
    current_player = 0
    discard_pile = [face_up]

    # used later to display pick_card's exit tip (see pick_card definition)
    first_round = True

    ai_turn = False

    # round loop (1 round = a single player's action)
    while True:
        # line to visually separate each round
        clear_screen()
    
        print(f"It is player {current_player + 1}'s turn.")
        print(f"The face up card is {print_card(face_up, ai_turn, public_card=True)}.")
        print("")
        print("Your deck:")

        current_hand = player_hands[current_player]

        # print every card in a player's hand using a 1-based card number
        card_number = 0
        for card in current_hand:
            card_number += 1
            print(f"{card_number}: {print_card(card, ai_turn, public_card=False)}")

        print("")
        print("a: Play a card")
        print("b: Draw")
        print("")

        # true if no cards remain in the center deck while trying to draw
        draw_aborted = False

        # action loop (make sure the player always goes back to the action menu when a specific action fails)
        while True:
            # skip rounds where the player can't draw and cannot use any of their cards
            if draw_aborted:
                one_card_valid = False

                for card in current_hand:
                    if play_valid(card, face_up):
                        print("You have to play a card.")
                        one_card_valid = True
                        break

                if not one_card_valid:
                    print("It is impossible for you to play this round.")
                    break

                draw_aborted = False

            ai_action = "a" if [card for card in current_hand if play_valid(card, face_up)] else "b" # AI plays if any valid cards, else draw

            action = input("Action: ") if not ai_turn else ai_action # AI action if AI's turn

            # see play_card definition
            if action == "a":
                current_hand, discard_pile, play_aborted = play_card(current_hand, discard_pile, first_round, ai_turn)
                first_round = False

                # if no card is played, start next interation of action loop
                if play_aborted:
                    continue

                break

            # see draw_card definition
            elif action == "b":
                deck, discard_pile, current_hand, draw_aborted = draw_card(deck, discard_pile, current_hand, ai_turn)

                # if no card can be drawn, start next iteration of action loop
                if draw_aborted:
                    continue

                break

            print("Invalid action! Answer with 'a' or 'b'.")

        sleep(0.75)

        # 1 card remaining in the player's hand = Uno!
        if len(current_hand) == 1:
            print("\nUno!")
            sleep(2)

        # 0 cards remaining = winning the game
        elif len(current_hand) == 0:
            print(f"\nPlayer {current_player + 1} won! Congrats!")
            break

        if ai_turn:
            sleep(4) # So Player can read what the AI did

        # switch to next player
        current_player = (current_player + 1) % num_players
        if ai_active and current_player == 1:
            ai_turn = True
        else:
            ai_turn = False

        # face_up is the last card added to the discard pile
        face_up = discard_pile[-1]


def start_game(deck):
    # fancy little ascii art
    print("""
    ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  Jerome & Felix
     ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   Edition
          
        """)

    # ask the number of players indefinitely if the initially inputted data is incorrect
    while True:
        # input number of players
        try:
            min_players = 1
            max_players = 10
            
            num_players = int(input(f"Number of players ({min_players}-{max_players}): "))

            ai_active = False
            if num_players == 1:
                ai_active = True
                num_players = 2

            if num_players < min_players or num_players > max_players:
                raise Exception

            break

        except Exception:
            print(f"Enter a number between {min_players} and {max_players}.")

    # player hands, 7 cards for each player
    player_hands = []
    for _ in range(num_players):
        player_hands.append([deck.pop(0) for _ in range(7)])

    # face up card, first in the discard pile
    face_up = deck.pop(0)

    main(num_players, player_hands, face_up, deck, ai_active)


# generate the 40-card uno deck (without special cards)
colors = ("Red", "Yellow", "Blue", "Green")
ranks = list(range(0, 10)) + list(range(1, 10)) # official game rules; 2 cards of each color except 0
deck = [(color, rank) for color in colors for rank in ranks]

random.shuffle(deck)

start_game(deck)