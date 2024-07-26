class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_1,num_2 = float("inf"),float("inf")

        for n in nums:
            if n<=num_1:
                num_1 = n
            elif n<=num_2:
                num_2 = n
            else:
                return True
        return False
