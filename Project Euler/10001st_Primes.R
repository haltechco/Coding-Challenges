# Project Euler Program:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.

# Question: What is the 10,001st prime number?

# A prime number is that, that is only divisible by itself and 1.

# Create a list of prime numbers, once the list reaches 10,001, end. 
# 10,001 prime is prime_number_list[-1]


primes_upto <- function(limit){
  prime_list_upto <- seq(2, limit) # List of numbers from 2 -> limit.
  prime_nums <- c()      # To be amended with primes.
  
  # Finds all the prime numbers up to the limit.
  for(i in seq(2, limit)){
    if(any(prime_list_upto == i)){ # If i is within the bounds.
      # Amend i to prime list if it is a prime.
      prime_list_upto = c(prime_list_upto[(prime_list_upto %% i) != 0], i)
    }
  }
  return(prime_list_upto)
}

# Inefficient: find a way to loop until the length of the data set is 10,001.
# Therefore, we have found 10,001 primes & data_set[length(data_set)] is last value.
data_set <- primes_upto(150000)
cat("The 10,001st primes number is: ", data_set[10001])