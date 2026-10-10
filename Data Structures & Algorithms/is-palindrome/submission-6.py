class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_text = s[::-1]
        reversed_text = reversed_text.strip()
        print(reversed_text)
        if s == reversed_text:
            return True

        return False
        