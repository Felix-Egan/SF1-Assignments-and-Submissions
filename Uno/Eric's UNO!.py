# Imports 
import random
import os
import time
cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Pregame constants (Note that the number of cards has been adjusted to the actual game's card count = 108) 
face_up_pile = []
colors = ["Red", "Yellow", "Blue", "Green"]
digits = ["+2", "+2", "Reverse", "Reverse", "Skip", "Skip"]
digits.extend(list(range(10)) + list(range(1, 10)))
digits = [str(digit) for digit in digits]
draw_pile = [(digit, color) for digit in digits for color in colors] # Renamed deck to draw_pile for convenience and readibility
wild_cards = [("Wild Color Change", "Black"), ("Wild Draw Four", "Black")]
draw_pile.extend(wild_cards * 4)
random.shuffle(draw_pile)
reverse_play = False
players_called_UNO = []
penalizable_players = []
cls()
print("""
As Eric said many times, we were tasked with making a simplified version of UNO, to which I gladly responded with "Respectfully, no." so I made a full-fledged version of UNO instead! (I have not slept in 3 days 👍)
This version works in a very similar fashion to the normal UNO game we all love (until someone starts with 4 wild cards and we all want to do is scare them while they are drinking a glass of juice so it splashes all over
their clothes... Yeah, I see you Antonin!!!). This version only DOESN'T include the following features that UNO players sometimes implement, mainly: NO Stacking +2s and +4s, NO Reversing a +2 or +4 (otherwise known as the
ULTIMATE UNO REVERSE!!!), and finally +2s and +4s do NOT skip turns in this version. I don't even know why that's a considered rule to begin with! Anyways, have fun! Max playercount of *15* btw, otherwise things break :/
""")
input("""
PS: I've done my very best to squeeze out any potential bugs and hiccups that might arise. If ever a bug does show up, please leave a comment in the code somewhere and send it back
to me so I can look back with veteran eyes at the countless hours of sleep I missed out on to make this script.
Press Enter to continue...""")
num_players = int(input("Enter number of players: ")) 
cls()
player_hands = [[draw_pile.pop(0) for i in range(7)] for i in range(num_players)]

# Special Cards 
def reverse_card():
    global reverse_play # Sorry for using global variables Eric. They just make my life so much easier for this script ¯\(ツ)/¯ Plus its just a boolean... It shouldn't break anything
    reverse_play = not reverse_play
    print("The order of play is now reversed!")

def skip_card(current_player):
    print(f"Player{(current_player - 1) % num_players if reverse_play else (current_player + 1) % num_players} skips their turn")
    current_player = ((current_player - 1) % num_players) if reverse_play else ((current_player + 1) % num_players)
    return current_player

def opponent_draw_card(player_hands, current_player, draw_pile, card_draw_count):
    for i in range(card_draw_count):
        if draw_pile:
            print("Your opponent draws a card.")
            if not reverse_play: player_hands[(current_player + 1) % num_players].append(draw_pile.pop(0))
            else: player_hands[(current_player - 1) % num_players].append(draw_pile.pop(0))
        else:
            print("The draw pile is empty, so your opponent picks up no cards.")

def draw_four_color_change_card(current_player, draw_pile, face_up):
    face_up = change_color(face_up)
    opponent_draw_card(player_hands, current_player, draw_pile, 4)
    return face_up

# Game Start 
def start_game():
    face_up = draw_pile.pop(0)
    face_up_pile.append(face_up)
    if face_up[1] == "Black":
        face_up_pile.append(face_up)
        start_game()
    current_player = 0
    main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player)

# Play Validation 
def valid_play(card, face_up):
    return card[1] == face_up[1] or card[0] == face_up[0] or card[1] == "Black"

# Refresh draw_pile 
def refresh_draw_pile(face_up_pile, draw_pile):
    if not draw_pile:
        random.shuffle(face_up_pile)
        for card in face_up_pile: draw_pile.append(card)
        face_up_pile = []
        print("All cards in the Face Up pile have been reshuffled into the draw_pile.")

# Color changing 
def change_color(face_up):
    print("Choose the new color (enter index):")
    for color in colors: 
        print(f"{colors.index(color) + 1}: {color}")
    chosen_index = int(input("Card index: ")) - 1
    print(f"The new color is {colors[chosen_index]}")
    face_up = (face_up[0], colors[chosen_index])
    return face_up

# Call Uno 
def play_call_UNO(player_hand, face_up, draw_pile, current_player):
    round_results = play_round(player_hands[current_player], face_up, draw_pile, current_player)
    face_up = round_results[0]
    current_player = round_results[1]
    players_called_UNO.append(f"Player{current_player+1}")
    print(f"Player {current_player + 1} called UNO!")
    return face_up

# Draw a card 
def draw_card(player_hand, face_up, draw_pile, current_player):
    if draw_pile:
        print("You draw a card.")
        player_hand.append(draw_pile.pop(0))
    else:
        print("The draw pile is empty.")
        valid_cards = [card for card in player_hand if valid_play(card, face_up)]
        if valid_cards:
            print(f" But you have valid cards in your hand: {valid_cards}")
            print("You must play these cards to continue the game.")
            play_round(player_hand, face_up, draw_pile, current_player)
        else: 
            print(f"And you have no valid cards in your hand: {player_hand}")
            print("You skip your turn.")

