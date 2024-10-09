class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_parenthesis,close_parenthesis= 0,0
        for char in s:
            if char == '(':
                open_parenthesis += 1
            elif char == ')' and open_parenthesis > 0:
                open_parenthesis -= 1
            else:
                close_parenthesis += 1
        return open_parenthesis + close_parenthesis
