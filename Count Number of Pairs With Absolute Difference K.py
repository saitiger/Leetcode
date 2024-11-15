class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mpp = defaultdict(int)
        cnt = 0
        for num in nums:
            cnt+= mpp[num-k] + mpp[num+k]
            mpp[num] += 1
        return cnt
