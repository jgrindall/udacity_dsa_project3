# Explanation


Perform a binary search, keeping the true answer between estimate0 and estimate1.

I start with estimate1 = n/2, which is an upper bound for n>=5.

Stop when our estimates are within 0.5 of each other and just check them both.


# Analysis


The algorithm is O(log n) and requires no extra storage.
