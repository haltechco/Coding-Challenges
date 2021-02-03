'''
A palindrome number reads the same both ways. The largest palindrom made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the prodcut of two 3-digit numbers.
'''

def is_palindrome(val):
    return str(val) == str(val)[::-1]

def search_values(lower, upper):
    adding = []
    # Searching for the largest palindrome for 999 * every values to 100
    #                                          998
    #                                          997...
    for x in range(upper, lower, -1):
        for y in range(upper, lower, -1):
            if is_palindrome(x*y) and x*y > 1:
                adding.append(x*y)
    return max(adding)

print(search_values(100,999))
