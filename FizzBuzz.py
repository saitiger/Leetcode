class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i%15==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

  # Solution 2 
        res = []
        i, fizz, buzz = 1, 0, 0

        while i <= n:
            fizz += 1
            buzz += 1

            if fizz == 3 and buzz == 5:
                res.append("FizzBuzz")
                fizz = buzz = 0
            elif fizz == 3:
                res.append("Fizz")
                fizz = 0
            elif buzz == 5:
                res.append("Buzz")
                buzz = 0
            else:
                res.append(str(i))

            i += 1

        return res
