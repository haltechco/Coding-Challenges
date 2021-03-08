# Project Euler Coding Problem: Lattice Paths

# Proofs
# https://en.wikipedia.org/wiki/Lattice_path#Combinations_and_NE_lattice_paths
# https://en.wikipedia.org/wiki/Binomial_coefficient

# From Wolfram: The number of paths of length a+b from the origin (0,0) to a 
# point (a,b) which are restricted to east and north steps is given by the 
# binomial coefficient (a+b)
#                      ( a ).

# Binomial Coefficient:    (n) <-  n!/
#                          (k)     k!(n-k)!

# The binomial coefficient is the number of ways of picking unordered 
# outcomes from possibilities. In our case, the number of ways we can traverse
# the grid.

# Factorial: Product of all integers less than or equal to n (5!: 5x4x3x2x1=120)

nCk <- function(n, k){
  nCk <- factorial(n) / (factorial(k) * factorial(n-k))
  return(nCk)
}

# TEST 1: in a 2x2 grid;
cat("First test, expecting 6: result --> ", nCk(4,2))

# TEST 2: in a 20x20 grid: from (0,0) to (a,b) is C(a+b, a)
cat("Second test, a 20x20 grid has ", nCk(20+20, 20), " lattice paths.")

