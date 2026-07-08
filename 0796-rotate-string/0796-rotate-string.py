class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        new_str = s + s    # combine s two times
        if goal in new_str:
            return True
        return False
        