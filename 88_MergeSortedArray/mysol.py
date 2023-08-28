'''
Problem: Merge 2 sorted arrays in-place, the function should not create a third array, nums1 has to be modified.
Solution: The problem constraints state that after the nums1 array is over, it is filled with n zeros where n is the length of nums2.
Example: nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]; the problem also provides the sizes of both arrays, disregarding the zeroes. In this case, the sizes are 3 for both arrays.
Therefore, the approach here is iterate through nums1 from the first index where value is 0 until the end of the array, in each iteration change the value 0 for the respective value in the nums2 array, this way merging both arrays.
When the merging is complete, sort nums1.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0 # Start the iterator variable to loop through nums2
        for j in range(m, m+n): # Iterate through nums1 from the first index where value is 0 until the end of the array.
            nums1[j]=nums2[i] # Change the value 0 in nums1 to the correct value in nums2.
            i+=1 # Add the nums2 iterator to go to next index
        nums1.sort() # Sort nums1
