class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        cnt, l, r = 0, 0 ,len(nums) - 1

        while l < r:
            summ = nums[l] + nums[r]
            if summ > k:
                r -= 1
            elif summ < k:
                l += 1
            else:
                cnt += 1
                l += 1
                r -= 1
        return cnt

# Hashmap

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mpp = defaultdict(int) 
        cnt = 0
        for n in nums:
            if mpp[n]: 
                cnt += 1
                mpp[n] -= 1
            else: 
                mpp[k - n] += 1        
        return cnt
