class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Solution 1 
        res=[]
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        
        return res
# Solution 2 
      for i in range(len(words)):
            for letter in words[i]:
                if letter==x:
                    res.append(i)
                    break
        return res
