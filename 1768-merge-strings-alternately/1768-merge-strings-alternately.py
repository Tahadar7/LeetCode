class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A,B= len(word1), len(word2)
        i, j = 0, 0
        res = []

        while i < A and j < B:    # until if any string complete
            res.append(word1[i])
            i += 1
            res.append(word2[j])
            j += 1
        
        res.append(word1[i:])
        res.append(word2[j:])

        return ''.join(res)    # convert list to string


        