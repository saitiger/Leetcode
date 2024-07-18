BRUTE FORCE SOLUTION GIVES TLE NEED TO FIND A BETTER SOLUTION!

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        total_sum = 0

        for i in range(n):
            for j in range(i, n):
                min_val = min(arr[i:j+1])
                total_sum += min_val
                total_sum %= mod

        return total_sum
