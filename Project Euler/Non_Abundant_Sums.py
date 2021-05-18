'''PROJECT EULER: PROBLEM 23: NON-ABUNDANT SUMS

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However, this
upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.

'''
from functools import reduce
from tqdm import tqdm

# Code taken from Problem 21;
# Sums the divisors/factors of n, i.e. 28 = 1+2+4+7+14
def sum_factors(n):
    factors_of_n = 0
    factors_of_n = sorted(list(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    factors_of_n.pop() # Last element is n/1, not needed.
    return sum(factors_of_n)


def solve():
    n_abundant = [] # Hold all abundant numbers upto the upper bound
    upper_bound = 28123 # Upper bound/limit
    ans = 0 # Add to when ai + aj does not = n
    scope_to_search = tqdm(list(range(12, upper_bound+1)))

    for n in scope_to_search:
        # Create our list of abundant numbers
        if sum_factors(n) > n:
            n_abundant.append(n)

        # Here we want to see if n cannot be written as the sum of two abundant numbers.
        if not any((n-a in n_abundant) for a in n_abundant):
            ans += n

    return ans



print(solve())










# end.
