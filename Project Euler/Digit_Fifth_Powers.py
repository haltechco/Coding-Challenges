sum_powers = 0
i = 10 # 1**4 not included, i.e. any value < 10 not included.
arb_large = 500000

while i < arb_large:
    curr_digit = 0
    sep_digit = list(str(i)) # I.e. 113 becomes ['1', '1', '3']

    for ind_digit in sep_digit: # 1**5 + 1**5 + 1**3
        digit = int(ind_digit) ** 5
        curr_digit += digit

    if curr_digit == i:
        sum_powers += curr_digit
        print(curr_digit)

    i += 1

print(sum_powers)
