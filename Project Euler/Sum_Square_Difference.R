# Project Euler Problem:
# The sum of the square of the first 10 natural numbers is -> 385.
i.square <- 0
for(i in 1:10) {
  i.square <- i.square + i^2
}

# The square of the sum of the first ten natural numbers is -> 3025
i.square_sum = 0
for(i in 1:10){
  i.square_sum <- i.square_sum + i
}
i.square_sum <- i.square_sum^2

# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 - 385 = 2640.

# Question <- Find the difference between the sum of the squares of the first 
#             one hundred natural numbers and the square of the sum.

# To solve the above we can simply increase the range from 1:10 -> 1:100.
i.square <- 0
for(i in 1:100) {
  i.square <- i.square + i^2
}

i.square_sum = 0
for(i in 1:100){
  i.square_sum <- i.square_sum + i
}
i.square_sum <- i.square_sum^2

sum_difference <- i.square_sum - i.square
cat(sum_difference)