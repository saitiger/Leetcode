class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0,len(people)-1
        cnt = 0

        while l<=r:
            if l==r:
                cnt+=1
                break
            if people[l]+people[r]<=limit:
                cnt+=1
                l+=1
                r-=1
            else:
                cnt+=1
                r-=1
        return cnt
