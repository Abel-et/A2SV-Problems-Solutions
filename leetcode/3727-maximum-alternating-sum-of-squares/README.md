# 3727. Maximum-Alternating-Sum-of-Squares

**Difficulty:** Medium

**Problem:** [Maximum-Alternating-Sum-of-Squares](https://leetcode.com/problems/maximum-alternating-sum-of-squares)

---

You are given an integer array `nums`. You may **rearrange the elements** in any order.

The **alternating score** of an array `arr` is defined as:

- `score = arr[0]² - arr[1]² + arr[2]² - arr[3]² + ...`

Return an integer denoting the **maximum possible alternating score** of `nums` after rearranging its elements.

Example 1:**Input:** nums = [1,2,3]

**Output:** 12

**Explanation:**

A possible rearrangement for `nums` is `[2,1,3]`, which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

`score = 2² - 1² + 3² = 4 - 1 + 9 = 12`

Example 2:

**Input:** nums = [1,-1,2,-2,3,-3]

**Output:** 16

**Explanation:**

A possible rearrangement for `nums` is `[-3,-1,-2,1,3,2]`, which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

`score = (-3)² - (-1)² + (-2)² - (1)² + (3)² - (2)² = 9 - 1 + 4 - 1 + 9 - 4 = 16`

**Constraints:**

- `1 <= nums.length <= 10⁵`

- `-4 * 10⁴ <= nums[i] <= 4 * 10⁴`