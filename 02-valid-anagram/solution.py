def is_anagram(s: str, t: str) -> bool:
    """Return True if t uses exactly the same letters as s (same counts), else False."""
    # TODO: your solution here
    pass


if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aab", "abb", False),
        ("a", "ab", False),
        ("", "", True),
        ("listen", "silent", True),
    ]

    passed = 0
    for s, t, expected in tests:
        result = is_anagram(s, t)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: is_anagram({s!r}, {t!r}) -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
