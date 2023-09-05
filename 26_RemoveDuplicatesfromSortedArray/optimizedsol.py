'''
This solution implements a two-pointer strategy. Specifically:

The i pointer iterates through the elements in the array.
The j pointer is advanced only when a new element is found. 
When a new element is encountered, it is inserted at the position j, and then j is incremented to the next position. 
This effectively removes duplicates from the array while maintaining the order of distinct elements.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1 # Set j to the second position of the array
        for i in range(1, len(nums)): # Iterate with i
            if nums[i-1]!=nums[i]: # If the numbers side by side are not equal, means that a new unique element was found at index i
                nums[j]=nums[i] # Let the array at index j assume the value of a new unique element
                j+=1 # Send j to next position
        return j # j is the size of the array with no duplicates as it is incremented every time a unique element is found