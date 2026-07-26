class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()        # values accessed as hashTable
        for num in arr:
            # if double in set or its exactly half in set 
            if 2 * num in seen or (num // 2 in seen and num % 2 == 0):
                return True
            seen.add(num)
        return False
        