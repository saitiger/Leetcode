class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False 
            
        strictlyInc = False
        strictlyDec = False
        
        for i in range(len(arr)-1):
            if (arr[i+1] < arr[i]):
                if (strictlyInc == False):
                    return False
                strictlyDec = True
            elif (arr[i+1] > arr[i]):
                if (strictlyDec == True):
                    return False
                strictlyInc = True
            else:
                return False
        
        if strictlyInc and strictlyDec:
            return True
        else:
            return False
