class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # BRUTE FORCE 
        # res1 = []
        # res2 = []
        # for num1 in nums1:
        #     if num1 not in nums2 and num1 not in res1:
        #         res1.append(num1)
    
        # for num2 in nums2:
        #     if num2 not in nums1 and num2 not in res2:
        #         res2.append(num2)

        # return [res1,res2]

        # Using Sets to reduce complexity 
        
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        lst1 = [num for num in nums1_set if num not in nums2_set]
        lst2 = [num for num in nums2_set if num not in nums1_set]

        return [lst1, lst2]
    
