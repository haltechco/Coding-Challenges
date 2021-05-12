''' PROJECT EULER: PROBLEM 20: FACTORIAL DIGIT SUM

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

VALUE_TO_FACTOR = 100

# Multiplication of top down, i.e. 10x9...2x1
def factorial_sum(n):
    fact_sum = 1

    for i in range(n,0,-1):
        fact_sum = fact_sum * i

    return fact_sum

# Seperate ^ into [3, 6, 2, 8, 8, 0, 0]
split_int_digits = [int(x) for x in str(factorial_sum(VALUE_TO_FACTOR))]

# 10! = 3628800 split and sum is 3+6+2+8+8+0+0 = 27
sum_split_digits = 0
for x in split_int_digits:
    sum_split_digits += x

# OUTPUT:
print(f'Sum of {VALUE_TO_FACTOR}! is {sum_split_digits}')
