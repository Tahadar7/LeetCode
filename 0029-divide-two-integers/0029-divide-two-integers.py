class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend/divisor

        if ans > 2**31 -1:
            return 2**31 - 1
        elif ans < -2**31:
            return -2**31
        else:
           return int(ans)