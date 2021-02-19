# Work out the first ten digits of the sum of the following one-hundred 
# 50-digit numbers.

data <- readLines("OneDrive\ -\ Queensland\ University\ of\ Technology/Eight\ Eight\ One/GitHub/Coding-Challenges/Project\ Euler/Largest_Sum_Data.txt")

data.matrix <- as.matrix(
                          c(strsplit(data, "")),
                          nrow = 1,
                          byrow = TRUE)


