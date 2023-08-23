**Brute Force Solution**
Description: It iterates through every combination of two numbers until it finds the numbers that add up to the target.
Time Complexity: O(n^2), for every element it iterates through every other element.
Space Complexity: O(1), there are no auxiliary variables proportional to the size of the input array.

**Dict/Hashmap Solution**
Description: The main idea here is to have an auxiliary dictionary that stores every element in the array as a key and its indexes as values. 
For every element, calculate the element that is needed for the sum to add up to the target (needed = target - element). 
Then, check if the element is already in the auxiliary dictionary. 
If it is, return the element's index and the value of the key needed in the dictionary. If it isn't, just add the element to the dictionary.
Time Complexity: O(n), iterates only once through the entire input array.
Space Complexity: O(n), the size of the auxiliary dict is proportional to the size of input array.
