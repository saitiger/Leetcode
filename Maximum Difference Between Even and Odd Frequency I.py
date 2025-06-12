class Solution:
    def maxDifference(self, s: str) -> int:
        # Find the frequency of all characters 

        mpp = defaultdict(int)

        for char in s:
            mpp[char]+=1
        
        # Find the values of a1,a2
        a1 = 0 
        a2_ls = []
        for val in mpp.values():
            if val%2!=0:
                a1 = max(a1,val)
            else:
                a2_ls.append(val) 
        a2 = min(a2_ls)

        return a1-a2

  # Pythonic Solution (Credits : Editorial)

class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven
