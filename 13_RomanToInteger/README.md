**First Solution**<br/>
&ensp;  Description: Although this is a valid solution, it is slightly inefficient due to too many if-statements.
The best solution would be to consider that in Roman Numerals if a smaller value appears before a larger value, it represents subtraction, 
while when a smaller or equal value appears after to a larger value, it represents an addition, I learned that with @kshatriyas's solution.<br/>
&ensp;  I am sharing this solution because it was my first thinking process and correct answer by leetcode. Also, this solution is O(1) space complexity.
Here the main idea is to look at every single char from the input string and add its value to the final answer, numerals like C, X, and I have to have the next numeral also checked to decide how they will add up in the final answer.
<br/><br/> _Time Complexity:_ O(n), iterates through every single element of the input string once.
<br/> _Space Complexity_ O(1), there are no auxiliary variables proportional to the input size.
<br/>
<br/>
**Second Solution**<br/>
&ensp;  Description: In this solution for every current char check the next char, if the next char is greater than the current char subtract the current from the final answer.
If the next char is less than or equal to the current char, the current char should be added to the solution, also if there is no next char(end of the string) add the current char.
For this create a dictionary that stores as keys the Roman char and as values its decimal representation.
This approach is slightly better than the previous one because it has fewer if statements, even though the time complexity is the same.
<br/><br/> _Time Complexity:_ O(n), iterates through every single element of the input string once.
<br/> _Space Complexity_ O(n), needs an auxiliary dictionary of size 'm', where 'm' is number of possible chars in the input string, if there are no duplicates n=m.
<br />
<br />
**Note:** For more details on each solution, please refer to their respective code; they are all extensively commented.
