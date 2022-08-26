# Explanation

My solution is in two steps.

First, I find the rotation point.

For example, if the input array is  [6, 9, 10, 16, 19, 20, 24, 0, 3, 4] then the rotation index is 7.

To find it, I define three sets

A := [6, 9, 10, 16, 19, 20, 24]
B := [0]
C := [3, 4]]

I maintain one pointer which is always in A union B and another which is always in B union C.

I check all possible cases and halve the interval at each step.

Once the rotation point is identified I do another binary search, but in the array:

[6, 9, 10, 16, 19, 20, 24, 0, 3, 4, 6, 9, 10, 16, 19, 20, 24]

I ignore the first 6 elements and do a binary search on the elements from index 7 onwards: [...........  0, 3, 4, 6, 9, 10, 16, 19, 20, 24]

Once found, use the rotation point to get the "real" index in the original array.

There is probably a one-step solution to this, but this solution is O(log n) and has the advantage of also identifiying the pivot point.



# Analysis

In terms of time complexity, both steps are O(log n), so it it O(log n) overall.

It requires no additional storage other than a constant number of integers, so O(1)

