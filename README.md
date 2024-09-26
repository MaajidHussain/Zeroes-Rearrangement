# Zeroes-Rearrangement
This program rearranges an array of integers by moving all zero values to the end while maintaining the order of non-zero elements.

Detailed Description:
The chocolate_factory function takes an array of integers as input and processes it to rearrange the elements such that all zero values are pushed to the end of the array. The function works as follows:

Initialization: It initializes an empty list new_array to store non-zero elements and a counter zero_count to track the number of zeroes in the input array.

Traversal: The function iterates through each element in the input array. If the element is non-zero, it is added to new_array. If the element is zero, the zero_count is incremented.

Appending Zeroes: After the iteration, the function appends the counted zeroes to the end of new_array using the extend method, creating a list of zeroes based on the count.

Return Value: Finally, the function returns the modified array with all non-zero elements followed by the zeroes.

Example 1:

Input :
8  – Value of N
[4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline

Output:
4 5 1 9 5 0 0 0

Example 2:

Input:
6 — Value of N.
[6,0,1,8,0,2] – Element of arr[0] to arr[N-1], While input each element is separated by newline

Output:
6 1 8 2 0 0
