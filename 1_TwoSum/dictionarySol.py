'''
This is the dictionary/hashmap solution for the two-sum problem. 
The main idea here is to have an auxiliary dictionary that stores every element in the array as a key and their indexes as values. 
For every element, calculate the element that is needed for the sum to add up to the target (needed = target - element). 
Then, check to see if the element is already in the auxiliary dictionary. 
If it is, return the element's index and the value of the key needed in the dictionary. If it isn't, just add the element to the dictionary.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        auxdict = dict() # Create auxiliar dictionary
        for i in range(len(nums)): # For loop to iterate through every element in array
            need = target - nums[i] # Calculate the needed number for current element
            if need in auxdict: # If the needed number is in dict
                sol=[auxdict[need], i] # Solution is the combination of the value at key=needed plus the current element index
            else:
                auxdict[nums[i]]=i # If needed not in dict, add the key-value pair as number-index in the dictionary
        return sol # Return solutions