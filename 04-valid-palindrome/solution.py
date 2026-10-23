def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards, ignoring case and non-alphanumeric characters."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("Was it a car or a cat I saw?", True),
        ("0P", False),
        ("No 'x' in Nixon", True),
        ("ab_a", True),
    ]

    passed = 0
    for s, expected in tests:
        result = is_palindrome(s)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: is_palindrome({s!r}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
