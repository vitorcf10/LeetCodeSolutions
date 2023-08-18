class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pleft=[1]*len(nums)
        pright=[1]*len(nums)
        answer=[]
        for i in range(1, len(nums)):
            pleft[i]=pleft[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            pright[i]=pright[i+1]*nums[i+1]
        for i in range(0, len(nums)):
            answer.append(pright[i]*pleft[i])
        return(answer)