class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        seen = set(nums) 
        for num in seen:
            if (num + diff) in seen and (num + 2 * diff) in seen:
                cnt += 1
        return cnt
