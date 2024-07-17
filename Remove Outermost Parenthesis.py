class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans, op = [], 0
        for c in S:
            if c == '(' and op>0: ans.append(c)
            if c == ')' and op>1: ans.append(c)
            op+= 1 if c == '(' else -1
        return "".join(ans)
