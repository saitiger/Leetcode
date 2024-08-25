class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # res = []
        # for i in range(n):
        #     res.append(nums[i])
        #     res.append(nums[i+n])
        # return res

        # Solution 2 
        # for i, j in zip(nums[:n],nums[n:]):
            # res += [i,j]
        # return res

        # Solution 3 O(1) Space 
        
        # encoded = x + y* constant
        # x = encoded%constant
        # y = encoded//constant

        for i in range(n):
            x = nums[i]
            y = nums[i+n]%1001
            nums[i] = x + y*1001 # Encoding
        j = 2*n-1
        for i in range(n-1,-1,-1):
            nums[j] = nums[i]//1001
            nums[j-1] = nums[i]%1001
            j-=2
        return nums

        # Bit Manipulation 
    
        # for i in range(n):
        #     nums[i] = nums[i] << 10
        #     nums[i] = nums[i] | nums[i + n]  # store x, y

        # j = 2 * n - 1
        # for i in range(n - 1, -1, -1):
        #     y = nums[i] & (2**10 - 1)
        #     x = nums[i] >> 10
        #     nums[j] = y
        #     nums[j - 1] = x
        #     j -= 2

        # return nums
