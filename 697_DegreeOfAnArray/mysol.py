'''
For more details on the problem itself, check leetcode.com. In this solution, an auxiliary dictionary is created.
The numbers in the array are keys and their respective value is a list with the following structure [first time key appears in array, last time key appears in array, frequency of key in array].
With the dictionary, it is possible to find out the numbers with max frequency, within the max frequency numbers return the minimum sub array size, and each sub-array size is given by --> 1 + last time key appears in array - first time key appears in array.
'''
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size_one=0 # Variable that will store the size of each sub array of max frequency
        maxfreq=0 # Variable to store max frequency
        shortsize=float('inf') # Initialize the shortest size with infinity(any size is shorter)
        size=list() # List that will store all values of the dictionary
        mapp=dict() # Auxiliary dictionary
        for i in range(len(nums)): # Create dictionary based on numbers in array
            if nums[i] not in mapp: # If number is not a key in dictionary yet
                firstindex=i # Set first index to current index
                lastindex=i # Set last index to current index
                frequency=1 # Set frequency to 1
                mapp[nums[i]]=[firstindex, lastindex, frequency] # Add key-value pair to dictionary
            else: # If number is already in dictionary
                mapp[nums[i]][1]=i # Change last index to current index
                mapp[nums[i]][2]+=1 # Add 1 to frequency
            if mapp[nums[i]][2]>maxfreq: # If frequency of current key is greater than max frequency
                maxfreq=mapp[nums[i]][2] # Max frequency is now the frequency of current element
        # Dictionary ready
        size=list(mapp.values()) # Make all values of dictionary a list
        for tup in (size): # For every tuple inside the list
            if tup[2]==maxfreq: # If the frequency of the tuple equals max frequency
                size_one=tup[1]-tup[0]+1 # Size of sub-array is --> last index - first index + 1
                if size_one<shortsize: # If size of current sub-array is less than min size
                    shortsize=size_one # Min size is now the current sub-array size      
        return shortsize # Return minimun sub-array size of maximun frequency