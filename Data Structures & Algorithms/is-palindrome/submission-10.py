class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_text = s[::-1]
        reversed_text = reversed_text.replace(" ", "")
        print(reversed_text)
        s = s.replace(" ", "")
        print(s)
        if s.replace(" ", "") == reversed_text:
            return True

        return False
        