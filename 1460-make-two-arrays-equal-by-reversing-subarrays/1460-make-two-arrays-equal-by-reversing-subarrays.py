class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if not target or not arr:
            return False

        # Counter: Dictionary mapping per time items
        return Counter(target) == Counter(arr)  
        