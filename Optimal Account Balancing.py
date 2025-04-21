class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Step 1: Calculate net balances for each person
        balance = defaultdict(int)
        for frm, to, amt in transactions:
            balance[frm] -= amt
            balance[to] += amt

        # Step 2: Filter out zero balances
        debt = [amount for amount in balance.values() if amount != 0]

        def dfs(start):
            # Skip settled balances
            while start < len(debt) and debt[start] == 0:
                start += 1
            if start == len(debt):
                return 0

            min_trans = float('inf')
            for i in range(start + 1, len(debt)):
                # Only try to settle with opposite signs
                if debt[start] * debt[i] < 0:
                    # Try settling start with i
                    debt[i] += debt[start]
                    min_trans = min(min_trans, 1 + dfs(start + 1))
                    debt[i] -= debt[start]  # Backtrack

                    # Prune: if debt[i] was same as a previous one, no need to try again
                    if debt[i] + debt[start] == 0:
                        break
            return min_trans

        return dfs(0)
