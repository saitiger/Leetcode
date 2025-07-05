class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Solution 1
        # mpp = defaultdict(int)
        # for a in arr:
            # mpp[a]+=1
        
        # res = -1 
        # for k,v in mpp.items():
        #     if k==v:
        #         res = max(res,k)

        # return res

        chk = [0]*501

        # Solution 2
        for a in arr:
            chk[a]+=1
        
        res = -1

        for i in range(len(chk)-1,0,-1):
            if i==chk[i]:
                res = chk[i]
                break
        return res
