class Solution:
    def toGoatLatin(self, S: str) -> str:
        temp = []
        ans = " "  
        i = 1
        for word in S.split(" "):
            if word[0].lower() in 'aeiou':
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word = word + "a"*i
            i = i + 1
            temp.append(word)
        return ans.join(temp)
