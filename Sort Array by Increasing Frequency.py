class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mpp = {}
        for n in nums:
            mpp[n] = mpp.get(n,0)+1
        return sorted(nums,key = lambda x: (mpp[x],-x))
