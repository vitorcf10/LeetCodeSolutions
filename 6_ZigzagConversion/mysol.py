class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        repfirst=numRows+(numRows-2)
        d={}
        c=0
        finalstring=''
        if numRows>=len(s):
            return s
        if numRows==1:
            return s
        repfirst=numRows+(numRows-2)
        for j in range(numRows):
            d[j]=''
        while c < len(s):
            if c%repfirst<numRows:
                pos=c%repfirst
                d[pos]+=s[c]
            else:
                rest=c%repfirst
                place=repfirst-rest
                d[place]+=s[c]
            c+=1
        for i in range(len(d)):
            finalstring+=d[i] 
        return(finalstring)