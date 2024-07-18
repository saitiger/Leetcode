class Solution:
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        flag = False
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or num <= nums[i + 1]:
                continue
            if flag:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            flag = True
        return True
