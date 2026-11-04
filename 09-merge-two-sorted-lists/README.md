# 09 · Merge Two Sorted Lists (Easy) · Linked List

## The problem
You are given the heads of two sorted linked lists, `list1` and `list2`, each sorted in non-decreasing order.

Merge the two lists into one sorted linked list and return the head of the merged list. The merged list should be made by splicing together the nodes of the two input lists.

## Examples
- `list1 = 1 -> 2 -> 4`, `list2 = 1 -> 3 -> 4` returns `1 -> 1 -> 2 -> 3 -> 4 -> 4`
- `list1 = []`, `list2 = []` returns `[]`
- `list1 = []`, `list2 = 0` returns `0`

## Constraints
- The number of nodes in each list is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both lists are sorted in non-decreasing order.

## How to run
```bash
python solution.py
```
