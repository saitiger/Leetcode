class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return 1
        if word.isupper():
            return 1
        if (word[0].isupper() and word[1:].islower()):
            return 1
        else:
            return 0
