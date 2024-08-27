class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mpp = defaultdict(int)

        for n in nums:
            mpp[n]+=1
          
        s = 0
        for k,v in mpp.items():
            if v==1:
                s+=k
        return s
