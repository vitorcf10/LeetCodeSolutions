'''
Given the problem's condition that the majority element appears in the array more than half the time:
Sort the array.
Return the element at the index size // 2.
As it is guaranteed to be the majority element based on the problem statement. 
This is because the majority element will occupy at least half of the array after sorting.
This solution has better space complexity and worse time complexity compared to the other solution in this directory.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # Sort the array
        n = len(nums) # Get the size
        return nums[n//2] # Return the element in the middle