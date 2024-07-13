class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt=0
        seen = set(nums)
        for n in seen:
            if n-1 not in seen:
                cnt = 1
                while n+1 in seen:
                    cnt+=1
                max_cnt=max(max_cnt,cnt)
        return max_cnt
