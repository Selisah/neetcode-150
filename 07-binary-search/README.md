# 07 · Binary Search (Easy) · Binary Search

Stack only has one easy problem (Valid Parentheses), so today we start the next section, **Binary Search**.

## The problem, in plain words
You get a list of integers `nums` that is **already sorted from smallest to biggest**, and a number `target`. Return the **index** of `target` in the list. If `target` isn't in the list, return `-1`.

Your solution should run in **O(log n)** time, so looping through every item one by one is not the goal here.

Examples:
- `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9` → `4` (9 is at index 4)
- `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2` → `-1` (2 isn't in the list)
- `nums = [5]`, `target = 5` → `0`

## Key concept: O(log n) and sorted data
When data is sorted, you don't have to look at everything. Each check can rule out a big chunk of the list at once. Cutting the search space in half over and over means a list of 1,000,000 items takes only about 20 steps, instead of up to 1,000,000. That's what "O(log n)" means.

Python tip: `//` is whole-number division, so `7 // 2` gives `3`. You'll need it for finding a middle index.

## How to run
```bash
python solution.py
```
