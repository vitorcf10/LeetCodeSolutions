**My Solution**</br>
&ensp;  Description: For more details on the problem itself, check leetcode.com. In this solution, an auxiliary dictionary is created.
The numbers in the array are keys and their respective value is a list with the following structure [first time key appears in array, last time key appears in array, frequency of key in array].
With the dictionary, it is possible to find out the numbers with max frequency, within the max frequency numbers return the minimum sub-array size, and each sub-array size is given by -->
</br> sub-array size = 1 + last time key appears in array - first time key appears in array
</br>
</br>_Time Complexity:_ O(n), first the code iterates through every element in array(n), and then iterates through every element in the list of tuples.
This list is the size of every unique element in the array(m), however, 1<=m<=n in the worst-case scenario m=n generating O(m+n) = O(2n) = O(n).
</br>_Space Complexity:_ O(n), the same analysis done for time complexity can be done for space, the auxiliary dict has size m, the auxiliary list of tuples has also size m,
in a worst-case scenario(m=n), the extra space would be O(m+m) = O(n+n) = O(2n) = O(n).
</br>
</br>**Note:** For more details on the solution, please refer to its code; it is all extensively commented.
