class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def no_of_days(weight,capacity):
            total = 0
            num_days = 1
            for n in weights:
                if(total<=capacity):
                    total+=n
                else:
                    num_days+= 1
                    total = n
            return num_days

        l = max(weights)
        r = sum(weights)
        while l<=r:
            m = (l+r)//2
            numberOfDays = no_of_days(weights, m)
            if(numberOfDays<=days):
                r = m - 1
            else:
                l = m + 1
        return l
