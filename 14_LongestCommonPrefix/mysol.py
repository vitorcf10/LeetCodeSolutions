'''
To identify the longest common prefix among a list of strings, the code systematically compares characters in the same position across all strings. The process is as follows:
For each string in the input array:
Examine each character from left to right.
If the first character is the same for all strings, add that character to the answer, and move to next char.
Break the loop as soon as:
- A character is encountered that is different across the strings.
- One of the input strings has no more chars.
If there is no common prefix, the loop terminates during the first iteration, and an empty string ("") is returned as the result.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        j=0 # Pointer that keeps track of the current longest common prefix
        ans="" # Initialize answer
        result=True # Initialize a flag that will be used to break the loop if a condition is not met
        if len(strs)==1 or strs[0]=="": # If there is only one string or the input string is empty
            return(strs[0]) # Return input string
        while True:    
            for i in range(len(strs)-1): # For every word in input
                try: # Try statement will check if the strings being compared are not over
                    if strs[i][j]!=strs[i+1][j]: # Check if the char at index j is not equal in current word and next word
                        result=False # Set result flag to false, the common prefix is over(different chars were found in same position for different words)
                except: # If one of the strings is over, an index error will be handled
                    result=False # Set result flag to false, there are no more chars to compare in one string
            if result == True: # If the flag is true all letters at index j are the same for all words in the input
                ans+=strs[0][j] # Therefore, add letter at index j to answer as it is a common prefix
                j+=1 # Move j to check for the next letter in all words
            if result == False: # If the flag became false for any reason
                break # Break the loop and return current answer
        return(ans) # Return the built answer