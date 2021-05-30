''' PROJECT EULER: PROBLEM 27: QUADRATIC FORMULA:

'''

def quadratics(n, a, b):
    return ((n**2) + (a*b) + (b))

def is_prime(n):
    for i in range(2, n//2):
        if (n % i) == 0:
            return False
        else: # If n is not equally divis by any number, i.e. prime.
            return True

n_max, a_max, b_max, n_sequence = 0, 0, 0, 0
limits = 1000

for a in range(-limits, limits):
    for b in range(-limits, limits):
        while (abs(quadratics(n_sequence, a, b))):
            n_sequence += 1
        if (n_sequence > n_max):
            a_max = a
            b_max = b
            n_max = n_sequence





# end.
