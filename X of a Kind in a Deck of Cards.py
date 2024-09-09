class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
    
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    
        all_freqs = list(count.values())
        overall_gcd = reduce(find_gcd, all_freqs)
    
        return overall_gcd > 1
