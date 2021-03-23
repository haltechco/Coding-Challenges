#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    char_deletions = 0
    difference = {}

    for letter in a: # c, d, e
        if letter not in difference: # c, d, e not in dict, therefore = +1
            difference[letter] = 0
        difference[letter] += 1


    for letter in b: # a, b, c
        if letter not in difference: # a, b not in dict, therefore = +1
            difference[letter] = 0 # c is in dict, therefore = -1
        difference[letter] -= 1

    for n in difference.values():
        char_deletions += abs(n)

    return char_deletions

if __name__ == '__main__':

    a = 'fcrxzwscanmligyxyvym'

    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)

    print(str(res) + '\n')
