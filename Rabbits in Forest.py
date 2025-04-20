import math
class Solution:
    def numRabbits(self, answers):
        mpp = defaultdict(int)
        res = 0
        for a in answers:
            mpp[a]+=1
        for other_count, freq in mpp.items():
            if other_count == 0:
                res += freq
            else:
                res += math.ceil(freq / (other_count + 1)) * (other_count + 1)
        return res
