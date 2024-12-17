import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        cnt1, cnt2 = 0, 0
        el1, el2 = None, None

        min_val = math.floor(len(nums) / 3)  # Threshold condition

        for num in nums:
            if num == el1: 
                cnt1 += 1
            elif num == el2: 
                cnt2 += 1
            elif cnt1 == 0: 
                el1 = num
                cnt1 = 1
            elif cnt2 == 0: 
                el2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Second pass: Verify candidates
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
        
        if cnt1 > min_val:
            res.append(el1)
        if cnt2 > min_val:
            res.append(el2)

        res.sort()
        return res
