class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mpp = defaultdict(int)
        res = []
        for s in s1.split():
            mpp[s]+=1
        for s in s2.split():
            mpp[s]+=1
        for k,v in mpp.items():
            if v==1:
                res.append(k)
        return res
