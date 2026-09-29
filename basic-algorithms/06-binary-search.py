def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([1], 1) == 0
    print("Binary Search tests passed.")
