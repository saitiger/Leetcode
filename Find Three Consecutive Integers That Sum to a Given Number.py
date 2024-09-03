class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = num//3
        if ((mid-1)+(mid)+(mid+1))==num:
            return [mid-1,mid,mid+1]
        else:
            return []
