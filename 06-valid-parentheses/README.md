# 06 · Valid Parentheses (Easy) · Stack

Best Time to Buy and Sell Stock was the only easy problem in Sliding Window, so today we start the next section, **Stack**.

## The problem, in plain words
You get a string `s` made up only of the characters `(`, `)`, `{`, `}`, `[` and `]`. Return `True` if the brackets are valid, and `False` if not.

The brackets are valid when:
- every opening bracket is closed by the **same type** of bracket,
- brackets are closed in the **right order**, and
- every closing bracket has a matching opening bracket before it.

Examples:
- `"()"` → `True`
- `"()[]{}"` → `True`
- `"{[]}"` → `True` (the `[]` sits fully inside the `{}`)
- `"(]"` → `False` (a round bracket can't be closed by a square one)
- `"([)]"` → `False` (the brackets overlap instead of nesting)
- `"("` → `False` (it never gets closed)

## Key concept: the stack
A stack is a pile of items where you can only add to the top or take from the top, like a stack of plates. The last thing you put on is the first thing you take off ("last in, first out").

In Python, a plain list works as a stack:

```python
stack = []
stack.append("a")   # push "a" on top -> ["a"]
stack.append("b")   # push "b" on top -> ["a", "b"]
top = stack[-1]     # peek at the top -> "b"
stack.pop()         # take the top off -> ["a"]
print(len(stack) == 0)  # is it empty? -> False
```

Both `append` and `pop` from the end of a list are **O(1)**, which is why lists make good stacks.

## How to run
```bash
python solution.py
```
