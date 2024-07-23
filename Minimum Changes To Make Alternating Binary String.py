class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0
        arr = [int(x) for x in s] 
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                cnt+=1
                arr[i]= abs(1 - arr[i-1])
        return cnt

# FAILS THE TEST CASE "10010100" 
THEREFORE WE NEED TO CHECK ALSO BY INVERTING THE FIRST ELEMENTING 

        start0 = 0
        start1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        return min(start0, start1)
