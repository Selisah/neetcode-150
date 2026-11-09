from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Add two numbers stored as reversed digit lists and return the sum list."""
    # TODO: your solution here
    pass


def build(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    tests = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9, 9], [0, 0, 1]),
        ([5], [5], [0, 1]),
        ([1, 8], [0], [1, 8]),
    ]

    passed = 0
    for a, b, expected in tests:
        result = to_list(add_two_numbers(build(a), build(b)))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: add_two_numbers({a}, {b}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
