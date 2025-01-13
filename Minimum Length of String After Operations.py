class Solution:
    def minimumLength(self, s: str) -> int:
        
        mpp = defaultdict(int)
        ans = 0 

        for c in s:
            mpp[c]+=1

        for k,v in mpp.items():
            if v%2==0:
                ans+=2
            else:
                ans+=1
        return ans
