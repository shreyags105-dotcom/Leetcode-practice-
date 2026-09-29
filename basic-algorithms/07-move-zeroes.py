def move_zeroes(nums):
    write_index = 0

    for number in nums:
        if number != 0:
            nums[write_index] = number
            write_index += 1

    while write_index < len(nums):
        nums[write_index] = 0
        write_index += 1

    return nums


if __name__ == "__main__":
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0, 0, 1]) == [1, 0, 0]
    assert move_zeroes([1, 2, 3]) == [1, 2, 3]
    print("Move Zeroes tests passed.")
