# class Solution:
    # def canBeValid(self, s: str, locked: str) -> bool:
        # opencnt,closecnt = 0,0
        # i = 0 
        # while i<len(s):
        #     if s[i]==')':
        #         closecnt+=1
        #     if s[i]=='(':
        #         opencnt+=1
        #     if opencnt<closecnt:
        #         if locked[i]==1:
        #             return False
        #         else:
        #             opencnt+=1
        #             closecnt-=1
        #     # print("OPEN : ",opencnt)
        #     # print("CLOSE : ",closecnt)
        #     i+=1
        # return opencnt==closecnt

# Solution 1 
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        # First pass: Ensure we have enough potential '(' going left-to-right
        open_count, close_count = 0, 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':  
                open_count += 1
            else:  
                close_count += 1

            if close_count > open_count:
                return False

        # Second pass: Ensure we have enough potential ')' going right-to-left
        open_count, close_count = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0': 
                close_count += 1
            else:  
                open_count += 1

            if open_count > close_count:
                return False

        # If both passes are valid, the string can be balanced
        return True

# Solution 2 using Stack 
class Solution:
    def canBeValid(self, s, locked):
        length = len(s)

        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True
