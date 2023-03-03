from typing import List
from itertools import accumulate
from operator import add

# Functional solution
def runningSum(nums: List[int]) -> List[int]:
    return list(accumulate(nums, add))

# Imperative solution
def runningSum(nums: List[int]) -> List[int]:
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result

# Example input
lst = [1,2,3,4]
print(runningSum(lst))