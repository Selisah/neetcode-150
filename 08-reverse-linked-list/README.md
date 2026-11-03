# 08 · Reverse Linked List (Easy) · Linked List

Today we also start the next section, **Linked List**.

## The problem, in plain words
You get the `head` (the first node) of a singly linked list. Reverse the list and return the new head.

Examples:
- `1 -> 2 -> 3 -> 4 -> 5` becomes `5 -> 4 -> 3 -> 2 -> 1`
- `1 -> 2` becomes `2 -> 1`
- an empty list (`head = None`) stays empty, so return `None`

## Key concept: what a linked list is
A linked list is a chain of small objects called **nodes**. Each node holds a value (`val`) and a pointer to the next node (`next`). The last node's `next` is `None`. Unlike a Python list, you can't jump to the 3rd item directly; you have to start at the head and follow `next` one step at a time.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# build 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))

node = head
while node:             # walk the list until you fall off the end
    print(node.val)     # prints 1, 2, 3
    node = node.next
```

"Reversing" here means changing where each node's `next` points, not making a new list of values.

## How to run
```bash
python solution.py
```
