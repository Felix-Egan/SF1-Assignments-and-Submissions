import random

def scramble_word(word):
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

def display_lives(lives):
    """
    Displays the current number of lives as hearts
    """
    return "❤️ " * lives + "🖤 " * (5 - lives)

def play_round(lives):
    """
    Plays a single round of the game.
    Returns tuple of (bool for win/loss, remaining lives)
    """
    # Pick a random word and get its hint
    word = random.choice(list(word_list.keys()))
    hint = word_list[word]
    
    # Scramble the word
    jumbled = scramble_word(word)
    
    print("\nUnscramble this word:", jumbled)
    print("Hint:", hint)
    
    guess = input("\nYour guess: ").lower().strip()
        
    if guess == word:
        print("Correct! You got it!")
        return True, lives
    else:
        lives -= 1
        print(f"Wrong! The word was: {word}")
        print(f"Lives remaining: {display_lives(lives)}")
        return False, lives

def play_game():
    """
    Main game loop
    """
    score = 0
    lives = 5
    
    print("Welcome to SF1 Word Jumble! Can you unscramble all the words? All of these terms are related to computer science and programming, and have been seen in class. Good luck!")
    print(f"You have 5 lives: {display_lives(lives)} Each wrong guess costs one life.")
    print("Try to guess as many words as you can before running out of lives!")
    
    while lives > 0:
        won, lives = play_round(lives)
        if won:
            score += 1
            print(f"Your score: {score}")
    
    if lives == 0:
        print("\nGame Over! You've run out of lives!")
    
    print(f"\nFinal score: {score}")
    print("Thanks for playing!")

# Dictionary of words and their hints
word_list = {
    "python": "A programming language named after a snake",
    "github": "A web-based platform for version control",
    "git": "A distributed version control system",
    "CPU": "Central Processing Unit",
    "RAM": "Random Access Memory",
    "motherboard": "The main circuit board of a computer",
    "hard_drive": "A device for storing digital data",
    "solid_state_drive": "A storage device that uses flash memory",
    "network": "A group of interconnected computers",
    "packet": "A unit of data transmitted over a network",
    "remote_origin": "A default name for the remote repository",
    "branch": "A parallel version of a repository",
    "merge": "To combine two or more branches",
    "pull_request": "A request to merge changes into a repository",
    "git_clone": "To copy a repository from a remote source",
    "git_commit": "To record changes to a repository",
    "git_push": "To upload changes to a remote repository",
    "git_pull": "To fetch and download changes from a remote repository",
    "git_fetch": "To download changes from a remote repository",
    "rebase": "To apply changes from one branch to another",
    "repository": "A location where files are stored",
    "commit": "A saved change in a repository",
    "git_branch": "To create a new branch",
    "router": "A device that forwards data packets between computer networks",
    "node": "A device connected to a network",
    "ISP": "Internet Service Provider",
    "linkrot": "The process by which links on a website become broken",
    "ip_address": "A unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network",
    "DNS": "Domain Name System",
    "tcp_handshake": "The process of establishing a connection between two computers",
    "http": "Hypertext Transfer Protocol",
    "curl": "A command-line tool for transferring data with URLs",
    "html": "Hypertext Markup Language",
    "ssh": "Secure Shell",
    "transistor": "A semiconductor device used to amplify or switch electronic signals",
    "binary": "A number system with a base of 2 (0s and 1s)",
    "integrated_circuit": "A set of electronic circuits on one small flat piece of semiconductor material",
    "logic_gate": "A device that performs a basic operation on electrical signals",
    "kernel": "The core component of an operating system",
    "FOSS": "Free and Open Source Software",
    "lookup_table": "A data structure used to store key-value pairs",
    "tracing": "A method of debugging code by printing messages to a log",
    "boolean": "A data type with two possible values: True or False",
    "data": "Information in a form suitable for use with a computer (e.g., numbers, text, images, boolean values, etc...)",
    "function": "A block of code that performs a specific task",
    "append": "To add an element to the end of a list",
    "insert": "To add an element at a specific index in a list",
    "remove": "To delete an element from a list",
    "pop": "To remove and return the last element from a list",
    "index": "The position of an element in a list",
    "list": "A collection of items in a specific order",
    "tuple": "An immutable collection of items",
    "vim": "A highly configurable text editor (that everyone despises)",
    "silicon": "A material used in the production of semiconductors and integrated circuits",
    "trace_route": "A network diagnostic tool that shows the path of data packets",
    "Eric_J_Mayhew": "An amazing teacher with a middle name still unknown...",
}
# Start the game
play_game()