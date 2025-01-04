class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i**2 for i in range(1, n + 1)}  
        count = 0
        for c in range(1, n + 1):
            c_squared = c**2
            for a in range(1, c):  
                b_squared = c_squared - a**2
                if b_squared in squares:
                    b = int(b_squared**0.5)  
                    if 1 <= b <= n:  
                        count += 1
        return count
