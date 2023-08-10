# Although this is a valid solution, it is really inefficient due to too much if-statements
# The best solution would be considering that in Roman Numerals if a smaller value appears before a larger value, it represents subtraction, 
# while when a smaller value appears after or equal to a larger value, it represents addition. I learned that with @kshatriyas's solution.
# I am sharing this solution because it was my first thinking process and correct answer by leetcode.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        i=0
        while(i<len(s)):
            if s[i]=='M':
                ans+=1000
            elif s[i]=='D':
                ans+=500
            elif s[i]=='C':
                try:
                    if s[i+1]=='D':
                        ans+=400
                        i+=1
                    elif s[i+1]=='M':
                        ans+=900
                        i+=1
                    else:
                        ans+=100
                except:
                    ans+=100
            elif s[i]=='L':
                ans+=50
            elif s[i]=='X':
                try:
                    if s[i+1]=='L':
                        ans+=40
                        i+=1
                    elif s[i+1]=='C':
                        ans+=90
                        i+=1
                    else:
                        ans+=10
                except: 
                    ans+=10
            elif s[i]=='V':
                ans+=5
            elif s[i]=='I':
                try:
                    if s[i+1]=='V':
                        ans+=4
                        i+=1
                    elif s[i+1]=='X':
                        ans+=9
                        i+=1
                    else:
                        ans+=1
                except:
                    ans+=1
            i+=1
        return ans