from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict = defaultdict(int)
        for ch in s:
            freq_dict[ch] += 1      
        sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)  
        result = ""
        for ch, freq in sorted_freq:
            result += ch * freq
        return result
# BUCKET SORT
        cnt = Counter(s)
        buckets = defaultdict(list)
        for char, c in cnt.items():
            buckets[c].append(char)
        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        return "".join(res)
