class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq
        heap = [(-freq, word) for word, freq in Counter(words).items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
