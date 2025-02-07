class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mpp = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            s = 0 
            while i:
                s+=i%10
                i=i//10
            mpp[s]+=1
        return max(mpp.values())
