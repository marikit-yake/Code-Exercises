from typing import List

lst = [5, 32, 6, 7, 82, 2, 4, 6]

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    # Sorts numbers in ascending order
    # [2, 4, 5, 6, 6, 7, 32, 82]
    nums_sorted = sorted(nums)
    print(nums_sorted)

    # Returns list of indices
    # indicating how many numbers are smaller than n for n in nums
    return [nums_sorted.index(n) for n in nums]


print(smallerNumbersThanCurrent(lst))