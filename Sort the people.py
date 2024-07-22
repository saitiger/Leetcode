class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mpp = dict(zip(heights, names))
        sort_mpp = sorted(heights, reverse=True)
        return [mpp[height] for height in sort_mpp]
