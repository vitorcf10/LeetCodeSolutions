'''
Although this is a valid solution, it is slightly inefficient due to too many if-statements.
The best solution would be to consider that in Roman Numerals if a smaller value appears before a larger value, it represents subtraction, 
while when a smaller or equal value appears after to a larger value, it represents an addition. I learned that with @kshatriyas's solution.
I am sharing this solution because it was my first thinking process and correct answer by leetcode. Also, this solution is O(1) space complexity.
Here the main idea is to look at every single char from the input string and add its value to the final answer, numerals like C, X, and I have to have the next numeral also checked in order to decide how they will add up in the final answer.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        i=0
        while(i<len(s)): # Iterate through the input string
            if s[i]=='M': # If char is M add 1000 to answer
                ans+=1000
            elif s[i]=='D': # If char is D add 500 to answer
                ans+=500
            elif s[i]=='C': # If char is C
                try: # Try-except statement in case C is the last char of the string
                    if s[i+1]=='D': # And the next char is D add 400 to answer
                        ans+=400
                        i+=1
                    elif s[i+1]=='M': # And the next char is D add 900 to answer
                        ans+=900
                        i+=1
                    else: # If it is any other char add 100 to answer
                        ans+=100
                except:
                    ans+=100
            elif s[i]=='L': # If char is L add 50 to answer
                ans+=50
            elif s[i]=='X': # If char is X
                try: # Try-except statement in case X is the last char of the string
                    if s[i+1]=='L': # And the next char is L add 40 to answer
                        ans+=40
                        i+=1
                    elif s[i+1]=='C': # And the next char is C add 90 to answer
                        ans+=90
                        i+=1
                    else: # If it is any other char add 10 to answer
                        ans+=10
                except: 
                    ans+=10
            elif s[i]=='V': # If char is V add 5 to answer
                ans+=5
            elif s[i]=='I': # If char is I
                try: # Try-except statement in case I is the last char of the string
                    if s[i+1]=='V': # And the next char is V add 4 to answer
                        ans+=4
                        i+=1
                    elif s[i+1]=='X': # And the next char is X add 9 to answer
                        ans+=9
                        i+=1
                    else: # If it is any other char add 1 to answer
                        ans+=1
                except:
                    ans+=1
            i+=1
        return ans # Return answer after iterating through string