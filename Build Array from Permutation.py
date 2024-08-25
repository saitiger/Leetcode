class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
      #O(n)
      #res = []  
      #for i in range(len(nums)):
        # res.append(nums[nums[i]])
    #   return res

    # Follow Up 
    # encoded = old_num + new_num * constant 
    # Constant can be 1001 i.e. any value greater than the constraint(1000)
    
    # old_num = encoded%constant
    # new_num = encoded//constant 

        for i in range(len(nums)):
            old_num = nums[i]
            new_num = nums[nums[i]]%1001
            nums[i] = old_num + new_num*1001 # Encoding
        for i in range(len(nums)):
            nums[i] = nums[i]//1001
        return nums
