# def remove_vowels(word: str) -> str:
#     vowels = "aeiouyAEIOUY"
#     vowels_and_spaces = vowels + " "
#     result = ""
#     if len(word) <= 10:
#         for letter in word:
#             if letter not in vowels:
#                 result += letter        
#         return result
#     else:
#         for letter in word:
#             if letter in vowels_and_spaces:
#                 result += letter
#     return result

def remove_vowels(word: str, y_is_a_vowel: bool) -> str:
    vowels = "aeiouAEIOU"
    vowels += "yY" if y_is_a_vowel else ""
    result = ""
    for letter in word or letter == " ":
        if letter not in vowels:
            result += letter
    return result


# print(remove_vowels(input("Enter a word: "), True if input("Is 'y' a vowel? (y/N) (Default = Yes, because, it is. Why is this even a debate?): ") == "y" or "" else False))