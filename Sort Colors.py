class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n]+=1
            # if n in cnt:
            #     cnt[n] = 1
            # else:
            #     cnt[n]+=1
        
        for i in range(cnt[0]):
            nums[i] = 0
        
        for i in range(cnt[0],cnt[0]+cnt[1]):
            nums[i] = 1
        
        for i in range(cnt[0]+cnt[1],len(nums)):
            nums[i] = 2
            
        return nums

        # One Pass Solution 
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums
