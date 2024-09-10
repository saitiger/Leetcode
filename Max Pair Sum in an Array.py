class Solution:
    def maxSum(self, nums):
        maxNumForDigit = [0] * 10 # Array which stores the numbers associated with the max digit
        ans = -1
        for num in nums:
            maxD = 0
            temp = num
            # Calculating the max digit for each number 
            while temp:
                maxD = max(maxD, temp % 10)
                temp //= 10
            
            if maxNumForDigit[maxD]:
                ans = max(ans, maxNumForDigit[maxD] + num) 
            
            if num > maxNumForDigit[maxD]: # Add the bigger number to the array since we want max sum 
                maxNumForDigit[maxD] = num
        
        return ans
