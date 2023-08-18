class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        index=0
        if len(citations)==0:
            return(index)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                index+=1
            else:
                break
        return(index)