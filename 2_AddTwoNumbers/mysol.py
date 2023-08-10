# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = list()
        nodeans = list()
        carry = 0
        templ1=l1
        templ2=l2
        while(templ1 and templ2):
            if((templ1.val+templ2.val+carry)>=10):
                result.append(((templ1.val+templ2.val+carry)%10))
                carry = 1
            else:
                result.append(templ1.val+templ2.val+carry)
                carry = 0
            templ1=templ1.next
            templ2=templ2.next
        if(templ1):
            while(templ1):
                result.append((templ1.val+carry)%10)
                if(templ1.val+carry>=10):
                    carry=1
                else: 
                    carry=0
                templ1=templ1.next
        if(templ2):
            while(templ2):
                result.append((templ2.val+carry)%10)
                if(templ2.val+carry>=10):
                    carry=1
                else: 
                    carry=0
                templ2=templ2.next
        if carry == 1:
            result.append(carry)
        for i in range(len(result)):
            nodeans.append(ListNode(val=(result[i])))
        for i in range(len(result)):
            if i==(len(result)-1):
                nodeans[i].next=None
            else:
                nodeans[i].next=nodeans[i+1]
        return nodeans[0]