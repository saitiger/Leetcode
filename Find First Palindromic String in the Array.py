class Solution:
    def is_palindrome(self,word):
        i = 0
        j = len(word) - 1
        while i<=j:
            if word[i]==word[j]:
                i+=1
                j-=1
            else:
                return False
        return True 
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""
