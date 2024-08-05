class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mpp = defaultdict(int)
        for a in arr:
            mpp[a]+=1
        
        cnt = 0
        for m in mpp:
            if mpp[m]==1:
                cnt+=1
                if cnt==k:
                    return m

        return ""
