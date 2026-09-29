## Problem: Best Time to Buy and Sell Stock (Easy)

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach
The code tracks the lowest price seen so far and computes the best profit whenever the current price exceeds that minimum. This keeps the calculation linear.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
This problem teaches the importance of evaluating each day in context rather than looking at every possible pair of days.
