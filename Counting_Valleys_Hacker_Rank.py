#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

#-----------------------------------------------------------------------------#
# Logic.
# If two consecutive U or D, then moved up a mountain or down a valley.
# If two U or D, then returned to sea level then two U or D add to mount/valley.

#-----------------------------------------------------------------------------#


def countingValleys(steps, path):
    # Write your code here
    valleys_walked = 0
    mountain = 0
    valley = 0

    for i in path:
        last_step = i[-1]

        if i == 'U' and :
            valley += 1
        else:
            mountain += 1

    #print(f'{valley} ++++ {mountain}')

    return valleys_walked

x = countingValleys(8, ['UDDDUDUU'])

print(x)
