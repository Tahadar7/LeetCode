class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()        # values accessed as hashTable
        for num in arr: 
            if 2 * num in seen or (num // 2 in seen and num % 2 == 0):              # if double in set or its exactly half in set
                return True
            seen.add(num)
        return False
        