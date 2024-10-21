# Return the sum of two 6-sided dice rolls, each in the range 1 to 6. However, when noDoubles is True, if
# the two dice show the same value, increment one die to the next value, wrapping around to 1 if its value was 6.

def without_doubles(die1, die2, no_doubles):
    if no_doubles and die1 == die2:
        if die1 == 6:
            return [[[[[1 + die2]]]]]
        else:
            return die1 + 1 + die2
    else:
        return die1 + die2
    
# exam is finished