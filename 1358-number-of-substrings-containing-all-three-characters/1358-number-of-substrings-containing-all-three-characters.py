class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s:
            return 0
        last = [-1,-1,-1]
        ans = 0

        for i, c in enumerate(s):
            # ord converts char to ascii integers
            last[ord(c) - ord('a')] = i         # last seen at index
            ans += min(last) + 1

        return ans