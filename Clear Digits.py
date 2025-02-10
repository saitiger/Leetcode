class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i].isalpha():
                stk.append(s[i])
            else:
                if stk: 
                    stk.pop()
        return ''.join(stk)
