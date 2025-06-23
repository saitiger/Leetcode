class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        ans = ""
        i = 0
        while i<len(s):
            if i+k<=len(s):
                res.append(s[i:i+k])
                i+=k
            elif i+k>len(s):
                while i<len(s):
                    ans+=s[i]
                    i+=1
                    k-=1
                ans+=fill*k
                res.append(ans)
        return res 
