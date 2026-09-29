## Problem: Move Zeroes (Easy)

**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
The function keeps a write pointer to the next non-zero slot and copies each non-zero value into place. Afterward, all remaining positions are filled with zeros.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
This is a classic in-place partitioning pattern that helps maintain order while minimizing extra memory use.
