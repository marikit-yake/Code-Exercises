from functools import reduce

def subtractProductAndSum(n: int) -> int:
    nums = [int(num) for num in list(str(n))]
    prod = reduce(lambda x, y: x * y,  nums)
    sum_ = reduce(lambda x, y: x + y, nums)
    return prod - sum_

import numpy as np
# Alt solution
def subtractProductAndSum(n: int) -> int:
    nums = list(map(int, str(n)))
    prod = np.product(nums)
    sum_ = np.sum(nums)
    return prod - sum_



print(subtractProductAndSum(234))