'''
In this solution for every current char check the next char, if the next char is greater than current char subtract current from final answer.
If next char is less than or equal to current char, current char should be added to the solution, also if there is no next char(end of string) add current char.
For this create a dictionary that stores as keys the romam char and as values its decimal representation.
This approach is slightly better than the previous one because it has fewer if statements, eventhough time complexity is the same.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict() # Create auxiliary dict with Roman numeral as key and decimal representation as value.
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        ans = 0 # Initialize answer
        i=0
        for i in range(0, len(s)-1): # For every char in input string
            if (d[s[i]]) < (d[s[i+1]]): # Check if next char is greater than current
                ans+=(-d[s[i]]) # If so, subtract current char from answer
            else: # If next char is equal or less than current
                ans+=(d[s[i]]) # Add current char to answer
        if len(s)==1: # If input string has only one char
            return d[s] # Return the decimal representation of the char
        else: # Else
            ans+=(d[s[i+1]]) # Add the last char
            return ans # Return answer