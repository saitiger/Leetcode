class Solution(object):
    def intersection(self, nums1, nums2):
        n1 = set(nums1)
        n2 = set(nums2)
        ans = set()

        for n in n1:
            if(n in n2 and n not in ans):
                ans.add(n)
            else:
                pass

        for n in n2:
            if(n in n1 and n not in ans):
                ans.add(n)
            else:
                pass
        return ans

# Solution 2 : Without using Set

  #     seen = {}
    #     result = []

    #     for x in nums1:
    #       seen[x] = 1
          
    #     for x in nums2:
    #       if x in seen and seen[x] == 1:
    #         result.append(x)
    #         seen[x] = 0

    #     return result
