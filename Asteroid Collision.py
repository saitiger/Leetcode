class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for a in asteroids:
            while stk and a < 0 and stk[-1] > 0:
                if stk[-1] < -a:  
                    stk.pop()
                    continue
                elif stk[-1] == -a:  
                    stk.pop()
                break
            else:
                stk.append(a)
        return stk
