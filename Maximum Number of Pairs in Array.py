class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mpp = defaultdict(int)
        pairs,remaining = 0,0
        for n in nums:
            mpp[n]+=1

        for v in mpp.values():
            pairs+=v//2
            remaining+= v%2
        return [pairs,remaining]
