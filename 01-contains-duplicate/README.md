# 01 · Contains Duplicate (Easy)

**NeetCode 150 · Arrays & Hashing** · [LeetCode #217](https://leetcode.com/problems/contains-duplicate/)

## The problem, in plain words

You get a list of numbers called `nums`. Return `True` if **any number shows up more than once**. Return `False` if every number is unique.

```
[1, 2, 3, 1]  -> True   (1 appears twice)
[1, 2, 3, 4]  -> False  (all different)
[]            -> False  (nothing to repeat)
```

## Hint

Walk through the list one number at a time. Before moving on, ask yourself: *"Have I already seen this number?"* If yes, you're done. If not, remember it and keep going.

The trick is choosing something that can answer "have I seen this?" **instantly**, instead of re-scanning everything you've looked at so far.

## Key concept: sets and hash maps

A **hash map** (in Python, a `dict`) stores **key → value** pairs, like a phone contact list: name → number.

```python
ages = {"Liz": 20, "Ama": 22}
ages["Kofi"] = 19        # add a new key
print("Liz" in ages)     # True  -> checking a key is super fast
print(ages["Ama"])       # 22
```

A **set** is its little sibling: it only keeps the **keys**, no values. It's perfect when you just need to know "is this in here or not?"

```python
seen = set()
seen.add(5)
print(5 in seen)   # True
print(7 in seen)   # False
```

**Why they're fast:** a list checks `x in my_list` by looking at every item one by one (slow when the list is big). A set or dict uses *hashing*: it turns the key into an address and jumps straight there. That makes lookups roughly **O(1)**, which means constant time no matter how big it gets.

For this problem a set is all you need. You'll use full `dict`s (key → value) in the next few problems.

## Complexity to aim for

- **Time:** O(n), one pass through the list
- **Space:** O(n), for the set of numbers you've seen

## Try it

Fill in `solution.py`, then run:

```bash
python solution.py
```
