class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.mpp = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.mpp[self.nums2[index]] -= 1  # Remove one instance of the old value from the dictionary 
        self.nums2[index] += val # Increment at index by value val 
        self.mpp[self.nums2[index]] += 1  # Increment the new value count in the dictionary 

    def count(self, tot: int) -> int:
        cnt = 0
        for n1 in self.nums1:  
            cnt+= self.mpp[tot - n1] # Check in the dictionary if the value total-current element exists if yes increment by its frequency
        return cnt
