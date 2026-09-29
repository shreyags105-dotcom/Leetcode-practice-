from collections import Counter


def is_anagram(s, t):
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    print("Valid Anagram tests passed.")
