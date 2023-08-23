'''
This is a brute force solution for the two-sum problem. 
It iterates through every combination of two numbers until it finds the numbers that add up to the target.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1): # For loop to iterate through every element
            j=i+1 #Set the pointer j to the next element
            while (j<(len(nums))): # While j is less than the array length 
                if(nums[i]+nums[j]==target): # Check if the sum of the element at index i and j add up to target
                    tgti=i # If so save the index of i and j.
                    tgtj=j
                j+=1 # If the sum does not add up to target go to the next element
        sol=[tgti, tgtj] # Solution is the combination of the index saved for i and j
        return sol # Return solution