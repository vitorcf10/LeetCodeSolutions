class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=""
        if s=='' or s is None or len(s)==0:
            return output
        s=s.split()
        s=list(reversed(s))
        for i in range(len(s)):
            output+=(" "+ s[i])
        output=output.strip()
        return(output)