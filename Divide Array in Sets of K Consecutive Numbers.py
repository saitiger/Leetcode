class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        n = len(nums)
        
        if n % k != 0:
            return False
        
        cnt = Counter(nums)
        
        while cnt:
            min_cnt = min(cnt)
            
            for i in range(k):
                curr = min_cnt + i
                if cnt[curr] == 0:
                    return False
                cnt[curr] -= 1
                if cnt[curr] == 0:
                    del cnt[curr]
        
        return True
