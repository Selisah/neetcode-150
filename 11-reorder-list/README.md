# 11 · Reorder List (Medium) · Linked List

## The problem
You are given the head of a singly linked list:

`L0 → L1 → L2 → ... → Ln-1 → Ln`

Reorder the list to be in the following form:

`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

You may not modify the values in the list's nodes. Only the nodes themselves may be changed. Modify the list in place; the function returns nothing.

## Examples
- `head = [1, 2, 3, 4]` becomes `[1, 4, 2, 3]`
- `head = [1, 2, 3, 4, 5]` becomes `[1, 5, 2, 4, 3]`

## Constraints
- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

## How to run
```bash
python solution.py
```
