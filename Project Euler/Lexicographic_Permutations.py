'''PROJECT EULER: PROBLEM 24: LEXICOGRAPHIC PERMUTATIONS

A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1
and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''
from math import factorial
def perm(n, digits):
   if len(digits) == 1: return digits # Handling last sequence, i.e. 0.

   # 9! ... 8! ... 2! ... 1!
   int, rem = divmod(n, factorial(len(digits)-1))

   perm_seq = digits[int] + perm(rem, digits[:int] + digits[int+1:])

   return perm_seq


MILLIONTH = 999999 # Indexing
DIGITS = '0123456789'

print(f'1-MILLIONTH Permutation is: {perm(MILLIONTH, DIGITS)}')

# https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-024-solution/
# end.
