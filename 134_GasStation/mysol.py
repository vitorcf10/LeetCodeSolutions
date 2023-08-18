
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curtank=0
        start=0
        if sum(cost)>sum(gas):
            return -1
        for i in range (len(gas)):
            curtank+=(gas[i]-cost[i])
            if curtank<0:
                start=i+1
                curtank=0
        return start