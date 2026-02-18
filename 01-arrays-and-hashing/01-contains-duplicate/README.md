# Contains Duplicate

## Problem Description

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

- **Link**: [LeetCode - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **Difficulty**: Easy
- **Category**: Arrays & Hashing

## Solution 1: Brute Force
The simple approach is to compare every element with every other element.
- **Time Complexity**: $O(n^2)$
- **Space Complexity**: $O(1)$

```python
def containsDuplicateBruteForce(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

## Solution 2: Hash Set (Optimal)
Using a hash set allows for $O(1)$ lookups and insertions.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$

```python
def containsDuplicateHashSet(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

## Pythonic One-Liner
```python
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
```
