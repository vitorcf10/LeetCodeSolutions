class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=False
        if len(nums)==1:
            return 1
        m=0
        for i in range(len(nums)-1):
            j=1
            k=i
            now=nums[i]
            while(k+j<len(nums) and now==nums[k+j]):
                nums[k+j]=101
                flag=True
                j+=1
        nums.sort()
        if flag:
            while(nums[m]<101):
                m+=1
            return m
        else:
            return len(nums)