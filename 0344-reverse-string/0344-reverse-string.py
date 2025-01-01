class Solution:
    def reverseString(self, s):
        """
        Reverses the input list of characters in place.
        :param s: List[str]
        :return: None
        """
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1    