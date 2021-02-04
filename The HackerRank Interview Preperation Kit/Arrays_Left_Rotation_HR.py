def rotate_left(a,d):

    a_shifted = a
    rotate_to_start = d/len(a)
    count = 0

    if rotate_to_start.is_integer():#If the number of rotations is equal to the
        return a #length of the array, we always shift to our starting position.

    while count < n:
        move_index = a.pop(0)
        a_shifted.append(move_index)
        count += 1

    return a_shifted

n = 23
a = [1,2,3,4,5,6,3,4,1,123]

print(rotate_left(a,n))
