class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels= {'a', 'e', 'i', 'o', 'u'}  # set for vowels
        l = res = count = 0

        for i in range(len(s)):
            count += 1 if s[i] in vowels else 0

            if i-l+1 > k:   # window size
                count -= 1 if s[l] in vowels else 0     # decrease count if l is vowel
                l += 1      # move left pointer
            res = max(count, res)

        return res

            
            

        