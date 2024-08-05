class Solution:
    def isNStraightHand(self, hand, groupSize):
        from collections import Counter
        n = len(hand)
        
        if n % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        
        while card_count:
            min_card = min(card_count)
            
            for i in range(groupSize):
                current_card = min_card + i
                if card_count[current_card] == 0:
                    return False
                card_count[current_card] -= 1
                if card_count[current_card] == 0:
                    del card_count[current_card]
        
        return True
# Using Min Heap

        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            curr = min_heap[0]
            for i in range(curr, curr + groupSize):
                if i not in card_count:
                    return False
                card_count[i] -= 1
                if card_count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True

# Solution 2 Leetcode Editorial (Optimal Approach)

  for card in hand:
            start_card = card
            while card_count[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1

        return True
