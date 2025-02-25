class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = prefix_sum = 0
        odd_count = 0
        even_count = 1 # Start with 1 {0 is even}
        
        # For odd sum we need to add an even number and an odd number 
        # Track even and odd subarray sums with prefix_sum
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
            # when prefix is odd we increment count by even_count (since we start with even_count=1 current odd_count is also included)
                count += even_count
                odd_count += 1
            count %= MOD  
        return count
