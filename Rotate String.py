class Solution(object):
    def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False
# SOLUTION 2
      # Using the fact that all rotations of a string s are contrained in the string s+s
        if len(s) != len(goal):
            return False
        if len(s)==0: return True
        return goal in s + s
