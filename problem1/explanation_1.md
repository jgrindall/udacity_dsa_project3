# Explanation


Perform a binary search, keeping the true answer between estimate0 and estimate1.

I start with estimate1 = n/2, which is an upper bound for n>=5.

Stop when our estimates are within 0.5 of each other and just check them both.


# Analysis


The algorithm is O(log n) in terms of time. 

It requires no additional storage other than a few integers, so O(1)
