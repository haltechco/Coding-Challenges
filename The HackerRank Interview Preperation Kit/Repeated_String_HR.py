def repeated_string(s, n):

    occur_a = 0 # Updated as we find each occurance of a[str].

    if s == 'a': # If there is only 'a' within the string no need to search.
        occur_a = n
    else:
        num_repeats = (n // len(s)) + 1 # Number to multiply, edge to be cut off
        string_repeated = s * num_repeats # Multiplying with excess
        string_repeated = string_repeated[:n] # Removing excess

        occur_a = string_repeated.count('a')

    return occur_a

s = 'aba'
print(repeated_string(s, 10))
