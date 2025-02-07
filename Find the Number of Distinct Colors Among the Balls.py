# Attempt 1 using Set 
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        unique_nums = set() # Set to store the unique colors 
        arr = [-1]*(limit+1) # -1 means unvisited 

        res = []

        for i in range(len(queries)):
            if arr[queries[i][0]]!=-1: # If any value exists before 
                unique_nums.discard(arr[queries[i][0]]) 
# Remove the old value 'Remove' will give value error in case value does not exist using discard instead
            arr[queries[i][0]] = queries[i][1] # Add/Replace at the given location the current value
            unique_nums.add(arr[queries[i][0]]) # Add to the set 
            res.append(len(unique_nums)) # Adds the number of unique colors

        return res

  """
Fails Test Case 210, cannot process removed elements that is common. Need to use some other data structure {Hashmap}
  """

# Attempt 2
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        unique_nums = defaultdict(int) # Hashmap to store the counts of different colors 
        
        arr = [-1]*(limit+1) # -1 means unvisited 

        res = []

        for i in range(len(queries)):
            if arr[queries[i][0]]!=-1: # If any value exists before 
                unique_nums[arr[queries[i][0]]]-=1 # Reducing the count 
                if unique_nums[arr[queries[i][0]]]==0:
                    del unique_nums[arr[queries[i][0]]] # Remove the element from the hashmap if count becomes 0
            arr[queries[i][0]] = queries[i][1] # Add/Replace at the given location the current value
            unique_nums[arr[queries[i][0]]]+=1 # Increment the count
            res.append(len(unique_nums)) # Adds the number of unique colors
        return res

  # Memory Limit Exceeded

# Solution 
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = []  
        color_count = {}  # HashMap to store the counts of different colors
        ball_color = {}  # Maps each ball index to its current color
        for i in range(n):
            ball, color = queries[i]
            if ball in ball_color:
                prev_color = ball_color[ball]  # Get previous color
                color_count[prev_color] -= 1  # Reduce count of previous color
                # If no balls have this color, remove it from color_count
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            # Update ball_color with the new color
            ball_color[ball] = color  
            # Increment the count of the new color
            color_count[color] = color_count.get(color, 0) + 1
            # Store the number of unique colors
            result.append(len(color_count))
        return result
