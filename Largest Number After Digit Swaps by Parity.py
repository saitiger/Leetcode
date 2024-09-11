# Solution 1 
class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(n) for n in str(num)]
        odd,even = [],[]

        for d in digits:
            if d%2==0:
                even.append(d)
            else:
                odd.append(d)
        odd.sort()
        even.sort()
        i,j = len(odd)-1,len(even)-1
        res = ''
        for d in digits:
            if d%2==0:
                res+=str(even[j])
                j-=1
            else:
                res+=str(odd[i])
                i-=1
        return int(res)

# Solution 2 Using Heap 
class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        res=[]
        for i in str(num):
            if int(i) % 2 == 0:
                even.append(-int(i))
            else:
                odd.append(-int(i))
        heapq.heapify(even)
        heapq.heapify(odd)
        for value in str(num):
            val=int(value)
            if val%2==0:
                res.append(str(-heapq.heappop(even)))
            else:
                res.append(str(-heapq.heappop(odd)))
        return int("".join(res))
