class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {'2': 'abc', '3' : 'def', '4' :'ghi' , '5' : 'jkl', '6': 'mno', 
        '7': 'pqrs', '8': 'tuv', '9' : 'wxyz' }
        if not digits:
            return []

        n = len(digits)
        answer = []
        solution = []

        def backtrack(i):
            if i == n:
                answer.append(''.join(solution))
                return
            
            num = digits[i]
            for c in h[num]:
                solution.append(c)
                backtrack(i+1)
                solution.pop()
                
        backtrack(0)
        return answer
        