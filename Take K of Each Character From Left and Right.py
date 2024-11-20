class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count_a, count_b, count_c = 0, 0, 0

        for ch in s:
            if ch == 'a':
                count_a += 1
            elif ch == 'b':
                count_b += 1
            elif ch == 'c':
                count_c += 1

        if count_a < k or count_b < k or count_c < k:
            return -1

        i, j = 0, 0
        not_deleted_window_size = 0

        while j < n:
            if s[j] == 'a':
                count_a -= 1
            elif s[j] == 'b':
                count_b -= 1
            elif s[j] == 'c':
                count_c -= 1

            while i <= j and (count_a < k or count_b < k or count_c < k):
                if s[i] == 'a':
                    count_a += 1
                elif s[i] == 'b':
                    count_b += 1
                elif s[i] == 'c':
                    count_c += 1
                i += 1

            not_deleted_window_size = max(not_deleted_window_size, j - i + 1)
            j += 1

        return n - not_deleted_window_size
