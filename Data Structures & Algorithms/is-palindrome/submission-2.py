class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_text = s[::-1]
        if s == reversed_text:
            return True

        return False
        