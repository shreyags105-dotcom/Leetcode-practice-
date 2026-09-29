## Problem: Binary Search (Easy)

**Link:** https://leetcode.com/problems/binary-search/

### Approach
Binary search keeps a left and right boundary and repeatedly compares the middle element to the target. It narrows the search range in half each iteration.

### Complexity
- Time: O(log n)
- Space: O(1)

### Notes
This approach only works on sorted data, so it is valuable for recognizing whether a problem is structured for divide-and-conquer search.
