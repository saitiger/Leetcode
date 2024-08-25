class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # Solution 1 
        # cnt = 0
        # for h in hours:
        #     if h>=target:
        #         cnt+=1
        # return cnt

        return sum([1 for h in hours if h>=target])
