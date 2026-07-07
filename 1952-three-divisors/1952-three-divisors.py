class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        
        count = 2               # for 1 and n
        for i in range(2,n):
            if n % i == 0:
                count +=1
            
            if count > 3:
                return False
        return count == 3
        