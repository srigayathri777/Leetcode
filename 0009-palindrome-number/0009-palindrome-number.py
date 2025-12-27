class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverse = int(str(x)[::-1])
        return x == reverse

