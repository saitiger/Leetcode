from math import gcd, lcm
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for ele in nums:
            top = ele
            while stack and gcd(top, stack[-1]) > 1:
                top = lcm(stack[-1], top)
                stack.pop()
            stack.append(top)
        return stack
