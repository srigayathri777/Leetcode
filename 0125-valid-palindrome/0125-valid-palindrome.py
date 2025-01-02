class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ''.join(char.lower() for char in s if char.isalnum())
        return normalized==normalized[::-1]
        