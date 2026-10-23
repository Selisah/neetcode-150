# 04 · Valid Palindrome (Easy) · Two Pointers

You've finished all the easy Arrays & Hashing problems (Contains Duplicate, Valid Anagram, Two Sum). The rest of that section is medium, so today we start the next section, **Two Pointers**, with a friendly easy one. We'll come back to the medium hash map problems (like Group Anagrams) once you've got a couple more wins.

## The problem, in plain words
You get a string `s`. Ignore everything that isn't a letter or a digit (spaces, commas, colons, and so on), and treat uppercase and lowercase as the same. After cleaning it up like that, does it read the same forwards and backwards? Return `True` or `False`.

- `"A man, a plan, a canal: Panama"` → `True` (cleaned up it's `"amanaplanacanalpanama"`)
- `"race a car"` → `False` (cleaned up it's `"raceacar"`, which backwards is `"racaecar"`)
- `" "` → `True` (cleaned up it's an empty string, and empty reads the same both ways)

## Beginner-friendly hint
Put one finger at the start of the string and one at the end. Move them toward each other. Skip any character that isn't a letter or digit, then compare the two characters in lowercase. If they ever don't match, it's not a palindrome. If the fingers meet without a mismatch, it is.

## Key concept: two pointers
A "pointer" here is just an index variable, like `left = 0` and `right = len(s) - 1`. Instead of building a new reversed string, you walk inward from both ends at the same time.

```python
s = "abcba"
left, right = 0, len(s) - 1
while left < right:
    print(s[left], s[right])   # a a, then b b
    left += 1
    right -= 1
```

Two string helpers you'll want:
- `ch.isalnum()` is `True` if `ch` is a letter or a digit, so you can skip it when it's `False`.
- `ch.lower()` turns `"A"` into `"a"`, so `"A"` and `"a"` compare as equal.

This runs in **O(n)** time and uses **O(1)** extra space, since you never build a second string.

### Bonus thought (after you solve it)
There's a quick "cheat" version: build the cleaned string, then check `cleaned == cleaned[::-1]`. Try writing that too. It's also O(n) time, but it uses extra memory for the new string, which is why the two-pointer version is the one interviewers usually want to see.

### Connecting back to hash maps
No dictionary needed today, and that's part of the lesson: not every problem is a hash map problem. Asking "do I need to *remember* things I've seen?" (dictionary) versus "can I just compare from both ends?" (two pointers) is a great habit.

## How to run
```bash
python solution.py
```
