'''
This solution employs a brute-force approach to remove duplicates from an array.
The main ideia here is: If there is a duplicate, they will be one after each other, and the reason is the array being sorted.
1. Iterate through the array:
For each element in the array, examine the next element.
When a duplicate element is encountered, one of the duplicate elements is replaced with the number 101 (check the problem's constraints at leetcode to understand the reason why this substitution is valid).

2. After processing all elements, sort the modified array.

3. Calculate and return the size of the array after duplicates are removed:
If duplicates were found, count the number of elements in the array before reaching 101 and return this count.
If no duplicates were found, return the original length of the array.
This approach ensures that duplicates are handled by replacing one of them with 101 and then returns the size of the array based on the presence of duplicates.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=False # Set a flag to keep track if a duplicate is found
        if len(nums)==1: # If there is only one elemente return
            return 1
        m=0 # Start the counter variable
        for i in range(len(nums)-1): # For every element in array
            j=1
            k=i
            now=nums[i]
            while(k+j<len(nums) and now==nums[k+j]): # Check the elements that come right after current element
                # While the numbers are equal
                nums[k+j]=101 # Replace value to 101
                flag=True # Set flag True, a duplicate is found
                j+=1 
        nums.sort() # Sort array
        if flag: # If duplicate was found
            while(nums[m]<101):
                m+=1 # Count the number of elements before reaching 101
            return m # Return count
        else:
            return len(nums) # Return the original length of the array if no duplicates were found