class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        words=s.split()
        return len(words[-1]) if words else  0
        