class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # sorted desc the list with heights, zip pairs both
        return [n for h, n in sorted(zip(heights,names),reverse=True)] 

    

        