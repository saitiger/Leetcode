class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Solution 1 
        n = len(A)
        set_A, set_B = set(), set()
        prefix_common = []
        for i in range(n):
            set_A.add(A[i])
            set_B.add(B[i])
            # Calculating the intersection size
            common_count = len(set_A & set_B)
            prefix_common.append(common_count)
        return prefix_common

# Solution 2 

# Using the hashmap track the frequency of currently seen element for both the Arrays. As soon as the array reaches the frequency of 2 increase the count.
# The idea behind this is that no number is repeated in either arrays and the arrays are a permutation of each other 
        mpp = defaultdict(int)
        cnt = 0
        res = []
        for i in range(len(A)):
            mpp[A[i]]+=1
            if mpp[A[i]]==2:
                cnt+=1
            mpp[B[i]]+=1
            if mpp[B[i]]==2:
                cnt+=1
            res.append(cnt)
        return res 
