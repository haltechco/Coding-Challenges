int_combinations = set() # We use a set as to eliminate duplicates.

for a in list(range(2,100+1)): # For 2 <= a <= 5.
    for b in list(range(2,100+1)): # As above.
        aB = a**b
        int_combinations.add(aB) # Adding to distinc terms, no duplicates added.

int_combinations = sorted(int_combinations) # Sorted set of distinct terms.

print(len(int_combinations)) # To show us the # of distinct terms.
# end.
