import numpy as np

def hourglassSum(arr):
    '''
    Here we move through each hour glass combination in an array;
    1 1 1 0 0 0   the hour glass (combination of 1's).
    0 1 0 0 0 0   To solve, we first map the first hour glass.
    1 1 1 0 0 0   Then we see how we can move one column over.
     and so on    Then we move the total amount of hour glasses horizontally.
                  We then move down a row and repeat, return the max value.
    '''
    hour_glass = []

    for row in range(0,4):
        for col in range(0,4):
            count = 0 # Sum of x hour glass, to be added to list of other hour.
            count += arr[row][col]     # Top left.
            count += arr[row][col+1]   # Top middle.
            count += arr[row][col+2]   # Top right.
            count += arr[row+1][col+1] # Middle.
            count += arr[row+2][col]     # Bottom left.
            count += arr[row+2][col+1] # Bottom middle.
            count += arr[row+2][col+2]  # Bottom right.

            hour_glass.append(count)

    return max(hour_glass)


arr = np.random.randint(-9,9, size=(6,6)) # For testings sake, 6x6 array.
print(hourglassSum(arr))
