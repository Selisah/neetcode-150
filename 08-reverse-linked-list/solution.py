from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse the linked list and return the new head."""
    # TODO: your solution here
    pass


def build(values: List[int]) -> Optional[ListNode]:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([7], [7]),
        ([1, 1, 2], [2, 1, 1]),
        ([10, 20, 30], [30, 20, 10]),
    ]

    passed = 0
    for values, expected in tests:
        result = to_list(reverse_list(build(values)))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: reverse_list({values}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
