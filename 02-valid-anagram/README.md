# 02 · Valid Anagram (Easy) · Arrays & Hashing

## The problem, in plain words
You get two strings, `s` and `t`. Return `True` if `t` is an **anagram** of `s`, meaning it uses exactly the same letters, the same number of times each, just possibly in a different order. Otherwise return `False`.

- `"anagram"` and `"nagaram"` → `True` (same letters, same counts)
- `"rat"` and `"car"` → `False` (`t` has no `t`, `s` has no `c`)
- `"aab"` and `"abb"` → `False` (same letters, but different counts)

You can assume the strings only contain lowercase English letters.

## Beginner-friendly hint
Yesterday you used a **set** to ask "have I seen this before?" Today you need more than yes/no: you need **"how many times have I seen it?"** That's exactly what a dictionary is for. Count the letters in `s`, count the letters in `t`, and compare the two counts.

Quick shortcut first: if the two strings have different lengths, they can't be anagrams.

## Key concept: dictionaries as counters
A Python dictionary (`dict`) stores **key → value** pairs. Here, each key is a letter and each value is how many times that letter shows up.

```python
counts = {}
for ch in "hello":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

What's going on in that middle line:
- `counts.get(ch, 0)` means "give me the current count for `ch`, or `0` if it isn't in the dictionary yet."
- `+ 1` bumps it up by one.
- `counts[ch] = ...` saves the new count back under that letter.

Two dictionaries are equal with `==` when they have the same keys with the same values, no matter what order things were added in:

```python
{'a': 1, 'b': 2} == {'b': 2, 'a': 1}   # True
```

Looking up and updating a key in a dictionary is **O(1)** on average (instant, no scanning), so counting a whole string takes **O(n)** time.

### Bonus thought (after you solve it)
Another approach is sorting both strings and comparing them (`sorted(s) == sorted(t)`). It works, but sorting is O(n log n). The counting approach is O(n), and it's the pattern you'll reuse a lot in this section.

## How to run
```bash
python solution.py
```
