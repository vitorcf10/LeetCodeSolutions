# Can be solved in a much easier way if in the dictionary is included all possible romam numerals or if in dictionary include the 900, 400, 90, 40 etc.
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = dict()
        d[1] = 'I'
        d[5] = 'V'
        d[10] = 'X'
        d[50] = 'L'
        d[100] = 'C'
        d[500] = 'D'
        d[1000] = 'M'
        finalStr=''
        repeat=''
        pre=''
        strn=str(num)
        samecounter=0
        for i in range(len(strn)):
            goal = (int(strn[i])*10**(len(strn)-1-i))
            iterr=0
            value=1
            while goal-value>=0:
                rest=goal-value
                if iterr%2==0:
                    value*=5
                else:
                    value*=2
                iterr+=1
                if goal-value<0:
                    if iterr%2==0:
                        value=value//2
                    else:
                        value=value//5
                    finalStr = finalStr+d[value]
                    if len(finalStr)>1:
                        if finalStr[len(finalStr)-2]==finalStr[len(finalStr)-1]:
                            samecounter+=1
                        else:
                            samecounter=0
                    if samecounter==3:
                        repeat=finalStr[-1]
                        if strn[0]=='4' and i==0:
                            pre=''
                        else:
                            pre=finalStr[-5]
                        finalStr=finalStr[:-4]
                        if repeat=='I':
                            if pre=='V':
                                finalStr=finalStr[:-1]
                                finalStr+='IX'
                            else:
                                finalStr+='IV'
                        if repeat=='X':
                            if pre=='L':
                                finalStr=finalStr[:-1]
                                finalStr+='XC'
                            else:
                                finalStr+='XL'
                        if repeat=='C':
                            if pre=='D':
                                finalStr=finalStr[:-1]
                                finalStr+='CM'
                            else:
                                finalStr+='CD'
                    goal=rest
                    iterr=0
                    value=1
        return(finalStr)