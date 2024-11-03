class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        if words[0][0]!=words[-1][-1]:
            return False
        if len(words)==1:
            if words[0][0]==words[0][-1]:
                return True
        i = 0
        while i+1<len(words):
            if words[i][-1]!=words[i+1][0]:
                return False
            i+=1
        return True

# Solution 2 
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[len(sentence) - 1]
