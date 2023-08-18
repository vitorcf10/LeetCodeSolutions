class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        finalprod=1
        countzero=0
        zeropos=-1
        for i in range(len(nums)):
            if nums[i]==0:
                countzero+=1
                zeropos=i
                if countzero>1:
                    return [0]*len(nums)
            else:
                finalprod=finalprod*nums[i]
        if countzero==1:
            answer=[0]*len(nums)
            answer[zeropos]=finalprod
            return answer
        else:
            for i in range(len(nums)):
                answer.append(finalprod//nums[i])
            return answer