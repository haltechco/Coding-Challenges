# PROJECT EULER: PROBLEM 19: COUNTING SUNDAYS

# You are given the following information, but you may prefer to do some 
# research for yourself.

    # 1 Jan 1900 was a Monday.
    
    # Thirty days has September, April, June and November. All the rest have 
    # thirty-one, Saving February alone, Which has twenty-eight, rain or shine. 
    # And on leap years, twenty-nine.
    
    # A leap year occurs on any year evenly divisible by 4, 
    # but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth 
# century (1 Jan 1901 to 31 Dec 2000)?
  
# Start with calendar data?

count_sundays <- function(){
  counter <- 0
  # Move through the years:
  for(yr in 1901:2000){
    # Move through the months:
    for(mth in 1:12){
      date_of_interest <- sprintf("%s-%s-01", yr, mth)
      if(as.POSIXlt(date_of_interest)$wday == 0){
        counter <- counter + 1
      }
    }
  }
  return(counter)
}

sprintf("The number of Sundays falling on the first of the month in the twentieth century is %s days.", count_sundays())
