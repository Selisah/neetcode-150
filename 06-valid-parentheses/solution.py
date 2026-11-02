def is_valid(s: str) -> bool:
    """Return True if every bracket in s is closed by the same type, in the right order."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("{[]}", True),
        ("(]", False),
        ("([)]", False),
        ("(", False),
        ("]", False),
        ("((()))[{}]", True),
    ]

    passed = 0
    for s, expected in tests:
        result = is_valid(s)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: is_valid({s!r}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
