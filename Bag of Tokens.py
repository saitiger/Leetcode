class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        curr_score = 0
        max_score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                curr_score += 1
                max_score = max(max_score, curr_score)
                power -= tokens[l]
                l += 1
            elif curr_score >= 1:
                curr_score -= 1
                power += tokens[r]
                r -= 1
            else:
                return max_score
        return max_score
