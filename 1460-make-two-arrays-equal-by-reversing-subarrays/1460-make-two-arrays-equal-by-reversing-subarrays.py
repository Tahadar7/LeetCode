class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Counter: Dictionary mapping per time items
        return Counter(target) == Counter(arr)  
        