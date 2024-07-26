class Solution:
    def pivotInteger(self, n: int) -> int:
        # Brute Force 
        for i in range(1, n + 1):
            sum_left = sum(range(1, i + 1)) 
            sum_right = sum(range(i, n + 1)) 

            if sum_left == sum_right:
                return i  
        return -1  

        # Two Pointer 
        if n == 1:
            return 1
        l = 1
        r = n
        left_sum = 1
        right_sum = n
        
        while l<r:
            if left_sum < right_sum:
                l+= 1
                left_sum += l
            else:
                r-= 1
                right_sum += r
        
        return l if left_sum == right_sum else -1

        #Math

        import math
        if n == 1:
            return 1
        total_sum = n * (n + 1) // 2
        pivot = int(math.sqrt(total_sum))
        return pivot if pivot * pivot == total_sum else -1
