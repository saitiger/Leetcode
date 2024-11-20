class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1

        min_distance = float('inf')

        for i, word in enumerate(words):
            if word == target:
                direct_distance = abs(i - startIndex)
                circular_distance = n - direct_distance
                min_distance = min(min_distance, min(direct_distance, circular_distance))

        return min_distance
