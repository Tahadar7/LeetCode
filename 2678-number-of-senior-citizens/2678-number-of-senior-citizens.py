class Solution:
    def countSeniors(self, details: List[str]) -> int:
        if not details:
            return 0
        
        cnt = 0
        for each in details:
            if int(each[11] + each[12]) > 60:
                cnt +=1
        return cnt
        