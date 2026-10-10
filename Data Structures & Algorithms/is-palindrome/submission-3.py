class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_text = s[::-1]
        reverse_text = reverse_text.strip()
        if s == reversed_text:
            return True

        return False
        