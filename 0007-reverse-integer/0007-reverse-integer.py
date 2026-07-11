class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1    # sign of x - or +
        x = abs(x)
        reverse = 0

        while x != 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        if reverse < -2**31 or reverse > 2**31 -1:   # if in 32 bit limit
            return 0
        
        return sign * reverse       # muiltiply with sign

        