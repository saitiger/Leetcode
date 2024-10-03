class Solution:
    def canArrange(self, arr, k):
        remainder_count = defaultdict(int)
        for i in arr:
            remainder_count[i%k]+=1
        for i in arr:
            rem = i%k
            if rem == 0:
                if remainder_count[rem] % 2 == 1: # Check if remainder zero has even count else False
                    return False
            elif remainder_count[rem] != remainder_count.get(k - rem, 0): # Check if rem and its valid pair (k-rem) has the same count if not then one of the pairs will not have its valid pair 
                return False
        return True

# Solution 2 Credit Leetcode Editorial 
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted(arr, key=lambda x: x%k)

        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] % k != 0:
                break # If the first remainder is not zero start the two pointer approach
            if arr[start + 1] % k != 0:
                return False
            start = start + 2 # If the first reamainder is zero for a valid pair to exist second remainder has to be zero else False

        while start < end:
            # The pairs are opposite ends 
            # The range of remainders is 0,k-1 
            if (arr[start] + arr[end]) % k != 0:
                return False 
            start += 1
            end -= 1

        return True
