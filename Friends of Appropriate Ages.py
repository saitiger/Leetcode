class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def validrequest(a, b):
            if b <= 0.5 * a + 7: return False
            if b > a: return False
            return True
        age_groups = collections.Counter(ages)
        ans = 0
        for a,v1 in age_groups.items():
            for b,v2 in age_groups.items():
                if validrequest(a, b):
                    ans += v1 * v2
                    if a == b: ans-= v1
        return ans
