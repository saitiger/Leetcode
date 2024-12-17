# Solution 1 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return (nums[0]-1)*(nums[1]-1)

# Solution 2 
        largest = 0
        second_largest = 0
        for n in nums:
            if n > largest:
                second_largest = largest
                largest = n
            else:
                second_largest = max(second_largest, n)
        return (largest - 1) * (second_largest - 1)
