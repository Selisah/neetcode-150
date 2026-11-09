from typing import List, Optional


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """Return a deep copy of the list."""
    # TODO: your solution here
    pass


def build(pairs: List[list]) -> Optional[Node]:
    nodes = [Node(v) for v, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if r is not None:
            nodes[i].random = nodes[r]
    return nodes[0] if nodes else None


def to_pairs(head: Optional[Node]) -> List[list]:
    index = {}
    cur = head
    i = 0
    while cur:
        index[id(cur)] = i
        cur = cur.next
        i += 1
    out = []
    cur = head
    while cur:
        out.append([cur.val, index[id(cur.random)] if cur.random else None])
        cur = cur.next
    return out


def original_ids(head: Optional[Node]) -> set:
    ids = set()
    while head:
        ids.add(id(head))
        head = head.next
    return ids


if __name__ == "__main__":
    tests = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        [],
        [[5, 0]],
    ]

    passed = 0
    for pairs in tests:
        head = build(pairs)
        orig = original_ids(head)
        copy = copy_random_list(head)
        result = to_pairs(copy)
        # the copy must not reuse any original node
        fresh = True
        cur = copy
        while cur:
            if id(cur) in orig or (cur.random and id(cur.random) in orig):
                fresh = False
            cur = cur.next
        ok = result == pairs and fresh
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: copy_random_list({pairs}) -> {result} (expected {pairs}, fresh nodes: {fresh})")

    print(f"\n{passed}/{len(tests)} tests passed")
