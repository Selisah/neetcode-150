from typing import List


def search(nums: List[int], target: int) -> int:
    """Return the index of target in the sorted list nums, or -1 if it isn't there."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1),
        (([5], 5), 0),
        (([5], 3), -1),
        (([1, 2, 3, 4, 5, 6, 7], 1), 0),
        (([1, 2, 3, 4, 5, 6, 7], 7), 6),
        (([2, 4, 6, 8], 6), 2),
        (([], 1), -1),
    ]

    passed = 0
    for (nums, target), expected in tests:
        result = search(nums, target)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: search({nums}, {target}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
