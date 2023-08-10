class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k=0
        i=0
        savepos=0
        save=-1
        while i < (len(haystack)):
            if haystack[i]==needle[k]:
                k+=1
                if k == 1:
                    savepos=i
                if k==len(needle):
                    save=i
                    break
            elif haystack[i]!=needle[k] and k!=0:
                i=savepos
                k=0
            else:
                k=0
            i+=1
        firstoccur=save-len(needle)+1
        if save != -1:
            return(firstoccur)  
        else:
            return(save)