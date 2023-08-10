# This solution has less time complexity, it uses de logic described in my previous solution also in this folder.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        ans = 0
        i=0
        for i in range(0, len(s)-1):
            if (d[s[i]]) < (d[s[i+1]]):
                ans+=(-d[s[i]])
            else:
                ans+=(d[s[i]])
        if len(s)==1:
            return d[s]
        else:
            ans+=(d[s[i+1]])
            return ans