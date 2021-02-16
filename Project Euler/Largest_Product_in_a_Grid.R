# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# Take directory path from terminal and copy into below.
square <- as.matrix(read.delim("OneDrive\ -\ Queensland\ University\ of\ Technology/Eight\ Eight\ One/GitHub/Coding-Challenges/Project\ Euler/Largest_Product_in_a_Grid_Data.txt", header = FALSE, sep = " "))

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20×20 grid?

BFM <- function(){
  # We want to look at the sum of four adjacent number in the above directions;
  # square[ROW, COLUMN]
  #
  # For vertical, starting at row 1 -> (1,1) * (2,1) * (3,1) * (4,1)
  #                      then row 2 -> (2,1) * (3,1) * (4,1) * (5,1)...
  #         row 3, up to limit (20) -> (17,1) * (18,1) * (19,1) * (20,1)
  # Flip the above logic of row and column for horizontal.
  #
  # For vertically, we are moving up and right.
  #            and we are moving down and left.
  #
  prod.vertical <- square[1:17, ] * square[2:18, ] * square[3:19, ] * square[4:20, ]
  prod.horizont <- square[, 1:17] * square[, 2:18] * square[, 3:19] * square[, 4:20]
  prod.diag_L_R <- square[1:17,1:17] * square[2:18,2:18] * square[3:19,3:19] * square[4:20,4:20]
  prod.diag_R_L <- square[4:20,1:17] * square[3:19,2:18] * square[2:18,3:19] * square[1:17,4:20]
  
  largest_of_adj <- max(prod.vertical, prod.vertical, prod.diag_L_R, prod.diag_R_L)
  return(largest_of_adj)
}

cat(BFM())
