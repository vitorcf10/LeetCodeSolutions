class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        i=-1
        while(s[i]!=' ' and i>-len(s)):
            i-=1
        if i == -len(s):
            return(abs(i))
        else:
            return(abs(i+1))