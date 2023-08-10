class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        j=0
        ans=""
        result=True
        if len(strs)==1 or strs[0]=="":
            return(strs[0])
        while True:    
            for i in range(len(strs)-1):
                try:
                    if strs[i][j]!=strs[i+1][j]:
                        result=False
                except:
                    result=False
            if result == True:
                ans+=strs[0][j]
                j+=1
            if result == False:
                break
        return(ans)