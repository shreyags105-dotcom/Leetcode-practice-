def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        remainder = target - value
        if remainder in seen:
            return [seen[remainder], index]
        seen[value] = index
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("Two Sum tests passed.")
