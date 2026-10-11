class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.translate(None, string.punctuation)

        if s[::-1].replace(" ", "") == s:
            return True

        return False
        