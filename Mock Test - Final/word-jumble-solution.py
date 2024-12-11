import random

# Dictionary of words and their hints
word_list = {
    "python": "A programming language named after a snake",
    "coding": "The process of writing computer programs",
    "debug": "Finding and fixing errors in code",
    "function": "A reusable block of code",
    "variable": "A container for storing data"
}

def jumble_word(word):
    """Creates a jumbled version of the word"""
    # Convert word to list of characters
    word_chars = list(word)
    # Keep shuffling until we get a different arrangement
    scrambled = word
    while scrambled == word:
        random.shuffle(word_chars)
        scrambled = ''.join(word_chars)
    return scrambled

def play_game():
    # Initialize game variables
    lives = 3
    score = 0
    
    print("Welcome to Word Jumble!")
    
    # Main game loop
    while lives > 0:
        # Select random word and get its hint
        current_word = random.choice(list(word_list.keys()))
        current_hint = word_list[current_word]
        jumbled_word = jumble_word(current_word)
        
        # Get and check player's guess
        guess = input("Your guess: ").lower().strip()
        
        if guess == current_word:
            print("Correct!")
            score += 1
        else:
            lives -= 1
    
    # Game over message
    print(f"\nGame Over! Final score: {score}")

play_game()
