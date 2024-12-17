# Why Set does not work
"""
The purpose of the set is to track the elements if an element has been previously seen or if the element previously seen reached count/frequency zero.

"""
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        max_heap = []  # Max heap to keep track of frequencies
        count_map = {}  # Map to keep track of the total frequency of each ID
        res = []

        for i in range(len(nums)):
            # Update frequency in the count_map
            if nums[i] in count_map:
                count_map[nums[i]] += freq[i]
            else:
                count_map[nums[i]] = freq[i]
            
            # If the frequency becomes zero or less, remove it
            if count_map[nums[i]] <= 0:
                del count_map[nums[i]]
            else:
                heapq.heappush(max_heap, (-count_map[nums[i]], nums[i]))
            
            while max_heap and -max_heap[0][0] != count_map.get(max_heap[0][1], 0):
              # Checking the top element in a heap has a frequency consistent with the most up-to-date value in the count_map
                heapq.heappop(max_heap) # Remove the old counts 

            if max_heap:
                res.append(-max_heap[0][0])
            else:
                res.append(0)
        return res
