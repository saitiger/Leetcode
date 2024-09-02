class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        n = len(nums)
        res = [0]*n

        for i in range(n):
            if nums[i]>0:
                res[pos]=nums[i]
                pos+=2
            else:
                res[neg]=nums[i]
                neg+=2
        return res
