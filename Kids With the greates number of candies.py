class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = candies[0]
        res = []
        for n in candies:
            max_candies = max(max_candies,n)
        for n in candies :
            if(n+extraCandies>=max_candies):
                res.append(True)
            else:
                res.append(False)
        return res
