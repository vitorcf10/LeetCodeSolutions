class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size_one=0
        startindex=0
        endindex=0
        maxfreq=0
        shortsize=float('inf')
        size=list()
        mapp=dict()
        for i in range(len(nums)):
            if nums[i] not in mapp:
                firstindex=i
                lastindex=i
                frequency=1
                mapp[nums[i]]=[firstindex, lastindex, frequency]
            else:
                mapp[nums[i]][1]=i
                mapp[nums[i]][2]+=1
            if mapp[nums[i]][2]>maxfreq:
                maxfreq=mapp[nums[i]][2]
        size=list(mapp.values())
        for tup in (size):
            if tup[2]==maxfreq:
                size_one=tup[1]-tup[0]+1
                if size_one<shortsize:
                    shortsize=size_one        
        return shortsize