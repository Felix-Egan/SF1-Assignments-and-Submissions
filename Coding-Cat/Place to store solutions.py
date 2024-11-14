# etherial => aeehilrt
#sorted & sort is banned

def aplhabetical_order(word):
    word = list(word)
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] > word[j]:
                word[i], word[j] = word[j], word[i]
    return ''.join(word)

print(aplhabetical_order('etherial'))
print(aplhabetical_order('popperfish'))
print(aplhabetical_order('codingcat'))
print(aplhabetical_order('python'))
print(aplhabetical_order('java'))