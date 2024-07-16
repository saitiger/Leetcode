class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeroCount1, zeroCount2, sum1, sum2 = 0, 0, 0, 0

        for num in nums1:
            zeroCount1 += 1 if num == 0 else 0
            sum1 += num
        
        for num in nums2:
            zeroCount2 += 1 if num == 0 else 0
            sum2 += num
        sum1 += zeroCount1
        sum2 += zeroCount2

        if (zeroCount1 == 0 and sum2 > sum1) or (zeroCount2 == 0 and sum1 > sum2):
            return -1
        return max(sum1, sum2)
