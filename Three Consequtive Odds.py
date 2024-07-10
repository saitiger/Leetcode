class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
       # Solution 1 
        i = 0 
        flag = 0
        for a in range(len(arr)-2): # Finding the first odd number to reduce the number of comparisons in case we don't have any 
            if(arr[a]%2!=0):
                i = a
                break
        for j in range(i,len(arr)-2):
            if(arr[j]%2!=0 and arr[j+1]%2!=0 and arr[j+2]%2!=0):
                flag = 1
                break 
        return flag==1      
# Solution 2 
        cnt = 0
        for a in arr:
            if a%2!=0:
                cnt+=1
            else:
                cnt=0
            if(cnt==3):
                return True
        return False
