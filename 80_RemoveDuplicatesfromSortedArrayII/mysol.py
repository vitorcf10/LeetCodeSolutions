class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=0
        c=0
        i=1
        while i<len(nums):
            if(nums[i-1]==nums[i]):
                c+=1
                if c>=2:
                    nums[i-1]=10001
                    size+=1
            else:
                c=0
            i+=1
        nums.sort()
        return(len(nums)-size)