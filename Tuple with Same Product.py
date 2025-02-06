class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        mpp = defaultdict(int)
        cnt = 0 
        
        # Use hashmap to keep the count of each possible product 

        for i in range(len(nums)):
            for j in range(i+1,len(nums)): 
        # Product for each pair 
                mpp[nums[i]*nums[j]]+=1 

        for product_count in mpp.values(): 
        # For each product count the number of possible possible pairs
        # The formula is nC2 = n(n-1)/2 
        # Each pair has 8 possible tuples 
            num_pairs = ((product_count - 1)*(product_count))//2
            cnt+= 8*num_pairs
        return cnt

    """
        a*b = c*d
        2 groups  = 2 
        each group can be permuted in 2 ways = 2*2
        Total  = 2*2*2 = 8 
        a,b,c,d
        a,b,d,c
        b,a,c,d
        b,a,d,c
        c,d,a,b
        c,d,b,a
        d,c,a,b
        d,c,b,a
        """
