class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if total < min(cost1, cost2):
            return 1  # Only one way to buy 0 Pens and 0 Pencils 
        num_ways = 0
        i = 0
        while total >= 0:
            remaining = total - cost1 * i
            if remaining < 0:
                break
            num_pencils = remaining // cost2 + 1
            num_ways += num_pencils
            i += 1
        return num_ways
