# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                                 a^2 + b^2 = c^2.
#
# For example; 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Calculating Pythag Triplets: 
a <- b <- c <- 0
abc_sum <- 1000

a_poss <- floor(abc_sum/3) # a < b < c implies a can only be a third of sum(abc)
b_poss <- floor(abc_sum/2) # same logic for b

flag <- FALSE

BFM <- function(target){
# Brute force method. For all possibilities of a, b & c search until condition met.
  for(a in 1:floor(999/3)){   # For a < b < c: a has to be 1/3 of sum(a,b,c)
    for(b in 1:floor(999/2)){ # & b has to be 1/2 of sum(a,b,c)
      for(c in 1:999){
        a_sqd <- a^2
        b_sqd <- b^2
        c_sqd <- c^2
        if(a_sqd + b_sqd == c_sqd){ # If we've found a pythag triplet.
          abc_sum = a + b + c
          if(abc_sum == target){ # However, need to check if its the one were looking for.
            cat("A: ", a, "\nB: ", b, "\nC: ", c, "\n")
            return(prod(a,b,c))
          }
        }
      }
    }
  }
}

cat(BFM(1000))








