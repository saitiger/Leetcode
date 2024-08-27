class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        cnt = Counter(arr)
        res, i, n = 0, 0, len(arr)
        while i < n:
            l, r = i, n - 1
            while l < r:
                if arr[i] + arr[l] + arr[r] < target:
                    l += cnt[arr[l]]
                elif arr[i] + arr[l] + arr[r] > target:
                    r -= cnt[arr[r]]
                else:
                    if arr[i] != arr[l] != arr[r]:
                        res += cnt[arr[i]] * cnt[arr[l]] * cnt[arr[r]]
                    elif arr[i] == arr[l] != arr[r]:
                        res += cnt[arr[i]] * (cnt[arr[i]] - 1) * cnt[arr[r]] // 2
                    elif arr[i] != arr[l] == arr[r]:
                        res += cnt[arr[i]] * cnt[arr[l]] * (cnt[arr[l]] - 1) // 2
                    else:
                        res += cnt[arr[i]] * (cnt[arr[i]] - 1) * (cnt[arr[i]] - 2) // 6
                    l += cnt[arr[l]]
                    r -= cnt[arr[r]]
            i += cnt[arr[i]]
        return res % 1000000007
