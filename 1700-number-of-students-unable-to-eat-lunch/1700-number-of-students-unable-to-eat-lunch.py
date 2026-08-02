class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # how many students
        count = Counter(students)

        for sand in sandwiches:   
            if count[sand] > 0:
                count[sand] -= 1   # student get sand
            else:
                return sum(count.values()) 
        return 0