class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        mid = int(len(s)/2)
        a = s[:mid]
        b = s[mid:]

        cnt_a,cnt_b = 0,0

        for i in range(len(a)):
            if a[i] in vowels:
                cnt_a+=1
            if b[i] in vowels:
                cnt_b+=1
        
        return cnt_a==cnt_b
