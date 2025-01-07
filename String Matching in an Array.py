class Solution:
    def stringMatching(self, words):
        ans = []
        for curr_idx in range(len(words)):
            for next_idx in range(len(words)):
                if curr_idx == next_idx:
                    continue
                if words[curr_idx] in words[next_idx]:
                    ans.append(words[curr_idx])
                    break 
        return ans
