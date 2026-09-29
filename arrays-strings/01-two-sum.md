## Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

### Approach
This solution uses a hash map to store each number and its index while scanning left to right. For every value, it checks whether the complementary value needed to reach the target has already appeared.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
This pattern is efficient because it avoids nested loops and works well for large inputs while still keeping the implementation short and readable.
