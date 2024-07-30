class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
# Method 2 
        from collections import Counter
        n = len(s)
        count = Counter(s)
        maxFreq = max(count.values())
        maxFreqCh = max(count, key=count.get)
        if maxFreq > (n + 1) // 2:
            return ""
        result = [''] * n
        index = 0
        while count[maxFreqCh] > 0:
            result[index] = maxFreqCh
            index += 2
            count[maxFreqCh] -= 1
        for ch, freq in count.items():
            while freq > 0:
                if index >= n:
                    index = 1
                result[index] = ch
                index += 2
                freq -= 1
        return ''.join(result)
