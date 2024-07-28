class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
# Bulbs which are toggled even number of times will remain off.
# Therefore we need to return only those bulbs who factors are odd pairs that their factors don't form a pair and only
# numbers that are perfect squares have this quality.
