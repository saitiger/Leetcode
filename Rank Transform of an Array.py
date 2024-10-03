# Solution 1 
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for i in range(1,len(sorted_arr)):
            if sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr

# Solution 2 : Using Set 
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            num_to_rank[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr
