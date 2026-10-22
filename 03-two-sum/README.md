# 03 · Two Sum (Easy) · Arrays & Hashing

## The problem, in plain words
You get a list of numbers, `nums`, and a number called `target`. Find the **two different positions** in the list whose numbers add up to `target`, and return those two positions (indices) as a list.

- `nums = [2, 7, 11, 15]`, `target = 9` → `[0, 1]` (because `2 + 7 = 9`)
- `nums = [3, 2, 4]`, `target = 6` → `[1, 2]` (because `2 + 4 = 6`)
- `nums = [3, 3]`, `target = 6` → `[0, 1]` (you can't use the same spot twice, but two spots can hold the same number)

You can assume there's always exactly one answer. Return the smaller index first.

## Beginner-friendly hint
The slow way is checking every pair with two loops. Instead, walk through the list once, and for each number ask: **"what number would I need to hit the target?"** That's `target - num`. If you've already seen that number earlier, you're done. To answer "have I seen it, and *where*?" instantly, keep a dictionary.

## Key concept: dictionaries that remember positions
Yesterday the dictionary mapped **letter → count**. Today it maps **number → the index where you saw it**.

```python
seen = {}
for i, num in enumerate([10, 20, 30]):
    seen[num] = i
print(seen)        # {10: 0, 20: 1, 30: 2}
print(20 in seen)  # True  (instant check, O(1))
print(seen[20])    # 1     (where 20 was)
```

A few things going on there:
- `enumerate(nums)` gives you both the index `i` and the value `num` on each loop.
- `x in seen` checks whether `x` is a **key** in the dictionary, and it's O(1) on average.
- `seen[x]` gives back the value stored under that key, here the index.

The trick for Two Sum: **check before you store.** For each number, first look for its partner (`target - num`) in `seen`. If it's not there, add the current number to `seen` and keep going. Checking first means you never pair a number with itself.

That gets you one pass through the list, so **O(n)** time, instead of the O(n²) two-loop version.

### Bonus thought (after you solve it)
Try writing the two-loop brute force too and compare. Seeing why the dictionary version is faster is the whole lesson of this section.

## How to run
```bash
python solution.py
```
