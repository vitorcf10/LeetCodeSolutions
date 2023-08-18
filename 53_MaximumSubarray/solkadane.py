class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum=0
        maxSum=-10001
        for i in range(len(nums)):
            currSum+=nums[i]
            if currSum>maxSum:
                maxSum=currSum
            if currSum<0:
                currSum=0
        return(maxSum)