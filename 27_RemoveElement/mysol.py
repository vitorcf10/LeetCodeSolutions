'''
Problem: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Solution: The problem constraints state that 0 <= val <= 100. 
Therefore, the idea is to iterate through the array, and each time "val" appears, change the value at that index to 101 and increment a counter by 1. 
At the end of the loop, sort the elements. 
This way, all numbers that are not equal to "val" will be in the first positions of the array, and return the size of the array without "val" by subtracting the counter from the original length.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0 # Initialize counter to 0
        og=len(nums) # Get the original length of the array before the removal of val
        for i in range(len(nums)): # For each position in the array
            if nums[i]==val: # If the number at index is equal to val
                counter+=1 # Add 1 to counter
                nums[i]=101 # Change the value at index to 101
        # The loop is now over, therefore val is eliminated from the array
        nums.sort() # Sort the array to make all the instances of 101 go to the end of the array
        return og-counter # Return the size of the array without val by subtracting the amount of times val is in the array from the original size of input