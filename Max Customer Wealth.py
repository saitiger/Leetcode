class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows = len(accounts)
        columns = len(accounts[0])
        max_wealth = 0

        for r in range(rows):
            wealth = 0
            for c in range(columns):
                wealth+=  accounts[r][c]
            max_wealth = max(max_wealth,wealth)
        return max_wealth
