# The following iterative sequence is defined for the set of positive integers:
  
# Function One:  n → n/2 (n is even)
# Function Two: n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
  
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
  
#  NOTE: Once the chain starts the terms are allowed to go above one million.
time.start <- Sys.time()
library(gmp)

###############################################################################
func.collatz_chain <- function(n){
  longest_seq <- vector() # Assigning the list to hold the sequence of numbers.
  i <- 1
  while(n != 1){ # If our current chain reaches 1, i.e. ends.
    if(n %% 2 == 0){
      n <- n/2
    }else{
      n <- 3*n + 1
    }
    longest_seq[i] <- n
    i <- i + 1
  }
  return(longest_seq)           
}
###############################################################################


###############################################################################
one_million <- 1E6
collatz_chain.max <- 0
collatz_chain.starting_num <- 0

for(i in 1:one_million){
  collatz_chain.length <- length(func.collatz_chain(i))
  if(collatz_chain.length > collatz_chain.max){ # Found our new largest chain.
    collatz_chain.starting_num <- i
    collatz_chain.max <- collatz_chain.length
  }
}
###############################################################################


###############################################################################
cat(paste0("Starting number to produce the longest sequence: ", collatz_chain.starting_num))
cat(paste0("Of length: ", collatz_chain.max, " numbers. \n"))

time.end <- Sys.time()
print(time.end - time.start)
###############################################################################
