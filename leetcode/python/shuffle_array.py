from typing import List

"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


def shuffle(nums: List[int], n: int) -> List[int]:
    # Use n as the middle index of the nums array (of len 2n)
    # Zip to make list of [(x1, y1), ..., (xn, yn)]
    new_lst = zip(nums[:n], nums[n:])

    # Sum with empty tuple hack for flattening
    result = list(sum(new_lst, ()))

    return result