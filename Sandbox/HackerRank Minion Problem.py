# Description:
# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules:
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# 
# Scoring:
# A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(s):
    vowels = "AEIOU"
    Stuart_score = 0
    Kevin_score = 0

    for i in range(len(s)): # i is the index of the letter whose substrings are being counted
        if s[i] in vowels: # if the letter is a vowel
            Kevin_score += len(s) - i # add the number of substrings that can be formed from s[i:] to Kevin's score
        else:
            Stuart_score += len(s) - i # add the number of substrings that can be formed from s[i:] to Stuart's score

    if Stuart_score > Kevin_score:
        print('Stuart', Stuart_score)
    elif Stuart_score < Kevin_score:
        print('Kevin', Kevin_score)
    else:
        print('Draw')

minion_game("BANANA")

# Output:
# Stuart 12
# (Kevin 9)

# Interesting solution. Calculates the number letters 'i' in any substring s[i:], checks if the the letter
# whose index is 'i' is a vowel or not, and adds the number of substrings that can be formed from s[i:] to the
# score of the player whose letter is a vowel. If the letter is not a vowel, the number of substrings that can be
# formed from s[i:] is added to the score of the player whose letter is not a vowel. The player with the highest
# score wins. If the scores are equal, it's a draw.