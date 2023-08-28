'''
Problem: search a number in a rotated sorted array, return the index of the number if the number is found else return -1
Solution: The main idea here is to adapt the binary search algorithm. Please check the comments for instructions on how to adapt it to solve the problem.
'''
class Solution(object):
    def search(self, nums, target):
        n = len(nums) # Get the length of the input array and store it in n
        # The problem will be solved with two pointers, low starts pointing to first index and high to last index
        low = 0 # Set the low pointer to first index 0
        high = n - 1 # Set the high pointer to last index (n-1)
        while (low <= high): # While the low pointer is less than or equal to high pointer keep searching for the target
            mid = (low + high) // 2 # Store the index in the middle of the array in mid
            if (nums[mid] == target): # If numns at index mid is the target
                return mid # Return the mid index
            elif (nums[low] <= nums[mid]): # If the number at index 0 is less than or equal to the number in the middle
                if (nums[low] <= target and target <= nums[mid]): # And the target is between these 2 numbers
                    high = mid - 1 # The target might be in the left subarray, so set high to mid - 1
                else: # If the target is not between these 2 numbers
                    low = mid + 1 # The target might be in the right subarray, so set low to mid + 1
            else: # If the number at index 0 is greater than the number in the middle
                if (nums[mid] <= target and target <= nums[high]): # And the target is between the high and mid indexes 
                    low = mid + 1 # The target might be in the right subarray, so set low to mid + 1
                else: # If the target is not between the high and mid indexes 
                    high = mid - 1 # The target might be in the left subarray, so set high to mid - 1
        return -1 # If the loop is broken by low>high return -1, the target is not in the array
    # If it is still hard to understand come up with an exemple, like nums = [4,5,6,7,0,1,2], target = 0, and go step by step in the algorithm.