#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    else:
        first_char = sentence[0]
    tuple_cr = (len(sentence), first_char)
    return tuple_cr
