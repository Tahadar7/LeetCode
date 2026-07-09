class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)   # max candies a kid have
        # >= with max candies are ture
        return [c+extraCandies >= max_candies for c in candies] 
        