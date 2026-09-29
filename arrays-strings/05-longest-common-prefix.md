## Problem: Longest Common Prefix (Easy)

**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
The method begins with the first string as the prefix and trims it until it matches the start of every other string in the list. This keeps the algorithm simple and effective.

### Complexity
- Time: O(n * m)
- Space: O(m)

### Notes
It is a good example of how gradually shrinking a candidate answer can lead to a correct result without scanning the whole problem space.
