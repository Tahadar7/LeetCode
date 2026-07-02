class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [0] * 3
        left = 0
        ans = 0
        for right in range(len(s)):
            # ord converts char to ascii integers
            cnt[ord(s[right]) - ord('a')] += 1

            while cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0:
                # if abc found then valid at the end
                ans += len(s) - right    
                cnt[ord(s[left]) - ord('a')] -= 1   # shrink window
                left += 1

        return ans