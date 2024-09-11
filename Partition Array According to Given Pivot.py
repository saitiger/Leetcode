class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        
        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1
        
        for num in reversed(nums):
            if num > pivot:
                result[right] = num
                right -= 1
        
        while left <= right:
            result[left] = pivot
            left += 1
        
        return result
