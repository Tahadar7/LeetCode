class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:      # if no same pattern
            return ""

        gcd = math.gcd(len(str1), len(str2))        # gcd of str lengths
        return str1[:gcd]    # ans is prefix of length gcd
        