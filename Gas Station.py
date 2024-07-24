class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_cost>total_gas:
            return -1
        
        res,total = 0,0

        for i in range(len(gas)):
            total = total + gas[i] - cost[i]

            if(total<0):
                total = 0 
                res = i+1
        return res
