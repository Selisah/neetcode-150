# 10 · Linked List Cycle (Easy) · Linked List

## The problem
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists if some node in the list can be reached again by continuously following the `next` pointer. Return `True` if there is a cycle in the linked list, otherwise return `False`.

(In the tests, `pos` is the index of the node that the tail's `next` pointer connects back to. `pos = -1` means there is no cycle. `pos` is only used to build the test list; it is not passed to your function.)

## Examples
- `head = [3, 2, 0, -4]`, `pos = 1` returns `True` (the tail connects back to the node at index 1)
- `head = [1, 2]`, `pos = 0` returns `True` (the tail connects back to the node at index 0)
- `head = [1]`, `pos = -1` returns `False`

## Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the list.

## How to run
```bash
python solution.py
```
