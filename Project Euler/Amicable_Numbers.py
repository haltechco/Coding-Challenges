'''PROJECT EULER: PROBLEM 21: AMICABLE NUMBERS

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''
from functools import reduce


# Stack overflow snippet... sorted + list + sum + pop added.
def sum_factors(n):
    factors_of_n = 0
    factors_of_n = sorted(list(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    factors_of_n.pop() # Last element is n/1, not needed.
    return sum(factors_of_n)

ami_nums = []
da = db = 0

for i in list(range(2,10000)):
    da = sum_factors(i)
    db = sum_factors(da)
    if i == db:
        if da != db:
            ami_nums.append(da)

print(sum(ami_nums))





# end.
