class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                cnt += 1
        return cnt

 # Without Converting to String  
    def evendigits(self, num: int) -> bool:
        cnt = 0
        while num:
            cnt += 1
            num //= 10
        return cnt & 1 == 0

    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if self.evendigits(num):
                cnt += 1
        return cnt
