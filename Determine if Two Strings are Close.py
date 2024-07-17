class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1 = set(word1)
        s2 = set(word2)
        if s1!=s2: return False
        cnt1,cnt2 = defaultdict(int),defaultdict(int)
        for s in word1:
            cnt1[s]+=1
        for s in word2:
            cnt2[s]+=1     
        freq_1 = list(cnt1.values())
        freq_2 = list(cnt2.values())
        freq_1.sort()
        freq_2.sort()
        if freq_1!=freq_2: return False
        return True

  # Solution 2 Using Bitmask Array
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        for ch in word2:
            freq2[ord(c) - ord('a')] += 1
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
        freq1.sort()
        freq2.sort()
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True
