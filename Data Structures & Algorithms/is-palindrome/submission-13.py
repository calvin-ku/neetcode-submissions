class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s[::-1].replace(" ", "") == s:
            return True

        return False
        