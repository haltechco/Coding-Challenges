''' PROJECT EULER: PROBLEM 28: NUMBER SPIRAL DIAGONALS

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?

'''

def spiral_corners_sum(n):
    sum_corners = 1
    odd_step = 2 # To step through odd nums, as we know our corners are odd.

    for x in range(3, n+1, odd_step):
        # Using func from http://www.javaproblems.com/2013/11/project-euler-problem-28-number-spiral_27.html
        sum_corners += (4 * x * x - 6 * (x - 1))

    return sum_corners

print(spiral_corners_sum(1001))












# end.
