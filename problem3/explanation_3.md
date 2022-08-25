# Explanation

Once the arrays are sorted the algorithm is simple.

Just pop off the largest numbers one by one and put them in the highest place value possible.


# Analysis

I'm using HeapSort since I wrote a MinHeap for the data structures project earlier and it was convenient.

The time complexity of the sort is O(n log n) and the complexity of scanning the elements is O(n), so this is O(n log n) over all.

The extra storage required is O(n), since in the MinHeap class I make an array 'self.elements'.

