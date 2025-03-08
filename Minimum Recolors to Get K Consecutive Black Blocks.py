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

# Dequeue
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dk = deque()
        cnt = 0

        for i in range(k):
            if blocks[i] == "W":
                cnt+= 1
            dk.append(blocks[i])

        res = cnt
        for i in range(k, len(blocks)):
            if dk.popleft() == "W":
                cnt-= 1
            if blocks[i] == "W":
                cnt+= 1
            dk.append(blocks[i])
            res = min(res, cnt)
        return res
