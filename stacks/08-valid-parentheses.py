def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False

    return not stack


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([{}])") is True
    print("Valid Parentheses tests passed.")
