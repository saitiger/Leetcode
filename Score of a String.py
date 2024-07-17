class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        arr = [x for x in s]
        for i in range(len(arr)-1):
            # print(score)
            # # score = abs(ord(arr[i+1]) - ord(arr[i]))
            score+=abs(ord(arr[i+1]) - ord(arr[i]))
        return score
