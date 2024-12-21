class Solution:
    def kthCharacter(self, k: int) -> str:
        temp = 'a'
        while len(temp) < k:
            curr = ''
            for char in temp:
                if char == 'z':
                    curr += 'a'
                else:
                    curr += chr(ord(char) + 1)
            temp += curr
        return temp[k - 1]
