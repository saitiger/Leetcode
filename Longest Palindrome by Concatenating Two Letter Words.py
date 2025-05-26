from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mpp = defaultdict(int)
        result = 0

        for word in words:
            reversed_word = word[::-1]

            if mpp[reversed_word] > 0:
                result += 4  # Length 4 using both elements 
                mpp[reversed_word] -= 1 # Reduce count by one to indicate that the word has been used 
            else:
                mpp[word] += 1 # Add the element for later search 

        for word, count in mpp.items():
            if word[0] == word[1] and count > 0:
            # Super Word 
                result += 2
                break

        return result

  """
        The idea is to find how many pairs exist 
        Length --> num_pairs*2*2 

        num_pairs*2 --> Number of elements
        *2 --> Length of each element 

        Now we need to check for super-elements i.e. 
        elements that are palindrome by itself e.g. gg 

        Therefore 
        Length --> (num_pairs*4) + (if_super_element)*2

        *2 --> Length of each super element 

        if_super_element --> If atleast one super element exists
        # We can only use one super element if it occurs once 
        # if in a pair can be used twice 

        if number of pairs is zero :
            if number of super elements is zero:
                return 0 {No palindrome exists}

        """
