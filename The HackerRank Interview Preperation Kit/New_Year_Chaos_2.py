''' HACKER RANK PROBLEM: NEW YEAR CHAOS


'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    # The number of bribes received by any/all members in the line.
    bribes_recv = 0

    # If Person P had to bribe more than 2 people, the line is too chaotic.
    too_chaotic = 'Too Chaotic'






if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)






'''
    # Re-index.
    Q = [q.index(person)-1 for person in q]

    [print(f'{x} ... {y}') for x, y in enumerate(Q)]


    # Loop through the que (initial place in que, current place in que);
    for initial, current in enumerate(Q):
        # i is the original position/order of the line, 1,2....n
        # P is the current position of the person of interest.
        if current-initial > 2:
            print(too_chaotic)
            return
        elif current-initial < 0:
            # If we move one step to the 'left' we've bribed someone.
            bribes_recv += abs((current-initial))
'''





#end.
