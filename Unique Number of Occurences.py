class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt ={} # Dict to count the number of occurrences 
        res = set()
        for a in arr:
            if(a in cnt.keys()):
                cnt[a]+=1
            else:
                cnt[a]=1
        for x in cnt.values(): # Iterating the counter dictionary 
            res.add(x) # Adding unique count values
        return (len(res)==len(cnt)) # Checking if the set has the same number of elements as the counter if yes that means all count values are unique

# Solution 2 optimizing for the fact that input ranges between -1000 to 1000
# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         a = [0] * 2001 # Creating an empty array that represents the max possible range
#         for x in arr:
#             a[x + 1000] += 1 # Populating the array 
        
#         a.sort()
    
#         for i in range(1, 2001):
            # if a[i] != 0 and a[i] == a[i-1]: # If any time the value of two adjacent cells are equal return false
#                 return False
    
#         return True
