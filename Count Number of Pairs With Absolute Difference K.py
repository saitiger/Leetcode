class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mpp = defaultdict(int)
        cnt = 0
        for num in nums:
            cnt+= mpp[num-k] + mpp[num+k]
            mpp[num] += 1
        return cnt

# O(N^2)
from collections import Counter
    mpp = Counter(nums)
    cnt = 0
    for num in mpp:
        # Check if `num + k` exists in the dictionary
        if num + k in mpp:
            count += mpp[num] * mpp[num + k] # No need to explicitly check `num - k` because it's symmetric i.e we need only one of the pairs i,j and j,i

    return count
