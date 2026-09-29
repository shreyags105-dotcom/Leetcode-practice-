def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["apple", "app", "apricot"]) == "ap"
    print("Longest Common Prefix tests passed.")
