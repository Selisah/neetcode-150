from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the nth node from the end of the list and return the head."""
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
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
        ([1, 2, 3], 1, [1, 2]),
        ([5, 6, 7, 8], 3, [5, 7, 8]),
    ]

    passed = 0
    for values, n, expected in tests:
        result = to_list(remove_nth_from_end(build(values), n))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: remove_nth_from_end({values}, n={n}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
