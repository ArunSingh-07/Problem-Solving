# Valid Anagram

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

- **Link**: [LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **Difficulty**: Easy
- **Category**: Arrays & Hashing

## Solution 1: Brute Force

```python
def BruteForce(s:str, t:str)-> bool:
    if len(s) != len(t):
        return False

    s_list = list(s)
    t_list = list(t)

    s_list.sort()
    t_list.sort()

    return s_list == t_list
```

## Solution 2: Hash Map (Optimal)
Use a frequency counter to count occurrences of each character.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$ (since character set size is fixed).

```python
def isAnagramHashMap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True
```

## Solution 3: Pythonic One-Liner (Counter)
Using the built-in `collections.Counter`.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$.

```python
from collections import Counter

def isAnagramCounter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```
