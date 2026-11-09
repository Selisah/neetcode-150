# 13 · Copy List With Random Pointer (Medium) · Linked List

## The problem
A linked list of length `n` is given where every node has an additional `random` pointer, which could point to any node in the list or `null`.

Construct a deep copy of the list. The copy should consist of exactly `n` brand new nodes, where each new node's `val` matches the original, and its `next` and `random` pointers point to new nodes in the copied list so that the copied list represents the same structure. No pointer in the new list may point to a node in the original list.

Return the head of the copied list.

For input/output, the list is represented as `[val, random_index]` pairs, where `random_index` is the index of the node `random` points to (or `null`).

## Examples
- `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]` returns `[[7,null],[13,0],[11,4],[10,2],[1,0]]`
- `head = [[1,1],[2,1]]` returns `[[1,1],[2,1]]`
- `head = [[3,null],[3,0],[3,null]]` returns `[[3,null],[3,0],[3,null]]`

## Constraints
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or points to a node in the list.

## How to run
```bash
python solution.py
```
