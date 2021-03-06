# [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers `nums`.

A pair `(i,j)` is called good if `nums[i]` == `nums[j]` and `i` < `j`.

Return the number of _good_ pairs.

### Example 1:

```
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
```

### Constraints:

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

| Time   | Space  | Difficulty | Related Topics                    |
| ------ | ------ | ---------- | --------------------------------- |
| _O(n)_ | _O(1)_ | Easy       | `Array`<br>`Hash Table`<br>`Math` |
