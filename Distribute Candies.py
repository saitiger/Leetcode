class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can_have = len(candyType)//2
        num = len(set(candyType))

        if can_have>=num:
            return num
        else:
            return can_have
     
