'''
This solution iterates through the array while maintaining an auxiliary dictionary. 
The dictionary records each distinct number in the array as a key, along with its frequency as the corresponding value.
Then, the algorithm identifies and returns the key (number) with the highest frequency, which corresponds to the majority element in the array.
This solution has better time complexity and worse space complexity compared to the other solution in this directory.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=dict() # Initialize auxiliary dict
        freqmax=0 # Initialize variable to keep max frequency
        key=0
        for i in range(len(nums)): # Iterate through each element in the array
            if nums[i] not in freq: # If the current element is not in the dictionary
                freq[nums[i]]=1 # Add the element to dictionary and give frequency of 1
            else: # If the current element is already in the dictionary
                freq[nums[i]]+=1 # Increase its frequency
            if freq[nums[i]]>freqmax: # If the frequency of the current element is greater than the max frequency
                freqmax=freq[nums[i]] # The max frequency is now the frequency of current element
                key=nums[i] # And the majority element is the current element 
        return key # Return the majority element