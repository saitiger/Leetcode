class Solution:
# Find the largest power of three that fits in the 32-bit integer space.
  max_int = 2**31 - 1
  power = 1 
  while power * 3 <= max_int:
    power *= 3
  largest_num = power

# Have to calculate the largest_num and can't do the logarithmic solution due to floating point precision.
# The log solution works for powers that are even since the numbers are stored in 2-bit format 
  
largest_power_of_three()
    def isPowerOfThree(self, n: int) -> bool:
        # return n>0 and log(n,3)%1==0
        if n<=0:
            return False
        return n > 0 and largest_num%n==0        
