class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if not arr:
            return False
        for i in range(0, len(arr)-2):  # start with 0 but bound to last element
            if arr[i] % 2 != 0:
                if arr[i + 1] % 2 != 0 and arr[i+2] % 2 != 0:
                    return True
        
        return False
             

        