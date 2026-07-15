class Solution:
    def alternateDigitSum(self, n: int) -> int:
        nums = list(map(int, str(n)))       # convert n to list of int

        ans = 0
        sign = 1
        for num in nums:
            ans += sign * num
            sign *= -1              # if - then + vice versa
        return ans
        