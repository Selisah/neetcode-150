from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice in nums, else False."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([7], False),
        ([-1, 0, -1], True),
    ]

    passed = 0
    for nums, expected in tests:
        result = contains_duplicate(nums)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: contains_duplicate({nums}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
