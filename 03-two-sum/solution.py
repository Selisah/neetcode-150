def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices [i, j] (i < j) of the two numbers in nums that add up to target."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 9, 4], 13, [2, 3]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]

    passed = 0
    for nums, target, expected in tests:
        result = two_sum(nums, target)
        ok = result is not None and sorted(result) == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: two_sum({nums}, {target}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
