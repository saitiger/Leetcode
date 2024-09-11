class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i,j = 0,0
        running_sum,cnt = 0,0
        n = len(arr)

        while j<n:
            running_sum+=arr[j]
            if j-i+1==k:
                if running_sum/k>=threshold:
                    cnt+=1
                running_sum-=arr[i]
                i+=1
            j+=1
        return cnt
