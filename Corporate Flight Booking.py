class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0] * n # Initialize result array 
        
        for first, last, seats in bookings:
            res[first - 1] += seats # Add count at starting index-1 (1 based index)
            if last < n:
                res[last] -= seats # Reduce the count at ending index+1

        # Prefix Sum 
        for i in range(1, n):
            res[i] += res[i - 1] 
        
        return res
