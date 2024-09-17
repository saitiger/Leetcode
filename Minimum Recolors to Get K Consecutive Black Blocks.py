class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans,missing = k,0 
        i,j = 0,0
        while j<len(blocks):
            if blocks[j]=='W':
                missing+=1
            if j-i+1==k:
                ans = min(ans,missing)
                if blocks[i]=='W':
                    missing-=1
                i+=1
            j+=1
        return ans 
