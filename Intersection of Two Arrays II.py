class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Solution 1
        # cnt = {}
        # res = []
        # for n in nums1:
        #     if n in cnt.keys():
        #         cnt[n]+=1
        #     else:
        #         cnt[n]=1
        # for n in nums2:
        #     if n in cnt and cnt[n]>0:
        #         res.append(n)
        #         cnt[n]-=1
        # return res
        
        #Solution 2
        cnt = [0]*1001 # Mentioned in the contstraints that 
        res = []
        for n in nums1:
            cnt[n]+=1
        for n in nums2:
            if cnt[n]>0:
                res.append(n)
                cnt[n]-=1
        return res

        # Solution 3 
        cnt1,cnt2 = {},{}
        res = []
        for n in nums1:
            if n in cnt1.keys():
                cnt1[n]+=1
            else:
                cnt1[n]=1
        for n in nums2:
            if n in cnt2.keys():
                cnt2[n]+=1
            else:
                cnt2[n]=1
        for n in cnt1:
            if n in cnt2:
                min_cnt = min(cnt1[n],cnt2[n])
                res.extend([n]*min_cnt)
        return res
