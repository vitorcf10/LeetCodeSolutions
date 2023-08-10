class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstr = str(x)
        ans=True
        maxiter=int(len(xstr)/2)
        for i in range(maxiter):
            if xstr[i]==xstr[-i-1]:
                ans=True
            else:
                ans=False
                break
        return ans