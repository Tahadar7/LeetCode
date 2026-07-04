class Solution:
    def isPalindrome(self, x: int) -> bool:
        # -ve number or number ending with zero cannot be palindrome
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reverse_half = 0    # check half reverse
        while x > reverse_half:
            reverse_half = reverse_half * 10 + x % 10
            x //= 10
        
        # ignore middle digit for even case
        return x == reverse_half or x == reverse_half // 10

        

        