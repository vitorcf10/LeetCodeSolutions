**Brute Force Solution**<br />
Description: It iterates through every combination of two numbers until it finds the numbers that add up to the target.<br />
_Time Complexity:_ O(n^2), for every element it iterates through every other element.<br />
_Space Complexity:_ O(1), there are no auxiliary variables proportional to the size of the input array.<br />

**Dict/Hashmap Solution**<br />
Description: The main idea here is to have an auxiliary dictionary that stores every element in the array as a key and its indexes as values.For every element, calculate the element that is needed for the sum to add up to the target (needed = target - element). Then, check if the element is already in the auxiliary dictionary. If it is, return the element's index and the value of the key needed in the dictionary. If it isn't, just add the element to the dictionary.<br />
_Time Complexity:_ O(n), iterates only once through the entire input array.<br />
_Space Complexity:_ O(n), the size of the auxiliary dict is proportional to the size of input array.
