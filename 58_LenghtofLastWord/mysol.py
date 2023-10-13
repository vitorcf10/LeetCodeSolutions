'''
The core idea is to process a given string as follows:
1. Trim any leading and trailing spaces from the string.
2. Iterate through the string in reverse, searching for the first blank space. During each iteration, increment a counter by 1 to keep track of the length of the last word.
3. If the string consists of only one word, return the length of that word. Otherwise, return the length of the last word by subtracting 1 from the counter(usage of while loop incremented 1 to the counter when the blank space is found).
This approach efficiently calculates the length of the last word in the string, handling both single-word and multi-word cases.
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip() # Trim leading and trailing spaces with str.strip()
        i=-1 # Initialize the counter to iterate in reverse order
        while(s[i]!=' ' and i>-len(s)): # While the current char of the string is not a blank and the negative counter is greater than the size of string
            i-=1 # Decrement counter
        if i == -len(s): # If the length of counter is equal to the length of string
            return(abs(i)) # Return the absolute value from the counter, meaning the input string is a sigle word.
        else: # If there is more than one word in the string.
            return(abs(i+1)) # Return the absolute value of negative counter + 1, this way taking away the blank space count.