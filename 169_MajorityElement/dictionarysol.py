class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=dict()
        freqmax=0
        key=0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
            if freq[nums[i]]>freqmax:
                freqmax=freq[nums[i]]
                key=nums[i]
        return key