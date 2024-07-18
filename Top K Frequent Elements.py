class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #SOLUTION 1
        freq_dict = defaultdict(int)
        
        for n in nums:
            freq_dict[n] += 1
        
        sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        
        for i in range(k):
            result.append(sorted_freq[i][0])
        return result
       
        #SOLUTION 2 HEAP

        dic = {}            
        for i, num in enumerate(nums):
            dic[num] = dic.get(num,0) + 1

        heap=[]
        for item in dic.items():
            key, value = item
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for value, key in heap:
            res.append(key)
        return res   

        #SOLUTION 3 BUCKET SORT

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
