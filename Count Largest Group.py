class Solution:
    def countLargestGroup(self, n: int) -> int:
        def helper(num):
            s = 0
            while num:
                s += num % 10
                num = num // 10
            return s

        mpp = defaultdict(int)
        max_group_size = 0 

        for i in range(1, n + 1):
            digit_sum = helper(i)
            mpp[digit_sum] += 1
            max_group_size = max(max_group_size, mpp[digit_sum])

        cnt = sum(1 for freq in mpp.values() if freq == max_group_size)
        return cnt
