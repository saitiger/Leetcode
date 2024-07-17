class Solution:
    def reverseWords(self, s: str) -> str:
#  Using Stack
        ans = ''
        stack = []
        for x in s.split():
            stack.append(x)
        while stack: 
            ans+=stack.pop() + " "
        return ans.rstrip()

  # Without Stack
        words = s.split()
        reversed_string = ' '.join(words[::-1])
        return reversed_string
