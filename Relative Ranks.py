class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
# Using Heap 
        max_heap = [(-val,idx) for idx,val in enumerate(score)]
        heapq.heapify(max_heap)
        cnt = 1

        while max_heap:
            _,idx = heapq.heappop(max_heap)
            if cnt==1:
                score[idx] = "Gold Medal"
            elif cnt==2:
                score[idx] = "Silver Medal"
            elif cnt==3:
                score[idx] = "Bronze Medal"
            else:
                score[idx] = str(cnt)
            cnt+=1
        return score 

# Using Pigeonhole principle and Array as a Map

class Solution:
    def find_max(self, score):
        max_score = 0
        for s in score:
            if s > max_score :
                max_score = s
        return max_score

    def findRelativeRanks(self, score):
        N = len(score)

        # Add the original index of each score to the array
        # Where the score is the key
        M = self.find_max(score)
        score_to_index = [0] * (M + 1)
        for i in range(N):
            score_to_index[score[i]] = i + 1

        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        # Assign ranks to athletes
        rank = [None] * N
        place = 1
        for i in range(M, -1, -1):
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place < 4:
                    rank[original_index] = MEDALS[place - 1]
                else:
                    rank[original_index] = str(place)
                place += 1
        return rank
