#region: Imports ✔
import random
import os
cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#endregion

#region: Pregame constants (Note that the number of cards has been adjusted to the actual game's card count = 108) ✔
face_up_pile = []
colors = ["Red", "Yellow", "Blue", "Green"]
digits = ["+2", "+2", "Reverse", "Reverse", "Skip", "Skip"]
digits.extend(list(range(10), list(range(1, 10))))
draw_pile = [(digit, color) for digit in digits for color in colors]
wild_cards = [("Wild Color Change", "Black"), ("Wild Draw Four", "Black")]
draw_pile.extend(wild_cards * 4)
random.shuffle(draw_pile)
reverse_play = False
players_called_UNO = []
#endregion

#region:Special Cards  ________
def reverse_card():
    pass                           #CHANGE THIS

def skip_card():
    pass                           #CHANGE THIS

def draw_2_card():
    pass                           #CHANGE THIS

def color_change_card():
    pass                           #CHANGE THIS

def draw_four_color_change_card():
    pass                           #CHANGE THIS
#endregion . . . . . . ________

# Game Start ✔
def start_game():
    num_players = int(input("Enter number of players: ")) #
    player_hands = [[draw_pile(0)  for i in range(7)] for i in range(num_players)] # generate a hand for each player
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
def choose_color(face_up):
    print("Choose a card to play (enter index):")
    for color in colors:
        print(f"{colors.index(color) + 1}: {color}")
    chosen_index = int(input("Card index: ")) - 1
    return colors[chosen_index]

# Call Uno
def call_UNO(player):
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
            print(f"You have valid cards in your hand: {valid_cards}")
            print("You must play these cards to continue the game.")
            play_round(player_hand, face_up, draw_pile)
        else: 
            print(f"You have no valid cards in your hand: {player_hand}")
            print("You skip your turn.")
            SKIP IMPLEMENTATION


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
            if chosen_card[0] == "Wild Color Change": color_change_card()
            elif chosen_card[0] == "Wild Draw Four": draw_four_color_change_card()
            elif chosen_card[0] == "Reverse": reverse_card()
            elif chosen_card[0] == "Skip": skip_card()
        
        else:
            print("Invalid card. Start again.")
            play_round(player_hand)

# If all() is banned ✔
def all_value(list1):
  value_counter = 0
  for item in list1:
    if item: value_counter += 1
  return value_counter == len(list1)

# Main Game Loop
def main_loop(player_hands, face_up, draw_pile, num_players):
    current = 0
    while all(player_hands):    # while all_value(player_hands)
        print(f"It is player {current + 1}'s turn.")
        print(f"The face up card is {face_up[1]} {face_up[0]}.")
        print(f"Player {current + 1}'s hand is {player_hands[current]}")
        play = int(input("Would you like to draw [0], play a card [1], play a card and call UNO! [2] or call someone out for not saying UNO! [3]? "))
        
        if play == 0: draw_card(player_hands[current], draw_pile, face_up)
        elif play == 1: play_round(face_up, player_hands[current], draw_pile)
        elif play == 2: call_UNO(face_up, player_hands[current], draw_pile)
        elif play == 3: penalize_no_uno_call(face_up, player_hands[current], draw_pile)
        
        current = ((current - 1) % num_players) if reverse_play else ((current + 1) % num_players)
        
        cls()

    for hand in player_hands:
        if not hand:
            exit(f"Player {player_hands.index(hand) + 1} has no more cards in their hand. They win!")
    
start_game()