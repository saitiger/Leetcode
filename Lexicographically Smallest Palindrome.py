class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        temp = list(s)
        l,r = 0,len(temp)-1
        while l<r:
            if(temp[l]!=temp[r]):
                if (temp[l]<=temp[r]):
                    temp[r]=temp[l]
                else:
                    temp[l]=temp[r]
            l+=1
            r-=1
        ans = ''
        for t in temp:
            ans+=t
        return ans
