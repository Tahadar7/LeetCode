class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:               # 0 or less
            return False
        while n > 1:            
            if n % 3 != 0:      # if not dvisible by 3 
                return False
            n //= 3             # divide by 3

        return True             # check if n is 1
        