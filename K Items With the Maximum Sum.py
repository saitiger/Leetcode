class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        if k<=(numOnes+numZeros):
            return numOnes*1 if k>=numOnes else k*1 
        else:
            return numOnes + (k-(numOnes+numZeros))*-1
