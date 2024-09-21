class Solution:
    def __init__(self, nums: List[int]):
        # Create a dictionary to store the indices of each target number
        self.indices = {}
        # Iterate through the array nums and add the index i to the list of indices associated with nums[i]
        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = [i]
            else:
                self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # Get the list of indices associated with the target number from the dictionary
        indices = self.indices[target]
        # Use the random module to generate a random index from the list of indices
        return random.choice(indices)

# Implementation of my code gave TLE on test case 14 
# Credits : https://leetcode.com/problems/random-pick-index/solutions/3258481/398-solution-with-step-by-step-explanation/?envType=problem-list-v2&envId=reservoir-sampling
