def get_nsl(arr: List[int]) -> List[int]:
    n = len(arr)
    result = [-1] * n
    st = []
    
    for i in range(n):
        while st and arr[st[-1]] > arr[i]:
            st.pop()
        result[i] = st[-1] if st else -1
        st.append(i)
    
    return result

def get_nsr(arr: List[int]) -> List[int]:
    n = len(arr)
    result = [n] * n
    st = deque()
    
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        result[i] = st[-1] if st else n
        st.append(i)
    
    return result

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 1000000007
        n = len(arr)
        
        nsl = get_nsl(arr)
        nsr = get_nsr(arr)
        
        total_sum = 0
        
        for i in range(n):
            d1 = i - nsl[i]
            d2 = nsr[i] - i
            total_ways_for_i_min = d1 * d2
            sum_i_in_total_ways = arr[i] * total_ways_for_i_min
            total_sum = (total_sum + sum_i_in_total_ways) % M
        
        return total_sum