# Round Play 
def play_round(player_hand, face_up, draw_pile, current_player):
    valid_cards = [card for card in player_hand if valid_play(card, face_up)]
    if not valid_cards:
        print(f"You have no valid cards in your hand: {player_hand}")
        draw_card(player_hand, face_up, draw_pile, current_player)
    else:
        print("Choose a card to play (enter index):")
        for card in player_hand:
            print(f"{player_hand.index(card) + 1}: {card[0]} {card[1]}")
        chosen_index = int(input("Card index: ")) - 1
        chosen_card = player_hand[chosen_index]
        if valid_play(chosen_card, face_up):
            player_hand.pop(chosen_index)
            face_up = chosen_card
            face_up_pile.append(face_up)
            print(f"You play the {chosen_card}")
            if   chosen_card[0] == "Wild Color Change": face_up = change_color(face_up)
            elif chosen_card[0] == "Wild Draw Four":  face_up = draw_four_color_change_card(current_player, draw_pile, face_up)
            elif chosen_card[0] == "Reverse": reverse_card()
            elif chosen_card[0] == "Skip": current_player = skip_card(current_player)
            elif chosen_card[0] == "+2": opponent_draw_card(player_hands, current_player, draw_pile, 2)
        else:
            print("Invalid card. Start again.")
            play_round(player_hand, face_up, draw_pile, current_player)
    return [face_up, current_player]

def manage_UNO_players(player_hands):
    for player in players_called_UNO:
        if player_hands[{int(player.split('Player')[1]) - 1}] != 1: players_called_UNO.remove(player)

# Main Game Loop
def main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player):
    while all(player_hands):
        refresh_draw_pile(face_up_pile, draw_pile)
        manage_UNO_players(player_hands)
        player_card_count = [f"Player{i+1}: {len(player_hands[i])} [{'UNO!' if f'Player{i+1}' in players_called_UNO else ''}]" for i in range(num_players)]
        print(player_card_count)
        print(f"It is player {current_player + 1}'s turn.")
        print(f"The face up card is {face_up[0]} {face_up[1]}.")
        print(f"Player {current_player + 1}'s hand is {player_hands[current_player]}")
        play = input("Would you like to draw [0], play a card [1], play a card and call UNO! [2] or call someone out for not calling UNO! [3]? ")
        if play: play = int(play)
        else:
            print("Please enter an index...")
            main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player)
        if 0 > play <3: 
            print("Please enter a valid index...")
            main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player)
        
        if play == 0: 
            if not draw_pile:
                print("The draw pile is empty.")
                valid_cards = [card for card in player_hand if valid_play(card, face_up)]
                if valid_cards:
                    print(f" But you have valid cards in your hand: {valid_cards}")
                    print("You must play these cards to continue the game.")
                    round_results = play_round(player_hands[current_player], face_up, draw_pile, current_player)
                    face_up = round_results[0]
                    current_player = round_results[1]
                else: 
                    print(f"And you have no valid cards in your hand: {player_hand}")
                    print("You skip your turn.")
            else:
                draw_card(player_hands[current_player], face_up, draw_pile, current_player)
        
        
        elif play == 1: 
            round_results = play_round(player_hands[current_player], face_up, draw_pile, current_player)
            face_up = round_results[0]
            current_player = round_results[1]
       
       
        elif play == 2: 
            if len(player_hands[current_player]) == 2 and [card for card in player_hands[current_player] if valid_play(card, face_up)]: 
                face_up = play_call_UNO(player_hands[current_player], face_up, draw_pile)[0]
                current_player = play_call_UNO(player_hands[current_player], face_up, draw_pile)[1]
            else:
                print("You are unable to call UNO! just yet. Please enter a valid index...")
                main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player)
        
        
        elif play == 3: 
            for player_hand in player_hands: 
                if len(player_hand) == 1 and f"Player{player_hands.index(player_hand) + 1}" not in players_called_UNO: penalizable_players.append(f"Player{player_hands.index(player_hand) + 1}")
            if not penalizable_players:
                print("There are no penalizable players. Please enter a valid index...")
                main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player)
            else:
                print("Choose a player to penalize:")
                for player in penalizable_players:
                    print(f"{penalizable_players.index(player) + 1}: {player}")
                chosen_index = int(input("Card index: ")) - 1
                chosen_player = penalizable_players[chosen_index]
                print(f"{chosen_player} forgot to call UNO! and YOU caught them! They draw 2 cards.")
                for i in range(2):
                    player_hands[int(chosen_player.split('Player')[1]) - 1].append(draw_pile.pop(0))
            penalizable_players.clear()
            main_loop(player_hands, face_up, draw_pile, face_up_pile, num_players, current_player)

        current_player = ((current_player - 1) % num_players) if reverse_play else ((current_player + 1) % num_players)
        time.sleep(1)
        cls()
    for player_hand in player_hands:
        if not player_hand:
            exit(f"Player {player_hands.index(player_hand) + 1} has no more cards in their hand. They win!")
    
start_game()