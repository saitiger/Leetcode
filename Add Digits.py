class Solution:
    def addDigits(self, num: int) -> int:
        # Brute Force
        if(len(str(num)))==1:
            return num
        while (len(str(num)))>1:
            s = 0
            for n in str(num):
                s+=int(n)
            num = str(s)
        return int(num)
# Solution 2 O(1)
        if num == 0:
            return 0
        if num%9 == 0:
            return 9
        return num%9
