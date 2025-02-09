class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Count of bad pairs = Count of total pairs - Count of good pairs
        Good pair :
        j-i = nums[j]-nums[i]
        nums[j]-j = nums[i] - i
        Find numbers with val - idx that are same 
        These are good pairs
        """
        mpp = defaultdict(int) # Hashmap for count of vals with same difference between num and index
        n = len(nums)
        total_pairs = (n*(n-1))/2 # nC2

        for i in range(n):
            mpp[nums[i]-i]+=1

        good_pairs = 0 # Count of bad pairs 
        for val in mpp.values():
            bad_pairs+=(val*(val-1))/2 

        return int(total_pairs-good_pairs)
