class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk, res = [], [-1] * n 
        for i in range(len(nums) * 2): 
            while stk and (nums[stk[-1]] < nums[i%n]): 
                res[stk.pop()] = nums[i%n] 
            stk.append(i%n) 
        return res 
