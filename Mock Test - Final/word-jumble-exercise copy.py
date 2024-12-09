import random

print("Welcome to SF1 Word Jumble! Can you unscramble all the words? All of these terms are related to computer science and programming, and have been seen in class. Good luck!")

# Dictionary of words and their hints
word_list = {
    "python": "A programming language named after a snake",
    "github": "A web-based platform for version control",
    "dawson_college": "The best college in Montreal",
    "Eric_J_Mayhew": "An amazing teacher with a middlename still unknown...",
}
score = 0
max_attempts = 3

def scramble_word(self, word):
    """
    Takes a word and returns a scrambled version of it.
    Example: 'python' might become 'thopyn'
    """
    word_list = list(word)
    scrambled = word
    
    # Keep scrambling until we get a different arrangement
    while scrambled == word:
        random.shuffle(word_list)
        scrambled = ''.join(word_list)
    
    return scrambled

def play_round(self):
    """
    Plays a single round of the game.
    Returns True if player wins, False otherwise.
    """
    # Pick a random word and get its hint
    word = random.choice(list(self.word_list.keys()))
    hint = self.word_list[word]
    
    # Scramble the word
    jumbled = self.scramble_word(word)
    
    print("\nUnscramble this word:", jumbled)
    print("Hint:", hint)
    print(f"You have {self.max_attempts} attempts.")
    
    # TODO: Implement the guess checking logic here
    # The function should:
    # 1. Allow the player to make up to max_attempts guesses
    # 2. For each guess:
    #    - If correct, print "Correct!" and return True
    #    - If wrong, print "Try again!" and remaining attempts
    # 3. If all attempts used, print the correct word and return False
    #
    # Your code goes here:





def play_game(self):
    """
    Main game loop
    """
    print("Welcome to Word Jumble!")
    print("Try to guess the scrambled words.")
    
    while True:
        if self.play_round():
            self.score += 1
            print(f"Your score: {self.score}")
        
        play_again = input("\nPlay another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"\nFinal score: {self.score}")
    print("Thanks for playing!")

# Start the game
play_game()