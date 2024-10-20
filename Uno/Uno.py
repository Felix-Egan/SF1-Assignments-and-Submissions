#region: Imports ✔
import random
import os
cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#endregion

#region: Pregame constants (Note that the number of cards has been adjusted to the actual game's card count = 108) ✔
face_up_pile = []
colors = ["Red", "Yellow", "Blue", "Green"]
digits = ["+2", "+2", "Reverse", "Reverse", "Skip", "Skip"]
digits.extend(list(range(10)) + list(range(1, 10)))
draw_pile = [(digit, color) for digit in digits for color in colors] # Renamed deck to draw_pile for convenience and readibility
wild_cards = [("Wild Color Change", "Black"), ("Wild Draw Four", "Black")]
draw_pile.extend(wild_cards * 4)
random.shuffle(draw_pile)
reverse_play = False
players_called_UNO = []
cls()
print("""
As Eric said many times, we were tasked with making a simplified version of UNO. Now, to which I gladly responded with "Respectfully, no." so I made a full-fledged version of UNO instead! (I have not slept in 3 days 👍)
This version works in a very similar fashion to the normal UNO game we all love (until someone starts with 4 wild cards and we all want to do is scare them while they are drinking a glass of juice so it splashes all over
their clothes... Yeah, I see you Antonin!!). This version only DOESN'T include the following features that UNO players sometimes implement, mainly: NO Stacking +2s and +4s, NO Reversing a +2 or +4 (otherwise known as the 
ULTIMATE UNO REVERSE!!!), and finally +2s and +4s do NOT skip turns in this version. I don't know why that's even a considered rule to begin with! Anyways, have fun! Max playercount of *15* btw, otherwise things break :/   
""")
input("Press Enter to continue...")
cls()
num_players = int(input("Enter number of players: ")) #
player_hands = [[draw_pile.pop(0)  for i in range(7)] for i in range(num_players)] # generate a hand for each player
#endregion

#region:Special Cards  ________
def reverse_card():
    global reverse_play # Sorry for using global variables Eric. They just make my life so much easier for this script `\_(._.)_/`
    reverse_play = not reverse_play
    print("The order of play is now reversed!")

def skip_card():
    current = ((current - 1) % num_players) if reverse_play else ((current + 1) % num_players)

def opponent_draw_card(player_hand, draw_pile, card_draw_count):  
    for i in range(card_draw_count):
        if draw_pile:
            print("Your opponent draws a card.")
            player_hand.append(draw_pile.pop(0))
        else:
            print("The draw pile is empty, so your opponent picks up no cards.")

def draw_four_color_change_card(player_hand, draw_pile, face_up):
    change_color(face_up)
    opponent_draw_card(player_hand, draw_pile, 4)
#endregion . . . . . . ________

# Game Start ✔
def start_game():
    face_up = draw_pile.pop(0)
    main_loop(player_hands, face_up, draw_pile, num_players)

# Play Validation ✔
def valid_play(card, face_up):
    return card[1] == face_up[1] or card[0] == face_up[0] or card[1] == "Black"

# Refresh draw_pile ✔
def refresh_draw_pile(face_up_pile, draw_pile):
    if not draw_pile:
        random.shuffle(face_up_pile)
        for card in face_up_pile: draw_pile.append(card)
        face_up_pile = []
        print("All cards in the Face Up pile have been reshuffled into the draw_pile.")

# Color changing ✔
def change_color(face_up):
    print("Choose the new color (enter index):")
    for color in colors: print(f"{colors.index(color) + 1}: {color}")
    chosen_index = int(input("Card index: ")) - 1
    
    if colors[chosen_index] == face_up[1]:
        print("New color cannot be the same as previous color. Please choose another color...")
        change_color()
    else: face_up = (face_up[0], colors[chosen_index])

# Call Uno
def call_UNO(player_hand):
    pass                           #CHANGE THIS

# Uno Penalty 
def penalize_no_uno_call(player_hand, draw_pile):
    pass                           #CHANGE THIS

def draw_card(player_hand, draw_pile, face_up):
    if draw_pile:
        print("You draw a card.")
        player_hand.append(draw_pile.pop(0))
    else:
        print("The draw pile is empty.")
        valid_cards = [card for card in player_hand if valid_play(card, face_up)]
        if valid_cards:
            print(f" But you have valid cards in your hand: {valid_cards}")
            print("You must play these cards to continue the game.")
            play_round(player_hand, face_up, draw_pile)
        else: 
            print(f"And you have no valid cards in your hand: {player_hand}")
            print("You skip your turn.")
            # SKIP IMPLEMENTATION


# Round Play ✔
def play_round(player_hand, face_up, draw_pile):
    valid_cards = [card for card in player_hand if valid_play(card, face_up)]
    if not valid_cards:
        print(f"You have no valid cards in your hand: {player_hand}")
        draw_card(player_hand, draw_pile, face_up)
    else:
        print("Choose a card to play (enter index):")
        for card in player_hand:
            print(f"{player_hand.index(card) + 1}: {card[1]} {card[0]}")
        chosen_index = int(input("Card index: ")) - 1
        chosen_card = player_hand[chosen_index]
        if valid_play(chosen_card, face_up):
            face_up = chosen_card
            player_hand.pop(chosen_index)
            
            print(f"You play the {chosen_card}")
            if   chosen_card[0] == "Wild Color Change": change_color(face_up)
            elif chosen_card[0] ==  "Wild Draw Four":   draw_four_color_change_card()
            elif chosen_card[0] ==     "Reverse":       reverse_card()
            elif chosen_card[0] ==      "Skip":         skip_card()
            elif chosen_card[0] ==       "+2":          opponent_draw_card(player_hand, draw_pile, 2)
        
        else:
            print("Invalid card. Start again.")
            play_round(player_hand)

# Main Game Loop
def main_loop(player_hands, face_up, draw_pile, num_players):
    global current # Again, just making my life easier :)
    current = 0
    while all(player_hands):
        refresh_draw_pile(face_up_pile, draw_pile)
        print(f"It is player {current + 1}'s turn.")
        print(f"The face up card is {face_up[1]} {face_up[0]}.")
        print(f"Player {current + 1}'s hand is {player_hands[current]}")
        play = input("Would you like to draw [0], play a card [1], play a card and call UNO! [2] or call someone out for not saying UNO! [3]? ")
        if play: play = int(play)
        else: 
            cls()
            main_loop(player_hands, face_up, draw_pile, num_players)
        
        if   play == 0: draw_card(player_hands[current], draw_pile, face_up)
        elif play == 1: play_round(face_up, player_hands[current], draw_pile)
        elif play == 2: call_UNO(face_up, player_hands[current], draw_pile)
        elif play == 3: penalize_no_uno_call(face_up, player_hands[current], draw_pile)
        
        current = ((current - 1) % num_players) if reverse_play else ((current + 1) % num_players)
        
        cls()

    for hand in player_hands:
        if not hand:
            exit(f"Player {player_hands.index(hand) + 1} has no more cards in their hand. They win!")
    
start_game()