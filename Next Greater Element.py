class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = dict().fromkeys(nums1)
        stack = []
        for i in reversed(nums2):
            while stack and stack[-1] < i:
                stack.pop()
            if i in nge:
                nge[i] = stack[-1] if stack else -1
            stack.append(i)
        return nge.values()
