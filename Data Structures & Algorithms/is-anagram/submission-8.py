class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if count(s) == count(t):
            return True

        return False
        