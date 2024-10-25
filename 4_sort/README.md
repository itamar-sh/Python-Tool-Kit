# Sort
We familiar with classic algorithm sorts of O(n*log(n)) and some algorithms of O(n) in case of some assumption on the elements size.

The attributes of sorting algorithms are:
1) In Place - If the algorithm return new array or use more than constant space is not in place.
2) Stable - Only relevant for In Place algorithm - Return array with the original order of two equilvant elements.

# Classic algorithms
QuickSort, BubbleSort, MergeSort, InsertionSort

# Linear Sort Algorithms - O(n) - using assumptions of on Elements Input Size
RadixSort, BucketSort, CountingSort

### Counting sort
Using cumulative count on frequencies array to know the final location of each element.
This algorithm takes O(n+k) while n is length of nums and k is max(n)-min(n).
This algorithms need to major assumption that k is O(n) to stay linear.
Also if the values are not numberic we will need smart way to holds frequncies array. Is it possilbe?
Also if the values are not positive we will need shift the range.

# TO Do
1 - Implement counting sort with range of values and not only max_value.
2 - Try to implement counting sort with non numeric elements.
