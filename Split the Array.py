class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = [0] * 100 # Due to the size constraints and value range we can use array instead of hashmap
        for n in nums:
            freq[n-1]+= 1
            if freq[n-1]>2: # If any value has more than 2 frequency we then array can't be split
                return False
        return True
