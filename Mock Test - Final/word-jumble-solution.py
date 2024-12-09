import random

class WordJumble:
    def __init__(self):
        # Dictionary of words and their hints
        self.word_list = {
            "python": "A programming language named after a snake",
            "coding": "The process of writing computer programs",
            "debug": "Finding and fixing errors in code",
            "function": "A reusable block of code",
            "variable": "A container for storing data"
        }
        self.score = 0
        self.max_attempts = 3

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
        
        # Allow up to max_attempts guesses
        for attempt in range(self.max_attempts):
            guess = input(f"\nAttempt {attempt + 1}, your guess: ").lower().strip()
            
            if guess == word.lower():
                print("Correct! You got it!")
                return True
            else:
                remaining = self.max_attempts - (attempt + 1)
                if remaining > 0:
                    print(f"Wrong! {remaining} attempts remaining.")
                else:
                    print(f"Sorry! The word was: {word}")
        
        return False

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
if __name__ == "__main__":
    game = WordJumble()
    game.play_game()
