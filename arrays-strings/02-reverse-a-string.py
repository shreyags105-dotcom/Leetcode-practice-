def reverse_string(text):
    chars = list(text)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)


if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("A man a plan a canal Panama") == "amanaP lanac a nalp a nam A"
    assert reverse_string("") == ""
    print("Reverse a String tests passed.")
