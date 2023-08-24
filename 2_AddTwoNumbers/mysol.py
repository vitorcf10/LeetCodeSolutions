'''
This is my first solution to the problem of adding two numbers represented by a linked list, the result should also be a linked list.
For a better understanding of the problem, here we have an example: 
2->4->3 + 5->6->4 = 7->0->8 (342+564=807); note that the head of all linked lists represents the ones place, the next value represents the tens place, and so on.
Therefore, my approach to solving the problem will be to add the elements at the same index and check for overflow, which should be added to the sum at the next index. 
Also if one list is longer than the other, we can treat the missing positions in the shorter list as zeros .
The result is first stored in an auxiliary array and then the array is transformed into a linked list in order to return the result with the correct data type.
A possible optimization would be instead of using the auxiliary array to store the result, use a linked list directly.
'''

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
        result = list() # Initialize the auxiliary array for result
        nodeans = list() # Initialize the auxiliary array that will transform the result array into a linked list
        carry = 0 # Variable to store the carry after each sum
        templ1=l1 # Pointer to head of linked list 1
        templ2=l2 # Pointer to head of linked list 2
        while(templ1 and templ2): # While both pointers are not None
            if((templ1.val+templ2.val+carry)>=10): # If the sum at index is greater than or equal 10
                result.append(((templ1.val+templ2.val+carry)%10)) # Append to result the remainder(by 10) of the sum at index
                carry = 1 # Set carry to 1
            else: # If the sum at index is less than 10
                result.append(templ1.val+templ2.val+carry) # Append to result the sum at index
                carry =  0 # Set carry to 0
            templ1=templ1.next # Move both pointers to next index
            templ2=templ2.next
        if(templ1): # If the while loop stopped because the linked list 2 pointer is None
            while(templ1): # While the pointer for linked list 1 is not None
                result.append((templ1.val+carry)%10) # Append to result the remainder(by 10) of the sum(value+carry)
                if(templ1.val+carry>=10): # If the sum at position is greater than or equal 10
                    carry=1 # Set carry to 1
                else:  # If the sum at position is less than 10
                    carry=0 # Set carry to 0
                templ1=templ1.next # Move pointer to next index
        if(templ2): # If the while loop stopped because the linked list 1 pointer is None
            while(templ2): # While the pointer for linked list 2 is not None
                result.append((templ2.val+carry)%10) # Append to result the remainder(by 10) of the sum(value+carry)
                if(templ2.val+carry>=10): # If the sum at position is greater than or equal 10
                    carry=1 # Set carry to 1
                else: # If the sum at position is less than 10
                    carry=0 # Set carry to 0
                templ2=templ2.next # Move pointer to next index
        if carry == 1: # If at the end of all computation carry is 1
            result.append(carry) # Append carry
        # At this point the complete sum is stored in result, the following code will create a linked list with the values in resulto
        for i in range(len(result)):
            nodeans.append(ListNode(val=(result[i]))) # Create a list node for every value inside result and store them in a list of nodes
        for i in range(len(result)): # For every node link them in order to create a linked list
            if i==(len(result)-1): # If it is the last element .next should point to None
                nodeans[i].next=None
            else: # Else .next should point to the node at next index
                nodeans[i].next=nodeans[i+1]
        return nodeans[0] # Return the node at index 0, head of result