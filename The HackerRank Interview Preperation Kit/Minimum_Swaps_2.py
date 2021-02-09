import numpy as np
from numpy import random

def minimum_swaps(arr):
    # Swap current number with lowest number right of index.
    # Case: arr = [1,3,5,2,4,6,7]
    # Step 1:     [1,2,5,3,4,6,7] -> Swap 2 & 3
    # Step 2:     [1,2,3,5,4,6,7] -> Swap 3 & 5
    # Step 3:     [1,2,3,4,5,6,7] -> Swap 4 & 5
    # Logic:
        # No number right of '1' is lower, therefore in the correct position.
        # '3' is in the incorrect position, '2' is a lower number, swap.
        # '5' then needs to be swapped with the next lowest term.
        # '5' then again needs to be swapped with '4'.
        # We can see that after '5', the order ascends.

    swap_required = 0
    print(f'Raw Array: {arr}')

    for i, elem in enumerate(arr):
        # If current value is not the min of remaining to search, a swap is needed.
        while arr[i]-1 != i: # Until all elements are sorted.
            if arr[i] != min(arr[i:]):
                value = arr[i] # Value needing to change.
                # arr[value-1] value needing to change with arr[i].
                arr[value-1], arr[i] = arr[i], arr[value-1]
                swap_required += 1

    print(f'Sorted Array: {arr}')
    print(f'# of Swaps Required: {swap_required}')

    return swap_required



arr = random.randint(5, size=(10))
arr = [1,3,5,2,4,6,7]
minimum_swaps(arr)
