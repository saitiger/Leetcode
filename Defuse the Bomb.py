class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
    
        result = [0] * n
    
        if k > 0:
            current_sum = sum(code[i] for i in range(1, k+1))
            for i in range(n):
                result[i] = current_sum
                current_sum = current_sum - code[(i + 1) % n] + code[(i + k + 1) % n]
        else:
            k = -k
            current_sum = sum(code[i] for i in range(n - k, n))
            for i in range(n):
                result[i] = current_sum
                current_sum = current_sum - code[(i - k) % n] + code[i]
    
        return result
