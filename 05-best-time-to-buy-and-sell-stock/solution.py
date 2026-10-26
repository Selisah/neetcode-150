from typing import List


def max_profit(prices: List[int]) -> int:
    """Return the max profit from buying once and selling once on a later day (0 if no profit is possible)."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([5], 0),
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 4),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    ]

    passed = 0
    for prices, expected in tests:
        result = max_profit(prices)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: max_profit({prices}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
