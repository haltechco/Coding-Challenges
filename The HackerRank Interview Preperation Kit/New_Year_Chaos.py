''' LOGIC:
Given a line of people, return how many bribes have been taken by any/all
people in the line.

Conditions:
    A person can only bribe and move forward.
    A person holds their number, i.e. q = [1,2,3], q = [1,3,2], 3 bribed 2.

Inputs:
    First line contains the number of test cases.
    Next two lines is;
        The number of people in the cue.
        List describing the final state of the que.
'''
import math

def minimum_bribes(q):

    # The number of bribes received by any/all members in the line.
    bribes_recv = 0

    # If Person P had to bribe more than 2 people, the line is too chaotic.
    too_chaotic = 'Too Chaotic'

    # Re-index.
    Q = [person-1 for person in q]

    # Loop through the que (initial place in que, current place in que);
    for initial,current in enumerate(Q):
        # i is the original position/order of the line, 1,2....n
        # P is the current position of the person of interest.
        print(f'Initial Pos: {initial} -- Current Pos: {current}')
        if current-initial > 2:
            print(too_chaotic)
            print(f'{current}# has moved to position {initial}#: {current-initial} bribes taken.')
            return
        elif current-initial <0:
            # If we move one step to the 'left' we've bribed someone.
            bribes_recv += abs((current-initial))

    bribes_recv += 1
    return bribes_recv


# This is the final state of the que.
q = [1,2,5,3,7,8,6,4]

print(minimum_bribes(q))
