# Median
The Naive solution is O(n*log(n)) - sort and take the middle number.

One assumption you can use is to say the max and min value of the input are fixed and relatively small.
Than you can use histogram (frequencies dict) to go with two pointers from array start and end to meet in the middle.
Than your solution will be O(n+k) with O(k) space when k is the range between the max and min value of the input.

Finally the optimized solution uses quickselect and can be be done with O(n).

# Median of data stream
In case you can't hold all the frequencies information and sort it.
This question can be found here:
https://leetcode.com/problems/find-median-from-data-stream/description/


