class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2) and nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif i < len(nums1) and (j >= len(nums2) or nums1[i][0] < nums2[j][0]):
                res.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:  
                res.append([nums2[j][0], nums2[j][1]])
                j += 1
        return res
