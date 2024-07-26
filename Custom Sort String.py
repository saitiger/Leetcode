class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Solution 1 Using sorted 
        # sorted_s = sorted(s, key=lambda c: order.find(c))
        # return ''.join(sorted_s)

        # Solution 2 Using Hashmap
      
        cnt = defaultdict(int)
        res = []
        
        for c in s:
            cnt[c]+=1

        for chrc in order:
            res.append(chrc*cnt[chrc])
            del cnt[chrc]

        for chrc in s:
            if cnt[chrc]>0:
                res.append(chrc*cnt[chrc])
                del cnt[chrc]

        return "".join(res)
