**My Solution**</br> 
&ensp;  Description: This solution should return true if the input number is a palindrome and false if not. A palindrome number is a number that is read the same way the other way around.</br> 
Example:</br> 
121 --> true</br> 
1221 --> true</br> 
1321 --> false</br> 
&ensp;  Therefore, my approach is to use 2 pointers one starts at the first digit, and the other starts at the last digit, if they are the same move both pointers to the next digit and compare again. If the comparison fails return false, if all comparisons are valid return true.</br> 
</br>
_Time Complexity_: O(n), if 'n' is the number of digits in the input integer the total of iterations would be around n/2, therefore O(n).</br> 
_Space Complecity_: O(1), there aren't auxiliary variables proportional to n.
