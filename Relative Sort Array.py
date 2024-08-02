class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_element = max(arr1)
        count = [0] * (max_element + 1)

        for element in arr1:
            count[element] += 1

        result = []
        for value in arr2:
            while count[value] > 0:
                result.append(value)
                count[value] -= 1

        for num in range(max_element + 1):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mpp = {}
        rem = []
        res = []
        for a in arr2:
            mpp[a] = 0
        for a in arr1:
            if a in mpp:
                mpp[a] += 1
            else:
                rem.append(a)
        a.sort()
        for a in arr2:
            for _ in range(mpp[a]):
                res.append(a)

        res.extend(rem)
        return res
