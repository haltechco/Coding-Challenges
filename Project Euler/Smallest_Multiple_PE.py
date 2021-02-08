import time

'''
'''

def brute_foce_method(sample):
    start = time.time()
    smallest_even_divis = 0
    count = 1
    still_looking = True

    while still_looking:
        if  count%1 == 0 and count%2 == 0 and count%3 == 0 and \
            count%5 == 0 and count%6 == 0 and count%7 == 0 and \
            count%8 == 0 and count%9 == 0 and count%10 == 0 and \
            count%11 == 0 and count%12 == 0 and count%13 == 0 and \
            count%14 == 0 and count%15 == 0 and count%16 == 0 and \
            count%17 == 0 and count%18 == 0 and count%19 == 0 and \
            count%20 == 0:
            # Checking every number from 1-2 holds no remainder.
            smallest_even_divis = count
            still_looking = False

        count += 1
    sum_time = time.time() - start

    return smallest_even_divis, sum_time

sample = list(range(1,20))
BFM = brute_foce_method(sample[0])
print(f'BFM:_________________________________________\n \
       Smallest evenly divisible number (1-20):{BFM[0]} \
       \nFunction run time: {BFM[1]:.2f} seconds.')
