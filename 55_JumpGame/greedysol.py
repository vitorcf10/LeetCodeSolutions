class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        indjump=0
        nextj=0
        maxsoma=0
        flag=None
        arr=[]
        while indjump<len(nums)-1:
            if nums[indjump]==0:
                return False
            if nums[indjump]>=len(nums)-1-indjump:
                return True
            else:
                nextj=0
                maxsoma=0
                found=0
                arr=nums[indjump+1:indjump+nums[indjump]+1]
                for i in range(len(arr)):
                    soma=i+arr[i]
                    if soma>len(arr)-1:
                        found=1
                        flag=False
                        if soma>maxsoma:
                            maxsoma=soma
                            nextj=indjump+i+1
                    elif found==0:
                        flag=True
                if flag:
                    return False
                indjump=nextj