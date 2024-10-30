def remove_vowels(word: str) -> str:
    vowels = "aeiouyAEIOUY"
    vowels_and_spaces = vowels + " "
    result = ""
    if len(word) <= 10:
        for letter in word:
            if letter not in vowels:
                result += letter        
        return result
    else:
        for letter in word:
            if letter in vowels_and_spaces:
                result += letter
    return result

print(remove_vowels(input("Remove Vowels if len<11 : ")))