'''
This solution should return true if the input number is a palindrome and false if not. A palindrome number is a number that is read the same way the other way around.
Example:
121 --> true
1221 --> true
1321 --> false
Therefore, my approach is to use 2 pointers one starts at the first digit, and the other starts at the last digit, if they are the same move both pointers to next digit and compare again. 
If the comparison fails return false, if all comparisons are valid return true.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstr = str(x) # Make x a string
        ans=True # Set the answer to start with true
        maxiter=int(len(xstr)/2) # Define the max number of comparisons needed to tell if the number is a palindrome
        for i in range(maxiter): # For every comparison
            if xstr[i]==xstr[-i-1]: # Use reverse indexing to apply the 2 pointer strategy and compare the beginning and end of number.
                ans=True # If all comparisons are true return true
            else: # If 1 comparison fails
                ans=False # Answer is false
                break # Break loop
        return ans # Return answer