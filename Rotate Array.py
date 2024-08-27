class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Solution 1 O(N)
        n = len(nums)
        if n == 0:
            return
    
        k = k % n  
        if k == 0:
            return  
        
        temp = []

        for i in range(n-k,n):
            temp.append(nums[i])
    
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
    
        for i in range(k):
            nums[i] = temp[i]

      # Solution 2 O(1)
      class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
