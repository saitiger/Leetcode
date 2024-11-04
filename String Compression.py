# Using extra memory 
    i, count = 0, 0
    res = []
    while i < len(chars):
        current_char = chars[i]
        count = 0
        while i < len(chars) and current_char == chars[i]:
            i += 1
            count += 1
        res.append(current_char)
        if count > 1:
            count_str = str(count)  
            for digit in count_str:
                res.append(digit)    
    return res, len(res)

# Inplace 
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  
        i = 0      
        
        while i < len(chars):
            current_char = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == current_char:
                i += 1
                count += 1
            
            chars[write] = current_char
            write += 1
            
            if count > 1:
                for digit in str(count): 
                    chars[write] = digit
                    write += 1
        
        return write
