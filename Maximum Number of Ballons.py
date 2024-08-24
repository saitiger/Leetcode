class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        balloon = Counter("balloon")
        res = float("inf")    
        for c in balloon:
            res = min(res,cnt[c]//balloon[c])
        return res
