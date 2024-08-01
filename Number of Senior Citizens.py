class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Method 1 
        cnt = 0 
        for d in details:
            # if int(d[11:13]) > 60:
            if d[11:13] > 60:
                cnt+=1
        return cnt
        # return sum((detail[11] > '6'  or detail[11] == '6' and detail[12] != '0') for detail in details)

        # Method 2 Scalable Source : Leetcode Editorial
        cnt = 0  
        for d in details:
            tens = ord(d[11]) - ord("0")
            ones = ord(d[12]) - ord("0")
            if tens * 10 + ones > 60:
                cnt+= 1
        return cnt
