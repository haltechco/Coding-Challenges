# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

two_million <- 2e06

seive_of_ertosthenes <- function(n){
  # Algorithm of finding all primes up to a limit.
  sieve <- 2:n
  sieve_lmt <- sqrt(n)
  current_prime <- 2 
  
  while(current_prime < sieve_lmt){
    # Prime number if no integer division. 10 %% 2 = 0, 10 %% 3 = 1
    sieve <- sieve[ sieve %% current_prime != 0 | sieve == current_prime]
    # Find the current prime, then move to the next one. 
    current_prime <- sieve[which(sieve == current_prime) + 1]
  }
  return(sieve)
}

# Example of which : which((1:12)%%2 == 0) # which are even? Gives: 0,2,4,6...

print(sum(seive_of_ertosthenes(two_million)))