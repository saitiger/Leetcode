class Solution:
    def minimumPushes(self, word):
        if len(word) <= 8:
            return len(word)

        count = 0
        mp = [0] * 10  
        assign = 2
        for ch in word:
            if assign > 9:
                assign = 2

            mp[assign] += 1
            count += mp[assign]
            assign += 1

        return count
