from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)  
        max_heap = [(-ord(char), count) for char, count in freq.items()]
        heapify(max_heap)  

        result = []

        while max_heap:
            # Pop the lexicographically largest character
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)  # Convert back to the character
            
            allowed_repeats = min(count, repeatLimit) 
            # Repeat the number of characters either upto repeatLimit 
            # or the frequency whichever is minimum
        
            result.append(char * allowed_repeats)

            # If frequency is greater than the Limit then pop the next element
            if count > allowed_repeats:
                # If there are no other characters to break the sequence, stop
                if not max_heap:
                    break
                
                next_char_neg, next_count = heappop(max_heap)
                next_char = chr(-next_char_neg)
                
                # Append the breaker character once
                result.append(next_char)
                
                # Update the frequency of the next largest character 
                if next_count > 1:
                    heappush(max_heap, (next_char_neg, next_count - 1))
                
                # Push back the remaining occurrences of the first character
                heappush(max_heap, (char_neg, count - allowed_repeats))
        
        return "".join(result)
