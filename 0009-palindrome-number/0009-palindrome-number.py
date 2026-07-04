class Solution:
    def isPalindrome(self, x: int) -> bool:
        # -ve number or number ending with zero cannot be palindrome
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reverse_half = 0
        while x > reverse_half:
            reverse_half = reverse_half * 10 + x % 10
            x //= 10
        
        return x == reverse_half or x == reverse_half // 10

        

        