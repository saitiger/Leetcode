class Solution:
    def divideArray(self, nums: List[int]) -> bool:

  # Use Hashmap to keep a count of elements in the array 
  # If any element is present is not present twice (or a multiple of two)
  # i.e. greater than zero but not equal to a multiple of two return False

        mpp = defaultdict(int)

        for n in nums:
            mpp[n]+=1
    
        for v in mpp.values():
            if v%2!=0:
                return False
        return True

# Solution 2 
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        max_num = max(nums)
        needs_pair = [False] * (max_num + 1)
        for num in nums:
            needs_pair[num] = not needs_pair[num]
        return not any(needs_pair[num] for num in nums)
