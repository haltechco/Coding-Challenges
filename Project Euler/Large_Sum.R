# Work out the first ten digits of the sum of the following one-hundred 
# 50-digit numbers.

data_set <- readLines("OneDrive\ -\ Queensland\ University\ of\ Technology/Eight\ Eight\ One/GitHub/Coding-Challenges/Project\ Euler/Largest_Sum_Data.txt")

data_set.list <- c(strsplit(data_set, ""))

data_set.matrix <- matrix(unlist(data_set.list), ncol = 50)

holding_chars <- ""
count <- 0

for(rows in 1:100){ # 100, 50-digit numbers.
  for(cols in 1:50){ # Concatenating the 50-digit numbers.
    temp <- data_set.matrix[rows, cols]
    holding_chars <- paste(holding_chars, temp, sep = "")
  }
  count <- as.bigz(count + as.numeric(holding_chars))
}

count.char <- as.character(count)
print(substr(count.char, 1, 10)) # We only want to look at the first 10 values.













