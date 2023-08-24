**My Solution**<br />
&ensp; Description: This is my first solution to the problem of adding two numbers represented by a linked list, the result should also be a linked list. For a better understanding of the problem, here we have an example:<br /> 
2->4->3 <br />+ <br />5->6->4 <br />= <br />7->0->8 <br />(342+564=807) <br />
Note that the head of all linked lists represents the ones place, the next value represents the tens place, and so on.<br />
&ensp; Therefore, my approach to solving the problem will be to add the elements at the same index and check for overflow, which should be added to the sum at the next index. Also if one list is longer than the other, we can treat the missing positions in the shorter list as zeros. The result is first stored in an auxiliary array and then the array is transformed into a linked list in order to return the result with the correct data type.
<br />&ensp;**Note:** A possible optimization would be instead of using the auxiliary array to store the result, use a linked list directly. For more details on the solution, please refer to its code; it is all extensively commented.<br /><br />
_Time Complexity:_ O(n), if we consider n as the size of the result list the code iterates a total of 3 times through every element in the result, O(3n) drop constant O(n).<br />
_Space Complexity:_ O(n), the code uses an auxiliary array of the same size as the final list(n).
