from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """Return True if the linked list has a cycle, otherwise False."""
    # TODO: your solution here
    pass


def build(values: List[int], pos: int) -> Optional[ListNode]:
    """Build a list from values. If pos >= 0, the tail points back to index pos."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1], 0, True),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 2, 3, 4, 5], 4, True),
        ([1, 1, 1], -1, False),
    ]

    passed = 0
    for values, pos, expected in tests:
        result = has_cycle(build(values, pos))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: has_cycle({values}, pos={pos}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
