class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)

# Without built-in function 
        count = 0
        for word in words:
            if self.is_prefix(word, pref):
                count += 1
        return count

    def is_prefix(self, word: str, pref: str) -> bool:
        if len(pref) > len(word):
            return False
        for i in range(len(pref)):
            if word[i] != pref[i]:
                return False
        return True
