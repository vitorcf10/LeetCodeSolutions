class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        og=len(nums)
        for i in range(len(nums)):
            if nums[i]==val:
                counter+=1
                nums[i]=101
        nums.sort()
        return og-counter