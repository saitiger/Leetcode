class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda n: -n[0])
        ans, max_beauty = [0] * len(queries), 0
        for i in sorted(range(len(queries)), key = lambda i: queries[i]):
            while items and items[-1][0] <= queries[i]:
                max_beauty = max(max_beauty, items.pop()[1])
            ans[i] = max_beauty
        return ans
