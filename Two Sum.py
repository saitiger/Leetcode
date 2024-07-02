class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i,v in enumerate(nums):
            diff = target - v 
            if(diff in hashMap):
                return(i,hashMap.get(diff))
            else :
                hashMap[v] = i
