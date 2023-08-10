class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        auxdict = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in auxdict:
                sol=[auxdict[need], i]
            else:
                auxdict[nums[i]]=i
        return sol