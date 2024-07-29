class Solution:
    MOD = 10**9 + 7

    def numFactoredBinaryTrees(self, arr):
        arr.sort()
        mpp = {}
        
        for i in range(len(arr)):
            count = 1
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in mpp:
                    count += mpp[arr[j]] * mpp[arr[i] // arr[j]]
            
            mpp[arr[i]] = count
        
        return sum(mpp.values()) % self.MOD
