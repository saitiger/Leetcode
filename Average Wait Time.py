class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0]
        wait = 0
        for c in customers:
            if start<c[0]:
                end = c[0] + c[1]
            else:
                end = start + c[1]
            wait+=end - c[0]
            start = end
        return wait/len(customers)

      # Solution 2 
        currentTime = 0
        totalwaitTime = 0
        
        for customer in customers:
            arrival, time = customer
            
            if currentTime < arrival:
                currentTime = arrival
                
            waitTime = currentTime + time - arrival
            totalwaitTime += waitTime
            
            currentTime += time
        
        return totalwaitTime / len(customers)
