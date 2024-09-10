class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Finding Degree
        mpp = defaultdict(int)
        left_idx,right_idx = {},{} # Store the first and last index of the element
        for i,n in enumerate(nums):
            if n not in left_idx:
                left_idx[n]=i
            right_idx[n]=i
            mpp[n]+=1

        degree = max(mpp.values())

        # Finding Smallest Contigous Array 
        ans = len(nums) # Worst case scenario we need the whole array 
        for m in mpp:
            if mpp[m]==degree: # Only search for elements that have atleast the target degree
                ans = min(ans,right_idx[m]-left_idx[m]+1)
        return ans 
