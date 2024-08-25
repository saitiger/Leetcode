class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if o=='++X' or o=='X++':
                x+=1
            else:
                x-=1
        return x 
