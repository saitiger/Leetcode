class Solution:
    def isValid(self, nums: List[int], mid_max: int, n: int) -> bool:
        arr = list(map(lambda x: x, nums))
        for i in range(n-1):
            if arr[i] > mid_max:
                return False
            buffer = mid_max - arr[i]
            arr[i+1] -= buffer
        return arr[n-1] <= mid_max
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxL = 0
        maxR = max(nums)
        result = 0
        while maxL <= maxR:
            mid_max = maxL + (maxR - maxL) // 2
            if self.isValid(nums, mid_max, n):
                result = mid_max
                maxR = mid_max - 1
            else:
                maxL = mid_max + 1
        return result
