# Explanation


Perform a binary search, keeping the true answer between estimate0 and estimate1.

I start with estimate1 = n/2, which is an upper bound for n>=5.

Stop when our estimate is guaranteed to be correct to the nearest whole number.


# Analysis


The algorithm is O(log n) and requires no extra storage.
